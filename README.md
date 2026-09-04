# AI Emotion HUD

A futuristic real-time facial emotion analysis dashboard built with **HTML, CSS, JavaScript, Python, OpenCV, Flask, DeepFace and TensorFlow**.

AI Emotion HUD combines a browser-based camera interface with a Python backend to analyze selected camera frames and visualize detected emotions through an interactive futuristic HUD.

> **Educational and demonstration project.** Facial emotion recognition is experimental and should not be treated as a definitive measurement of a person's emotional state.

---

## ✨ Features

*  Live browser camera preview
*  DeepFace-powered facial emotion analysis
*  Real-time emotion confidence visualization
*  Dominant emotion detection
*  Angry tracking
*  Happy tracking
*  Sad tracking
*  Surprise tracking
*  Neutral tracking
*  Futuristic HUD interface
*  Responsive design
*  Local processing support
*  Lightweight browser frontend with Python backend

---

## 🏗️ Project Structure

```text
AI-Emotion-HUD/
│
├── index.html          # Main frontend page
├── style.css           # HUD styling and animations
├── script.js           # Camera handling and API communication
├── app.py              # Flask backend and emotion analysis
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 🔄 How It Works

```text
          Webcam
             │
             ▼
     Browser Camera
             │
             ▼
        JavaScript
             │
             │ Selected Frames
             ▼
        Flask API
             │
             ▼
      OpenCV Processing
             │
             ▼
        DeepFace
             │
             ▼
    TensorFlow / Keras
             │
             ▼
      Emotion Scores
             │
             ▼
      Browser HUD
```

The browser handles the camera interface and visualization. Selected camera frames are sent to the local Flask backend, where OpenCV and DeepFace perform facial emotion analysis. The resulting emotion scores are returned to the browser and displayed through the HUD.

---

# 🚀 Run Locally

## Requirements

Before running the project, make sure you have:

* **Python 3.11.x**
* **64-bit Python**
* A working webcam
* A modern web browser
* Windows, macOS or Linux

> **Python 3.11.x is recommended** for compatibility with the DeepFace/TensorFlow dependency stack used by this project.

---

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Emotion-HUD.git
cd AI-Emotion-HUD
```

Replace `YOUR-USERNAME` with your GitHub username.

---

## 2. Create a Virtual Environment

### Windows

```powershell
py -3.11 -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell prevents activation, you can use:

```powershell
venv\Scripts\activate
```

### macOS / Linux

```bash
python3.11 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## 3. Verify Python Version

After activating the virtual environment, run:

```bash
python --version
```

You should see:

```text
Python 3.11.x
```

---

## 4. Install Dependencies

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install all project dependencies:

```bash
python -m pip install -r requirements.txt
```

The project uses the following dependency stack:

```text
Flask==3.0.3
flask-cors==4.0.1
deepface==0.0.93
opencv-python==4.10.0.84
numpy==1.26.4
tensorflow==2.15.1
tf-keras==2.15.1
```

> DeepFace may download required model files during the first analysis. The first run can therefore take longer than subsequent runs.

---

# ▶️ Start the Application

The frontend and backend run separately during local development.

## 5. Start the Backend

Make sure the virtual environment is activated.

Run:

```bash
python app.py
```

The Flask server should start at an address similar to:

```text
http://127.0.0.1:5000
```

**Keep this terminal running.**

---

## 6. Start the Frontend

Open a **second terminal** in the project directory.

Run:

```bash
python -m http.server 8000
```

Then open:

```text
http://127.0.0.1:8000
```

Allow camera access when the browser asks for permission.

---

## 🖥️ Local Setup

Both the frontend and backend must be running:

```text
┌─────────────────────┐
│       Webcam        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Browser Frontend  │
│   :8000             │
└──────────┬──────────┘
           │
       API Request
           │
           ▼
┌─────────────────────┐
│   Flask Backend     │
│   :5000             │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ OpenCV + DeepFace   │
│ TensorFlow / Keras  │
└──────────┬──────────┘
           │
      Emotion Scores
           │
           ▼
┌─────────────────────┐
│    HUD Display      │
└─────────────────────┘
```

---

# 🛠️ Troubleshooting

## `ModuleNotFoundError: No module named 'flask'`

Make sure the virtual environment is activated and run:

```bash
python -m pip install -r requirements.txt
```

---

## `ModuleNotFoundError: No module named 'deepface'`

Run:

```bash
python -m pip install deepface==0.0.93
```

Or reinstall all dependencies:

```bash
python -m pip install -r requirements.txt
```

---

## TensorFlow DLL Error on Windows

If you encounter an error such as:

```text
Failed to load the native TensorFlow runtime
```

or:

```text
DLL initialization routine failed
```

first verify:

```bash
python --version
```

Make sure you are using **Python 3.11.x 64-bit**.

Windows users may also need the **Microsoft Visual C++ Redistributable for Visual Studio 2015–2022 (x64)**.

---

## Camera Not Working

Make sure:

1. Your browser has camera permission.
2. No other application is currently using the webcam.
3. You are opening the frontend through the local HTTP server:

```text
http://127.0.0.1:8000
```

rather than relying on a direct `file://` URL.

---

## Backend Not Connecting

Make sure `app.py` is running and that the Flask server is available at:

```text
http://127.0.0.1:5000
```

Also verify that the API URL configured in `script.js` matches your backend address.

---

# 🌐 GitHub Pages

GitHub Pages can host the **frontend**, but it cannot execute Python, Flask, OpenCV, DeepFace or TensorFlow.

Therefore, uploading this project to GitHub Pages **does not by itself create a complete live AI demo**.

For a public deployment, the architecture should be:

```text
GitHub Pages / Web Host
          │
          ▼
     HTML + CSS + JS
          │
          │ API Requests
          ▼
   Python-Compatible Host
          │
          ▼
   Flask + DeepFace
          │
          ▼
      TensorFlow
```

The Flask backend must be deployed separately on a service that supports Python and the required dependencies.

After deploying the backend, update the API endpoint in `script.js` to point to the deployed backend.

Example:

```javascript
const API_URL = "YOUR_DEPLOYED_BACKEND_URL";
```

> **Important:** GitHub Pages alone cannot run the Python backend.

---

# 🔐 Privacy & Limitations

When running locally, selected camera frames are sent to the local Flask server for analysis.

Facial emotion recognition is an experimental AI application and can produce inaccurate or subjective results.

The detected emotion should **not** be considered a definitive measurement of a person's actual emotional state and should not be used for medical, employment, security, legal or other high-stakes decisions.

---

# 🧰 Tech Stack

| Technology             | Purpose                               |
| ---------------------- | ------------------------------------- |
| **HTML5**              | Frontend structure                    |
| **CSS3**               | HUD design and animations             |
| **JavaScript**         | Camera handling and API communication |
| **Python**             | Backend development                   |
| **Flask**              | Backend API                           |
| **Flask-CORS**         | Cross-origin API support              |
| **OpenCV**             | Image/frame processing                |
| **DeepFace**           | Facial emotion analysis               |
| **TensorFlow / Keras** | Deep learning backend                 |

---

# 🔮 Future Improvements

* Face bounding boxes
* Multiple-face tracking
* Emotion history graphs
* WebSocket-based streaming
* Cloud deployment
* Mobile camera controls
* Advanced 3D HUD effects
* Performance optimization
* Improved multi-face analysis

---

# 📜 License

Educational and demonstration use.

---

## 👩‍💻 Project

**AI Emotion HUD**

A browser-based experimental interface for visualizing AI-powered facial emotion analysis in real time.
