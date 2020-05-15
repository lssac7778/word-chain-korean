# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:25:41 2020

@author: lssac
"""


from pynput import keyboard

def one_key_input():
    keythrough = ""
    def on_press_(key):
        nonlocal keythrough
        keythrough = key
        return False
    def on_release_(key):
        return False
    
    # Collect events until released
    with keyboard.Listener(
            on_press=on_press_,
            on_release=on_release_) as listener:
        listener.join()
    
    if type(keythrough)!=str:
        keythrough = keythrough.char
    return keythrough

if __name__=="__main__":
    def on_press(key):
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
        except AttributeError:
            print('special key {0} pressed'.format(
                key))
    
    def on_release(key):
        print('{0} released'.format(
            key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False
    
    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
