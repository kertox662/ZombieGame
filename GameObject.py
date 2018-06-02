from tkinter import *
from getData import loadSettings
from PIL import Image, ImageTk

class GameObject:
    def __init__(self, initx, inity, objType, id, sprite, screen, camera, xOff = 0, yOff = 0):
        self.x = initx
        self.y = inity
        self.type = objType
        self.id = id
        self.screen = screen
        self.camera = camera
        if objType == "img" or objType == 'tile':
            # self.image = Image.open(sprite)
            # self.sprite = ImageTk.PhotoImage(image = self.image)
            self.sprite = sprite
        elif objType == "polygon":
            pass
        self.screenObj = -1
        self.xOff = xOff
        self.yOff = yOff

    def isOnScreen(self):
        if -100 - self.screen.width/2 <= self.x - self.camera.x + self.screen.width/2<= self.screen.width + 100:
            if -100 - self.screen.height/ 2<= self.y - self.camera.y + self.screen.height/2 <= self.screen.height + 100:
                return True
        
        return False
    
    def display(self):
        self.screen.canv.delete(self.screenObj)
        if self.isOnScreen():
            if self.type == "img" or self.type == 'tile':
                self.screenObj = self.screen.canv.create_image(self.x - self.camera.x + self.xOff + self.screen.width/2, self.y - self.camera.y + self.yOff + self.screen.height/2, image = self.sprite)

        

