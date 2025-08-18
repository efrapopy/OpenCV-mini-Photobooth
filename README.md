
# OpenCV mini Photobooth
Simple Photobooth system with opencv , tts , and stt.


## Attention 
```
⚠ program must be conected with internet ⚠
```
```
Make sure you have python version 13
```
## Installation

open in terminal and typing the text instead bellow

```bash
python -m venv ttsfoto 

```

```bash
ttsfoto/Scripts/activate
```

```bash
python -m pip install opencv-python pygame speechrecognition pyaudio edge-tts
```
## Settings Webcam 

If you using laptop or internal webcam/camera

```bash
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
````
If you using eksternal webcam/camera

```bash
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
```

## Voices Languages &  Gender

type this in terminal to check Language and gender you can used

```bash
edge-tts --list-voices
```
## Result


![App Screenshot](https://files.catbox.moe/poi1gc.jpg?text=App+Screenshot+Here)

![App Screenshot](https://files.catbox.moe/oejkao.jpg?text=App+Screenshot+Here)

![App Screenshot](https://files.catbox.moe/4v3olt.jpg?text=App+Screenshot+Here)


![App Screenshot](https://files.catbox.moe/7aktzx.jpg?text=App+Screenshot+Here)
