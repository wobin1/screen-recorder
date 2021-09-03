#import imageGrab from pillow
import datetime
from PIL import ImageGrab
import numpy as np 
import cv2 as cv
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S') 
print (timestamp)
file_name = f'{timestamp}.mp4'

fourcc = cv.VideoWriter_fourcc('m', 'p', '4', 'v')
capture_video = cv.VideoWriter(file_name, fourcc, 20.0, (width, height))


while True:
    img = ImageGrab.grab(bbox = (0, 0, width, height))
    np_processed_img = np.array(img)
    final_image = cv.cvtColor(np_processed_img, cv.COLOR_BGR2RGB)

    cv.imshow('screen Recorder', final_image)

    capture_video.write(final_image)

    if cv.waitKey(10) == ord('q'):
        break

    