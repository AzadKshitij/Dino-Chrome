# To check the project GoTo : 'https://chromedino.com/'
# import pyautogui
import time
import keyboard
from PIL import ImageGrab  # ,Image
# from numpy import asarray

COUNT = 0


def hit(key):
    # print('key pressed', key, COUNT)
    # pyautogui.keyDown(key)
    keyboard.press(key)
    # print('key pressed', key)
    # COUNT += 1


def isColide(data):
    for i in range(620, 800):
        for j in range(480, 500):
            if data[i, j] < 100:
                return True
    return False


def is_bird(data):
    for i in range(640, 750):
        for j in range(420, 440):
            if data[i, j] < 100:
                return True
    return False


def take_screenshort():
    image = ImageGrab.grab().convert('L')
    data = image.load()
    for i in range(620, 800):
        for j in range(480, 500):
            data[i, j] = 0
    for i in range(640, 750):
        for j in range(420, 440):
            data[i, j] = 71
    image.show()


if __name__ == "__main__":
    print('dino game is about to start.....')
    time.sleep(5)
    hit(' ')
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        if isColide(data):
            # print('upupupup')
            hit(' ')
        if is_bird(data):
            # print('down down down')
            hit('down')
            # time.sleep(0.01)
            hit('up')
    # take_screenshort()
