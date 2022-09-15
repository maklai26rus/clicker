import keyboard
import pyautogui
import mouse
import time

isClicking = False


def set_clicker():
    global isClicking
    if isClicking:
        isClicking = False
        print("Кликер отключен")
    else:
        isClicking = True
        pyautogui.write(" Hello world!", interval = 0.4)
        print("Start clicer")


keyboard.add_hotkey('Z + ALT', set_clicker)


while True:
    if isClicking:
        # mouse.click(button='left')
        time.sleep(0.01)


