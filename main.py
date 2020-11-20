import pyautogui
from PIL import Image, ImageGrab
import time


# from numpy import asarray


def hit_key(key):
    pyautogui.keyDown(key)


def draw():
    pass


def take_screenshot():
    image = ImageGrab.grab().convert('L')
    return image


def day_night_checker(data):
    for i in range(200, 250):  # for width
        for j in range(600, 650):  # for height
            if data[i, j] > 120:
                return 'day'
            if data[i,j] < 100:
                return 'night'


def is_collide(data):
    if day_night_checker(data) == 'day':
        # rectangle for cactus
        for i in range(340, 360):
            for j in range(400, 480):
                if data[i, j] < 100:
                    hit_key('up')
                    return
        return
    if day_night_checker(data) == 'night':
        for i in range(340, 360):
            for j in range(400, 480):
                if data[i, j] > 100:
                    hit_key('up')
                    return
        return

if __name__ == '__main__':
    print('dino game starting in 3 seconds')
    time.sleep(3)
    hit_key('up')
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()

        is_collide(data)

'''
        # day night check rect
        for i in range(200, 250): # for width
            for j in range(600, 650): # for height
                data[i, j] = 200

        image.show()
        break
'''
