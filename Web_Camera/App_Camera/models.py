import cv2, os, urllib.request
import numpy as np
from django.conf import settings

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, frame = self.video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret2, jpeg = cv2.imencode('.jpg', frame)

        return jpeg.tobytes()

class IPWebCam(object):
    def __init__(self):
        self.url = "http://192.168.105.202:8080"

    def __del__(self):
        cv2.destroyAllWindows()

    def get_frame(self):
        imgRest = urllib.request.urlopen(self.url)
        imgNp = np.array(bytearray(imgRest.read()), dtype=np.uint8)
        img = cv2.imdecode(imgNp,1)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #resize = cv2.resize(img, (640,480), interpolation=cv2.INTER_LINEAR)
        #frame_flip = cv2.flip(resize,1)
        
        
        ret, jpeg = cv2.imencode('.jpg',gray)
        return jpeg.tobytes()