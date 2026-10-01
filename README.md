# Webcam App using Python OpenCV

A simple webcam application built with Python and OpenCV. It opens the default webcam, shows live video, mirrors the frame, adds a text overlay, saves screenshots, and exits with the ESC key.

## Features

- Open default webcam
- Live webcam video
- Mirror/flip view
- Text overlay on video
- Save screenshot with `s`
- Exit with `ESC`

## Requirements

- Python 3.8+
- OpenCV

## Installation

```bash
git clone https://github.com/tigayalakshit7/webcam-app.git
cd webcam-app
python -m venv .venv
```

Activate the virtual environment:

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python webcam_app.py
```

Press `s` to save `screenshot.jpg`.

Press `ESC` to exit the webcam app.

## Controls

| Key | Action |
|---|---|
| `s` | Save screenshot |
| `ESC` | Exit app |

## Project Structure

```text
webcam-app/
├── webcam_app.py
├── requirements.txt
├── README.md
├── .gitignore

```

## How It Works

1. `cv2.VideoCapture(0)` opens the default webcam.
2. `cap.read()` reads each video frame.
3. `cv2.flip(frame, 1)` creates a mirror effect.
4. `cv2.putText()` adds text on the video.
5. `cv2.imshow()` displays the webcam window.
6. `cv2.waitKey(1)` checks keyboard input.
7. `cv2.imwrite()` saves a screenshot when `s` is pressed.
8. ESC key breaks the loop and closes the app.

