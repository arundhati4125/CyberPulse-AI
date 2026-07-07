from flask import Blueprint, jsonify, request

from services.predictor import predict
from services.severity import get_severity
from services.recommendation import get_recommendation
from utils.preprocess import preprocess

predict_bp = Blueprint("predict", __name__)


@predict_bp.route("/predict", methods=["POST"])
def prediction():

    data = request.get_json()

    features = preprocess(data)

    attack, confidence = predict(features)

    severity = get_severity(attack)

    recommendation = get_recommendation(attack)

    status = "SAFE"

    if attack != "normal":
        status = "WARNING"

    return jsonify({

        "status": status,

        "attack": attack,

        "confidence": confidence,

        "severity": severity,

        "recommendation": recommendation

    })