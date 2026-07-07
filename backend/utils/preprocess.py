import os
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENCODERS = joblib.load(
    os.path.join(BASE_DIR, "models", "encoders.pkl")
)


def preprocess(data):

    protocol = ENCODERS["protocol_type"].transform(
        [data["protocol"]]
    )[0]

    service = ENCODERS["service"].transform(
        [data["service"]]
    )[0]

    flag = ENCODERS["flag"].transform(
        [data["flag"]]
    )[0]

    features = [

        0,                      # duration

        protocol,

        service,

        flag,

        data["srcBytes"],

        data["dstBytes"],

        0,

        0,

        0,

        0,

        0,

        data["loggedIn"],

        0,

        0,

        0,

        0,

        0,

        0,

        0,

        0,

        0,

        0,

        data["count"],

        data["srvCount"],

        0,

        0,

        0,

        0,

        data["sameRate"],

        0,

        0,

        data["hostCount"],

        data["hostCount"],

        data["sameRate"],

        0,

        data["sameRate"],

        0,

        0,

        0,

        0,

        0

    ]

    return features