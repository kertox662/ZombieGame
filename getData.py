import json as js
from PIL import Image,ImageTk
import sys

def loadSettings(sFile = "data/configs.json"):
    if sys.platform == 'win32':
        sFile = ".\\" + sFile.replace("/","\\")

    with open(sFile) as jsonFile:
        data = js.load(jsonFile)
    return data

def loadImage(imagePath):
    if sys.platform == 'win32':
        imagePath = ".\\" + imagePath.replace("/","\\")
    img = Image.open(imagePath)
    imgTk = ImageTk.PhotoImage(image = img)
    return imgTk

def loadAnimation(animBase, frameNum):
    animFrames = [0]*frameNum
    for i in range(1, frameNum + 1):
        img = loadImage(animBase + 'Frame{}.png'.format(i))
        animFrames[i - 1] = img
    
    return animFrames
