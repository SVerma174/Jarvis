<h1 align="center">🤖 Jarvis - Your Personal Assistant</h1>
<h3 align="center">An AI-Powered Assistant with Face Authentication & Voice Commands</h3>
<h2 align="center">College 5th Sem Project</h2>
<p align="center">
  <img src="https://img.shields.io/badge/Project-Active-brightgreen" alt="Project Status">
  <img src="https://img.shields.io/badge/License-MIT-blue" alt="License">
</p>

---

## 🚀 Overview

**Jarvis** is an advanced AI-powered personal assistant designed to enhance productivity and provide hands-free assistance. It integrates face authentication for secure access, hotword detection for seamless activation, and a browser-based interface for versatile functionality.

---

## ✨ Features

- 👤 **Face Authentication**: Secure login using facial recognition.
- 🎤 **Hotword Detection**: Activate Jarvis hands-free using a pre-configured hotword.
- 🗣️ **Speech Synthesis**: Responds dynamically with natural voice feedback.
- 🌐 **Browser-based UI**: Powered by Eel for smooth interaction and management.
- 🔒 **Security**: Ensures restricted access through reliable authentication methods.
- 🚀 **Multiprocessing**: Efficiently handles tasks and processes simultaneously.

---

## 🛠️ Tech Stack

- **Frontend**:
  - HTML5
  - CSS3
  - JavaScript (with Eel for Python integration)
- **Backend**:
  - Python 3.8+
  - Multiprocessing for handling concurrent tasks
  - OpenCV for face recognition
- **Tools**:
  - GitHub for version control
  - Visual Studio Code for development
- **Libraries & Frameworks**:
  - SpeechRecognition
  - pyttsx3 (for text-to-speech conversion)
  - OpenCV (for facial recognition)

---

## 📦 Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/jarvis-project.git
   cd jarvis-project
   ```

2. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   python run.py
   ```

4. **Setup Configuration**: Ensure your webcam and microphone are properly connected for authentication and voice interaction.

---

## 📊 Project Structure

- **`main.py`**: Initializes and manages the Eel web server, as well as face authentication.
- **`run.py`**: Handles multiprocessing for running hotword detection and assistant functionalities.
- **`engine/`**: Contains core features like face recognition, voice commands, and more.
- **`www/`**: Stores frontend assets such as HTML, CSS, and JavaScript files.

---

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

<p align="center">🚀 Happy Coding! 🚀</p>
