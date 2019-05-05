import functions
import pyautogui
import msvcrt
from time import sleep
import tkinter as tk
from tkinter import ttk

#===========
# GUI setup
#===========

# create instance of tkinter
main = tk.Tk()

# window title
main.title("AutoClicker Alpha")

###
# TIME INTERVAL CELL
###

# cell title
timeCell = ttk.LabelFrame(main, text='Click Interval')
timeCell.grid(column=0, row=0, padx=8, pady=4, columnspan=2)

# time labels
secLabel = ttk.Label(timeCell, text='seconds').grid(column=1, row=0, padx=8, sticky='W')
milliLabel = ttk.Label(timeCell, text='milliseconds').grid(column=3, row=0, padx=8, sticky='W')

# text boxes
seconds = tk.IntVar()
seconds_entered = ttk.Entry(timeCell, width=8, textvariable=seconds).grid(column=0, row=0, padx=8)

milliseconds = tk.IntVar()
milliseconds_entered = ttk.Entry(timeCell, width=8, textvariable=milliseconds).grid(column=2, row=0, padx=8)

###
# CLICK OPTIONS CELL
###

# cell title
optionsCell = ttk.LabelFrame(main, text='Click Options')
optionsCell.grid(column=0, row=2, padx=16, pady=8, sticky=tk.W)

# option labels
buttonLabel = ttk.Label(optionsCell, text='Mouse button:').grid(column=0, row=0, padx=18, pady=12)
clickLabel = ttk.Label(optionsCell, text='Click type:').grid(column=0, row=1, padx=18, pady=12)

# option boxes
button = tk.StringVar()
button_chosen = ttk.Combobox(optionsCell, width=8, textvariable=button, state='readonly')
button_chosen['values'] = ('left', 'right')
button_chosen.grid(column=1, row=0, padx=8)
button_chosen.current(0)

clickType = tk.StringVar()
clickType_chosen = ttk.Combobox(optionsCell, width=8, textvariable=clickType, state='readonly')
clickType_chosen['values'] = ('Single', 'Double')
clickType_chosen.grid(column=1, row=1, padx=8)
clickType_chosen.current(0)

###
# REPEAT CELL
###

# cell title
repeatCell = ttk.LabelFrame(main, text='Click Repeat')
repeatCell.grid(column=1, row=2, padx=16, pady=4, sticky=tk.NW)

# repeat box label
repeatLabel = ttk.Label(repeatCell, text='times').grid(column=2, row=0, padx=18, pady=12)

# Radio button creation
setColors = ['Red', 'Dark Sea Green']
radNames = ['Repeat', 'Repeat until stopped']

radVar = tk.IntVar()
radVar.set(99)

for name in range(2):
    curRad = tk.Radiobutton(repeatCell, text=radNames[name], variable=radVar, value=name)
    curRad.grid(column=0, row=name, pady=9, sticky=tk.W)

# number of times spinbox
times = tk.IntVar()
times_entered = tk.Spinbox(repeatCell, from_=1, to=1000, width=5)
times_entered.grid(column=1, row=0, padx=8)

###
# START STOP BUTTON
###
def runAutoClick():
    curInter = int(seconds.get()) + (int(milliseconds.get()) / 1000)
    curButton = button.get()
    curClick = clickType.get()
    curTimes = int(times_entered.get())
    curRadio = radVar.get()

    if curRadio == 0:
        functions.finiteAC(curInter, curButton, curClick, curTimes)
    elif curRadio == 1:
        functions.infiniteAC(curInter, curButton, curClick)

def stopAutoClick():
    exit

startButton = ttk.Button(main, text='Start', command=runAutoClick)
startButton.grid(column=0, row=3, pady=16)

stopButton = ttk.Button(main, text='Stop')
stopButton.grid(column=1, row=3, pady=16)

main.mainloop()

