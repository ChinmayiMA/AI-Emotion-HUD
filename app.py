import base64
import os

import cv2
import numpy as np
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from deepface import DeepFace

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, static_folder=BASE_DIR, static_url_path="")
CORS(app)


@app.get("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")


@app.get("/api/health")
def health():
    return jsonify({
        "status": "ok",
        "message": "Emotion backend is running"
    })


@app.post("/api/analyze")
def analyze():
    try:
        data = request.get_json(silent=True)

        if not data or "image" not in data:
            return jsonify({
                "error": "Missing image field"
            }), 400

        image_data = data["image"]

        if "," in image_data:
            image_data = image_data.split(",", 1)[1]

        image_bytes = base64.b64decode(image_data)
        image_array = np.frombuffer(image_bytes, dtype=np.uint8)
        frame = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

        if frame is None:
            return jsonify({
                "error": "Invalid image data"
            }), 400

        result = DeepFace.analyze(
            img_path=frame,
            actions=["emotion"],
            detector_backend="opencv",
            enforce_detection=False,
            silent=True
        )

        if isinstance(result, list):
            result = result[0]

        emotions = result.get("emotion", {})
        dominant_emotion = result.get("dominant_emotion", "unknown")

        confidence = 0

        if emotions:
            confidence = float(emotions.get(dominant_emotion, 0))

        return jsonify({
            "success": True,
            "emotion": dominant_emotion,
            "confidence": round(confidence, 2),
            "emotions": {
                key: round(float(value), 2)
                for key, value in emotions.items()
            }
        })

    except Exception as error:
        print("Analysis error:", repr(error))

        return jsonify({
            "success": False,
            "error": str(error)
        }), 500


if __name__ == "__main__":
    print("Starting AI Emotion HUD backend...")
    print("Open http://127.0.0.1:5000 in your browser")
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
