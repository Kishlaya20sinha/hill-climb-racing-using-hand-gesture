# Hand Gesture Game Controller 🎮

## Author
**Kishlaya Sinha**

🔗 [LinkedIn Profile](https://www.linkedin.com/in/kishlaya-sinha-9134a0211)  
📧 kishlaya20sinha@gmail.com  
💻 [GitHub Profile](https://github.com/Kishlaya20sinha)

---

## 📌 Project Overview

Control games like **Hill Climb Racing** using your **hand gestures** detected via your **webcam**!  
The system simulates **keyboard presses** based on how many fingers you raise, creating an intuitive and hands-free gaming experience. 👋🕹️

---

## ✨ Features

- **Accelerate**: Raise **3 or more fingers** → Simulates **Right Arrow** key 🚀  
- **Brake**: Raise **fewer than 3 fingers** → Simulates **Left Arrow** key 🛑  
- **Real-time webcam gesture detection** 📸  
- **Keyboard input simulation** for seamless game control ⌨️  

---

## 🛠️ Technologies Used

- **Python** 🐍 – Core programming language  
- **OpenCV** 🎥 – Webcam access & image processing  
- **MediaPipe** ✋ – Hand landmark detection and tracking  
- **pynput** ⌨️ – Simulates keyboard keypresses  

---

## 🧠 How It Works

1. **Capture Video**: Frame-by-frame capture from your webcam.  
2. **Detect Hands**: MediaPipe identifies hand landmarks.  
3. **Count Fingers**: Based on landmarks, the system counts how many fingers are raised.  
4. **Map Actions**:
   - If **≥ 3 fingers**, simulate **Right Arrow** (Accelerate) ▶️  
   - If **< 3 fingers**, simulate **Left Arrow** (Brake) ◀️  
5. **Repeat**: Continuous loop for real-time interaction 🔄  

---

## ⚙️ Setup Instructions

### 📌 Prerequisites

- Python **3.7+** installed → [Download Python](https://www.python.org) ✅  
- A functional **webcam** 📹  

### 🚀Position Yourself: Ensure your hand is visible in the webcam. 👀

Start Gaming:

Raise 3+ fingers → Accelerate 🖐️➡️

Raise <3 fingers → Brake ✊⬅️

**Switch to your game window and play! 🏁**

### 📄 License
This project is licensed under the MIT License. ©️