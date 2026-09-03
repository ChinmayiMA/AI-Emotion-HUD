from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from deepface import DeepFace
import base64
import cv2
import numpy as np
import os

app = Flask(__name__, static_folder=".", static_url_path="")
CORS(app)

EMOTIONS = ["angry", "happy", "sad", "surprise", "neutral"]

def decode_image(data_url):
    if "," in data_url:
        data_url = data_url.split(",", 1)[1]
    raw = base64.b64decode(data_url)
    image = cv2.imdecode(np.frombuffer(raw, dtype=np.uint8), cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError("Could not decode image")
    return image

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(".", path)

@app.get("/health")
def health():
    return jsonify({"status": "online", "service": "AI Emotion HUD"})

@app.post("/analyze")
def analyze():
    try:
        payload = request.get_json(silent=True) or {}
        image_data = payload.get("image")
        if not image_data:
            return jsonify({"error": "No image supplied"}), 400

        frame = decode_image(image_data)

        result = DeepFace.analyze(
            img_path=frame,
            actions=["emotion"],
            enforce_detection=False,
            detector_backend="opencv",
            silent=True
        )

        face_result = result[0] if isinstance(result, list) else result
        raw = face_result.get("emotion", {})

        emotions = {e: round(float(raw.get(e, 0.0)), 2) for e in EMOTIONS}
        dominant = max(EMOTIONS, key=lambda e: emotions[e])

        return jsonify({
            "emotions": emotions,
            "dominant_emotion": dominant,
            "confidence": emotions[dominant]
        })
    except Exception as exc:
        print("Analysis error:", str(exc))
        return jsonify({"error": "Emotion analysis failed", "details": str(exc)}), 500

if __name__ == "__main__":
    print("=" * 50)
    print("AI Emotion HUD is running!")
    print("Open → http://127.0.0.1:5000")
    print("=" * 50)
    app.run(host="127.0.0.1", port=5000, debug=False)
