from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
import datetime

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
filename = f'{time_stamp}.mp4'

# print(time_stamp)
# print(width, height)

fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
capt_video = cv2.VideoWriter(filename,fourcc, 30.0,(width,height))

while True:
    img = ImageGrab.grab(bbox=(0,0,width, height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow('Screen Capture', img_final)
    capt_video.write(img_final)
    if cv2.waitKey(10) == ord('q'):
        break