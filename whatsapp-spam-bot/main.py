# Please use with great care ⚠ ⚠ ⚠

from pynput.keyboard import Key, Controller
import time

Keyboard = Controller()
time.sleep(10)

spam_str = input("What message do you want to span 🤣! ")

while True:
    for letter in spam_str:
        Keyboard.press(letter)
        Keyboard.release(letter)
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)