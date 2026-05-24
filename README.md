````markdown
# 🖐️ Gesture Scroll

Control your screen scroll using hand gestures — no mouse, no keyboard. Just your hand in front of the webcam.

Works on **all apps**: browsers, PowerPoint, social media, PDF viewers, VS Code — anything on your screen.

---

## ✋ Gestures

| Gesture | Action |
|---|---|
| ☝️ Index finger up | Scroll UP |
| ✊ Fist (all fingers down) | Scroll DOWN |
| 🖐️ Open palm (all fingers up) | STOP scrolling |

---

## 📁 Project Structure

```
gesture-scroll/
├── main.py               # Entry point
├── gesture_detector.py   # Hand tracking via MediaPipe
├── scroll_controller.py  # OS-level scroll via pynput
├── config.py             # Sensitivity & threshold settings
└── requirements.txt      # Dependencies
```

---

## ⚙️ Setup

**1. Clone the repo**
```bash
git clone https://github.com/fa22-bse-058-droid/gesture-scroll.git
cd gesture-scroll
```

**2. Create virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install "numpy==1.26.4"
pip install "mediapipe==0.10.9"
pip install "opencv-python==4.8.1.78"
pip install pyautogui pynput
```

**4. Run**
```bash
python main.py
```

---

## 🛠️ Configuration

Edit `config.py` to tune the experience:

| Setting | Default | Description |
|---|---|---|
| `SCROLL_SENSITIVITY` | `8` | Higher = faster scroll |
| `SCROLL_COOLDOWN` | `0.05` | Lower = more responsive |
| `GESTURE_THRESHOLD` | `0.05` | Hand movement sensitivity |
| `SHOW_PREVIEW` | `True` | Show/hide webcam window |
| `CAMERA_INDEX` | `0` | Default webcam |

---

## 📦 Dependencies

| Package | Version |
|---|---|
| mediapipe | 0.10.9 |
| opencv-python | 4.8.1.78 |
| numpy | 1.26.4 |
| pynput | latest |
| pyautogui | latest |

> ⚠️ **Important:** Use `numpy==1.26.4` — mediapipe is not compatible with NumPy 2.x

---

## 💻 Requirements

- Python 3.11
- Windows 10/11
- Webcam

---

## 👩‍💻 Author

**Ishna** — FA22-BSE-058  
COMSATS University Islamabad, Sahiwal Campus
````

