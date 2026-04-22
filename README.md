# 🎨 AutoDraw Bot

A Python bot that automatically draws any image on your screen using mouse movements — perfect for drawing apps like Instagram's story brush, MS Paint, or any canvas tool.

---

## 📋 Table of Contents

- [How It Works](#how-it-works)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Stopping the Bot](#stopping-the-bot)
- [Tips for Best Results](#tips-for-best-results)
- [Project Structure](#project-structure)

---

## How It Works

The bot processes your image through a computer vision pipeline before drawing:

1. **Grayscale conversion** — The image is converted to black and white using OpenCV.
2. **Resizing** — The image is scaled to 50% of your screen height, preserving the aspect ratio.
3. **Edge detection** — Canny Edge Detection (`threshold: 50–150`) extracts the key outlines and details from the image.
4. **Contour extraction** — OpenCV finds all connected edge paths (contours) in the processed image.
5. **Centered drawing** — The bot calculates the screen center and maps each contour point to an absolute screen coordinate.
6. **Mouse simulation** — For each contour, the bot moves the mouse to the starting point, holds down the mouse button (`mouseDown`), drags along all points, then releases (`mouseUp`) — mimicking a real drawing stroke.

---

## Requirements

- Python 3.7+
- The following Python packages (see `requirements.txt`):

```
opencv-python
numpy
pyautogui
keyboard
```

---

## Installation

**1. Clone or download the project**

```bash
git clone https://github.com/your-username/autodraw-bot.git
cd autodraw-bot
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

> ⚠️ On Linux, `pyautogui` may require additional system packages:
> ```bash
> sudo apt-get install python3-tk python3-dev scrot
> ```

**3. Add your image**

Place the image you want to draw in the project folder and name it exactly:

```
image.png
```

> The bot only looks for `image.png` by default. See [Configuration](#configuration) to change this.

---

## Usage

**1. Open the drawing app** of your choice (Instagram story canvas, MS Paint, etc.)

**2. Run the bot**

```bash
python bot.py
```

**3. Switch to your drawing app** — you have **5 seconds** before drawing begins.

The bot will print the number of contours detected and start drawing automatically.

---

## Configuration

You can tweak the following values at the top of `bot.py`:

| Variable | Default | Description |
|---|---|---|
| `pyautogui.PAUSE` | `0.010` | Delay (seconds) between each mouse movement. Lower = faster drawing. |
| `max_size` | `50% of screen height` | Maximum size of the drawing on screen. |
| Canny thresholds | `50, 150` | Controls edge detection sensitivity. Lower values = more detail. |
| Image filename | `"image.png"` | The image file to draw. Change to any `.png` or `.jpg`. |

---

## Stopping the Bot

You have two ways to interrupt the bot mid-drawing:

| Method | How |
|---|---|
| **Space key** | Hold down `SPACE` at any time to stop cleanly. |
| **PyAutoGUI Fail-Safe** | Move your mouse to the **top-left corner** of the screen rapidly. |

Both methods will release the mouse button safely before stopping.

---

## Tips for Best Results

- **Use a thin brush** in your drawing app — the bot draws outlines, not filled shapes, so a fine brush gives the sharpest result.
- **Use high-contrast images** — images with clear, distinct edges (logos, portraits, line art) produce much better results than photos with gradients.
- **Don't move the canvas** while the bot is drawing — any scroll or pan will misalign the drawing.
- **Close other windows** that might pop up and steal focus during drawing.
- **Lower `pyautogui.PAUSE`** for faster drawing, but be careful — too fast may cause the drawing app to miss points.

---

## Project Structure

```
autodraw-bot/
│
├── bot.py              # Main bot script
├── requirements.txt    # Python dependencies
├── image.png           # Your drawing source image (you provide this)
└── README.md           # This file
```

---

## ⚠️ Disclaimer

This bot takes control of your mouse. Make sure you are not running other tasks in the background while it draws. Always have the **Space key** or **fail-safe** ready in case you need to stop it.
