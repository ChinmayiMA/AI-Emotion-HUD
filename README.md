# AI Emotion HUD

A futuristic real-time facial emotion analysis dashboard built with **HTML, CSS, JavaScript, Python, OpenCV and DeepFace**.

The browser provides the camera interface and HUD, while a local Python Flask server receives selected frames and runs DeepFace emotion analysis.

## Features

- Live browser camera preview
- Futuristic HUD interface
- Real-time emotion confidence bars
- Dominant emotion detection
- Angry, Happy, Sad, Surprise and Neutral tracking
- DeepFace-powered AI analysis
- Responsive design
- GitHub-ready structure

## Project Structure

```text
AI-Emotion-HUD/
├── index.html
├── style.css
├── script.js
├── app.py
├── requirements.txt
└── README.md
```

## How It Works

```text
Browser Camera → JavaScript → Flask API → DeepFace → Emotion Scores → HUD
```

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Emotion-HUD.git
cd AI-Emotion-HUD
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

DeepFace may download model files the first time it runs.

### 4. Start the backend

```bash
python app.py
```

### 5. Start the frontend

In a second terminal:

```bash
python -m http.server 8000
```

Open:

```text
http://127.0.0.1:8000
```

Allow camera access.

## GitHub Pages

GitHub Pages can host the frontend, but it cannot run Python/DeepFace.

For a live public AI demo:

- GitHub Pages = frontend
- A Python-compatible host = Flask + DeepFace backend
- Change `API_URL` in `script.js` to your deployed backend endpoint.

## Privacy

When run locally, camera frames are sent to your local Flask server for analysis. Facial emotion recognition is experimental and can be inaccurate; do not use it for high-stakes decisions.

## Tech Stack

HTML5 · CSS3 · JavaScript · Python · Flask · Flask-CORS · OpenCV · DeepFace · TensorFlow/Keras

## Future Improvements

- Face bounding boxes
- Multiple-face tracking
- Emotion history graphs
- WebSockets for streaming
- Cloud deployment
- Mobile camera controls
- 3D HUD effects

## License

Educational and demonstration use.
