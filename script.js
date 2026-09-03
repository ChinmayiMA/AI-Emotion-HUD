const API_URL = "http://127.0.0.1:5000";

const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const startButton = document.getElementById("startButton");
const statusElement = document.getElementById("status");
const emotionElement = document.getElementById("emotion");
const confidenceElement = document.getElementById("confidence");
const confidenceBar = document.getElementById("confidenceBar");
const scoresElement = document.getElementById("scores");
const messageElement = document.getElementById("message");

let cameraStream = null;
let analyzing = false;
let timer = null;

function setStatus(text, online) {
    statusElement.textContent = text;
    statusElement.className = online
        ? "status online"
        : "status offline";
}

async function checkBackend() {
    try {
        const response = await fetch(`${API_URL}/api/health`);
        if (!response.ok) {
            throw new Error("Backend unavailable");
        }

        setStatus("Backend online", true);
    } catch (error) {
        setStatus("Backend offline", false);
        messageElement.textContent =
            "Start Flask first, then refresh this page.";
    }
}

async function startCamera() {
    try {
        cameraStream = await navigator.mediaDevices.getUserMedia({
            video: {
                width: { ideal: 640 },
                height: { ideal: 480 },
                facingMode: "user"
            },
            audio: false
        });

        video.srcObject = cameraStream;
        startButton.textContent = "Camera Running";
        startButton.disabled = true;

        messageElement.textContent =
            "Camera active. Analyzing your expression...";

        captureFrame();
    } catch (error) {
        console.error(error);
        messageElement.textContent =
            "Camera permission was denied or no camera was found.";
    }
}

function captureFrame() {
    if (!video.videoWidth || !video.videoHeight) {
        timer = setTimeout(captureFrame, 1000);
        return;
    }

    canvas.width = 480;
    canvas.height = Math.round(
        video.videoHeight * (canvas.width / video.videoWidth)
    );

    const context = canvas.getContext("2d");
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    const image = canvas.toDataURL("image/jpeg", 0.75);

    analyzeImage(image);

    timer = setTimeout(captureFrame, 1500);
}

async function analyzeImage(image) {
    if (analyzing) {
        return;
    }

    analyzing = true;

    try {
        const response = await fetch(`${API_URL}/api/analyze`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ image })
        });

        const data = await response.json();

        if (!response.ok || !data.success) {
            throw new Error(data.error || "Analysis failed");
        }

        updateEmotion(data);
        setStatus("Backend online", true);
    } catch (error) {
        console.error(error);
        setStatus("Analysis error", false);
        messageElement.textContent =
            "The backend could not analyze this frame.";
    } finally {
        analyzing = false;
    }
}

function updateEmotion(data) {
    const emotion = data.emotion || "unknown";
    const confidence = Number(data.confidence || 0);

    emotionElement.textContent = emotion.toUpperCase();
    confidenceElement.textContent = `${confidence.toFixed(1)}%`;
    confidenceBar.style.width = `${Math.min(confidence, 100)}%`;

    scoresElement.innerHTML = "";

    const emotions = data.emotions || {};
    const sortedScores = Object.entries(emotions)
        .sort((a, b) => b[1] - a[1]);

    for (const [name, score] of sortedScores) {
        const row = document.createElement("div");
        row.className = "score-row";

        row.innerHTML = `
            <span>${name}</span>
            <span>${Number(score).toFixed(1)}%</span>
        `;

        scoresElement.appendChild(row);
    }

    messageElement.textContent =
        "Analysis updated successfully.";
}

startButton.addEventListener("click", startCamera);
checkBackend();
