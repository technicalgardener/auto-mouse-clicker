import functions
import pyautogui
import msvcrt
from time import sleep
import tkinter as tk
from tkinter import ttk

def infiniteAC(inter, but, clickType):
    trigger = True
    if clickType == "Single":
        try:
            while trigger == True:
                pyautogui.click(clicks=1, button=but)
                sleep(inter)
        except KeyboardInterrupt:
            trigger = False
            print('interrupted!')

    if clickType == "Double":
        try:
            while True:
                pyautogui.doubleClick(clicks= 1, button= but)
                sleep(inter)
        except msvcrt.getwch() == 'q':
            print('interrupted!')
    
def getVar():
    return clicks, interval, button

def finiteAC(inter, but, clickType, repeat):
    if clickType == "Single":
        pyautogui.click(clicks=repeat, interval=inter, button=but)
    else:
        pyautogui.doubleClick(clicks=repeat, interval=inter, button=but)