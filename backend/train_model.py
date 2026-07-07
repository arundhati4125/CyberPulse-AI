import os
import joblib
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# -----------------------
# Dataset Path
# -----------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET = os.path.join(
    BASE_DIR,
    "dataset",
    "KDDTrain+.txt"
)

# -----------------------
# Column Names
# -----------------------

columns = [

'duration',
'protocol_type',
'service',
'flag',
'src_bytes',
'dst_bytes',
'land',
'wrong_fragment',
'urgent',
'hot',
'num_failed_logins',
'logged_in',
'num_compromised',
'root_shell',
'su_attempted',
'num_root',
'num_file_creations',
'num_shells',
'num_access_files',
'num_outbound_cmds',
'is_host_login',
'is_guest_login',
'count',
'srv_count',
'serror_rate',
'srv_serror_rate',
'rerror_rate',
'srv_rerror_rate',
'same_srv_rate',
'diff_srv_rate',
'srv_diff_host_rate',
'dst_host_count',
'dst_host_srv_count',
'dst_host_same_srv_rate',
'dst_host_diff_srv_rate',
'dst_host_same_src_port_rate',
'dst_host_srv_diff_host_rate',
'dst_host_serror_rate',
'dst_host_srv_serror_rate',
'dst_host_rerror_rate',
'dst_host_srv_rerror_rate',
'label',
'difficulty'

]

# -----------------------
# Read Dataset
# -----------------------

df = pd.read_csv(

    DATASET,

    names=columns

)

print("Dataset Loaded")

print(df.shape)

# -----------------------
# Encode Categorical Columns
# -----------------------

encoders = {}

categorical = [

'protocol_type',

'service',

'flag'

]

for col in categorical:

    le = LabelEncoder()

    df[col] = le.fit_transform(df[col])

    encoders[col] = le

# -----------------------
# Encode Labels
# -----------------------

label_encoder = LabelEncoder()

df["label"] = label_encoder.fit_transform(df["label"])

encoders["label"] = label_encoder

# -----------------------
# Features / Target
# -----------------------

X = df.drop(

    ["label", "difficulty"],

    axis=1

)

y = df["label"]

# -----------------------
# Train Model
# -----------------------

print("Training Random Forest...")

model = RandomForestClassifier(

    n_estimators=100,

    random_state=42

)

model.fit(X, y)

print("Training Complete")

# -----------------------
# Save Model
# -----------------------

MODEL_DIR = os.path.join(

    BASE_DIR,

    "models"

)

os.makedirs(

    MODEL_DIR,

    exist_ok=True

)

joblib.dump(

    model,

    os.path.join(MODEL_DIR, "model.pkl")

)

joblib.dump(

    encoders,

    os.path.join(MODEL_DIR, "encoders.pkl")

)

print("Model Saved")