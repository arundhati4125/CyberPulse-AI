import os
import joblib
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL = joblib.load(
    os.path.join(BASE_DIR, "models", "model.pkl")
)

ENCODERS = joblib.load(
    os.path.join(BASE_DIR, "models", "encoders.pkl")
)


def predict(features):

    prediction = MODEL.predict([features])[0]

    confidence = np.max(
        MODEL.predict_proba([features])[0]
    )

    attack = ENCODERS["label"].inverse_transform(
        [prediction]
    )[0]

    return attack, round(confidence * 100, 2)