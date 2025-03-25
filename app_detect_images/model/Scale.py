import cv2
import os
import numpy as np

class reScale():

    def __init__(self,image):
        self.image = image
    
    def changeScale(self):
        img = cv2.imread(self.image)  
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (224, 224))  
        imagenes = np.array(img)  

        return imagenes
        

