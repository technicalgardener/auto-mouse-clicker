import tkinter as tk
from tkinter import ttk
from pynput.mouse import Button, Controller
from pynput import mouse
from pynput import keyboard
from tkinter import Menu
from tkinter import messagebox as msg
from time import sleep
from threading import Thread

class GUI():

    def __init__(self):
        self.pause = True
        self.clickType = 0

        # instance creation
        self.main = tk.Tk()

        # interface creation
        self.main.title("AutoClicker 0.1")
        self.main.iconbitmap('Mouse.ico')
        self.createWidgets()

    # method for creating message boxes
    # 0: info box || 1: warning box || 2: error box
    def _msgBox(self, type, title, text):
        if type == 0:
            msg.showinfo(title, text)
        if type == 1:
            msg.showwarning(title, text)
        if type == 2:
            msg.showerror(title, text)

    # prints variable contents to console
    # inclusion of repeatVar into vars is not neccesary as it is only utilized to evaluate which clicker method to use
    def _printVars(self):
        vars = self._getVars()
        print(vars, self.repeatVar.get())
    
    # collects variables frequently used together into a tuple
    def _getVars(self):
        # collect seconds and milliseconds variables and put them into one meaningful float for total seconds between clicks
        ttlTime = self.seconds.get() + (self.milliseconds.get() / 1000)

        # prepare the click type for use in pynput function calls
        click = self.click.get()
        if click == 'single':
            self.clickType = 1
        else:
            self.clickType = 2
        variables = (ttlTime, self.button.get(), self.clickType, self.repeatTime.get())
        return variables

    # method for click automation with finite iteration
    def finiteClickr(self):
        # vars = (0: total time || 1: left/right button || 2: single/double click || 3: times to repeat)
        vars = self._getVars()
        iter = vars[3]

        # small buffer in order to let user get to desired window
        sleep(5)
        mouse = Controller()

        # continue clicker until iteration has finished or pause button (makes pause True) is pressed
        while iter:
            if self.pause == True:
                break
            # check which button the user has selected to be clicked
            if vars[1] == "left":
                mouse.click(Button.left, vars[2])
                sleep(vars[0])
                iter -= 1
            else:
                mouse.click(Button.right, vars[2])
                sleep(vars[0])
                iter -= 1

    # method for click automation that continues until interrupted
    def infiniteClickr(self):
        vars = self._getVars()

        # small buffer in order to let user get to desired window
        sleep(5)
        mouse = Controller()

        # continue clicker indefinitely until interrupted through pause button or exit
        while True:
            if self.pause == True:
                break
            # evaluate which button user has selected to be clicked
            if vars[1] == "left":
                mouse.click(Button.left, vars[2])
                sleep(vars[0])
            else:
                mouse.click(Button.right, vars[2])
                sleep(vars[0])

#    def on_move(self, x, y):
#        if self.pause == False:
#            self.pauseClickr()
#            sleep(3)
#            self.startClickr()
#        else:
#            sleep(3)

    def on_press(self, key):
        if key == keyboard.Key.f1:
            self.startClickr()
        elif key == keyboard.Key.f3:
            self.pauseClickr()
        elif key == keyboard.Key.f2:
            if self.pause == False:
                self.pauseClickr()
                sleep(20)
                self.startClickr()
            else:
                pass

# not sure how to implement this 
# the idea is to pause app briefly when mouse movement detected
# this listener causes bad mouse lag
# instead modified f2 key above in on_press to briefely pause clicker
#
#   def moveDectect(self):
#       mouseListen = mouse.Listener(on_move=self.on_move)
#       mouseListen.start()
#

    def hotkeyDetect(self):
        keyListen = keyboard.Listener(on_press=self.on_press)
        keyListen.start()

    # start button command call
    def startClickr(self):
        self.pause = False
        radio = self.repeatVar.get()

        # evaluate which radio (set or infinite clicks) user has selected
        # and runs appropriate method in seperate thread
        # 0: set number of clicks
        if radio == 0:
            self.finClkrThread()
        # 1: infinite number of clicks
        elif radio == 1:
            self.infinClkrThread()
        # warning message displayed in the event no radio button has been selected
        else:
            self._msgBox(1, "Radio not selected", "Please select a repeat condition under 'Click Repeat' section to begin.")
    
    # method pauses clicker automation
    def pauseClickr(self):
        self.pause = True

    # method to put finite clicker in seperate thread
    def finClkrThread(self):
        self.run_thread = Thread(target=self.finiteClickr)
        self.run_thread.setDaemon(True)
        self.run_thread.start()

    # method to put infinite clicker in seperate thread
    def infinClkrThread(self):
        self.run_thread = Thread(target=self.infiniteClickr)
        self.run_thread.setDaemon(True)
        self.run_thread.start()

    # method to put hotkey detection in seperate thread
    def hotkeyDetectThread(self):
        self.run_thread1 = Thread(target=self.hotkeyDetect)
        self.run_thread1.setDaemon(True)
        self.run_thread1.start()

#    def moveDetectThread(self):
#       self.run_thread2 = Thread(target=self.moveDectect)
#        self.run_thread2.setDaemon(True)
#        self.run_thread2.start()

    # method to display info message about the app
    def about(self):
        self._msgBox(0,"AutoClicker alpha", "An autoclicker with GUI. \nIncludes threading for pausing app. \nCreated by CMikkelborg")

    # method to shut down GUI
    def quit(self):
        self.main.quit()
        self.main.destroy()

    # method to create GUI widgets and labels
    def createWidgets(self):
        ###
        # CLICK INTERVAL CELL
        ###

        # cell title
        timeCell = ttk.LabelFrame(self.main, text='Click Interval')
        timeCell.grid(column=0, row=0, padx=8, pady=4, columnspan=2)

        # time labels
        secLabel = ttk.Label(timeCell, text='seconds').grid(column=1, row=0, padx=8, sticky='W')
        milliLabel = ttk.Label(timeCell, text='milliseconds').grid(column=3, row=0, padx=8, sticky='W')

        # text boxes
        self.seconds = tk.IntVar()
        seconds_entered = ttk.Entry(timeCell, width=8, textvariable=self.seconds).grid(column=0, row=0, padx=8)

        self.milliseconds = tk.IntVar()
        milliseconds_entered = ttk.Entry(timeCell, width=8, textvariable=self.milliseconds).grid(column=2, row=0, padx=8)

        ###
        # CLICK OPTIONS CELL
        ###

        # cell title
        optionsCell = ttk.LabelFrame(self.main, text='Click Options')
        optionsCell.grid(column=0, row=2, padx=16, pady=8, sticky=tk.W)

        # option labels
        buttonLabel = ttk.Label(optionsCell, text='Mouse button:').grid(column=0, row=0, padx=18, pady=12)
        clickLabel = ttk.Label(optionsCell, text='Click type:').grid(column=0, row=1, padx=18, pady=12)

        # option boxes
        self.button = tk.StringVar()
        button_chosen = ttk.Combobox(optionsCell, width=8, textvariable=self.button, state='readonly')
        button_chosen['values'] = ('left', 'right')
        button_chosen.grid(column=1, row=0, padx=8)
        button_chosen.current(0)

        self.click = tk.StringVar()
        click_chosen = ttk.Combobox(optionsCell, width=8, textvariable=self.click, state='readonly')
        click_chosen['values'] = ('single', 'double')
        click_chosen.grid(column=1, row=1, padx=8)
        click_chosen.current(0)

        ###
        # REPEAT CELL
        ###

        # cell title
        repeatCell = ttk.LabelFrame(self.main, text='Click Repeat')
        repeatCell.grid(column=1, row=2, padx=16, pady=8, sticky=tk.NW)

        # repeat box label
        repeatLabel = ttk.Label(repeatCell, text='times').grid(column=2, row=0, padx=18, pady=12)

        # Radio button creation
        self.repeatVar = tk.IntVar()
        self.repeatVar.set(5)
        self.radNames = ['repeat', 'repeat until stopped']

        for name in range(2):
            curRadio = tk.Radiobutton(repeatCell, text=self.radNames[name], variable=self.repeatVar, value=name)
            curRadio.grid(column=0, row=name, pady=9.3, sticky=tk.W)

        # number of times spinbox
        self.repeatTime = tk.IntVar()
        timesRepeated = tk.Spinbox(repeatCell, from_=1, to=1000, width=5, textvariable=self.repeatTime)
        timesRepeated.grid(column=1, row=0, padx=8)

        ###
        # START STOP BUTTON
        ###

        startButton = ttk.Button(self.main, text='Start (F1)', command=self.startClickr)
        startButton.grid(column=0, row=3, pady=16)

        stopButton = ttk.Button(self.main, text='Stop (F3)', command=self.pauseClickr)
        stopButton.grid(column=1, row=3, pady=16)

        ###
        # MENUS
        ###

        menuBar = Menu(self.main)
        self.main.config(menu=menuBar)

        fileMenu = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Menu", menu=fileMenu)
        fileMenu.add_command(label='about', command=self.about)
        fileMenu.add_separator()
        fileMenu.add_command(label='exit', command=self.quit)

        self.hotkeyDetectThread()
#        self.moveDetectThread()
        self.main.mainloop()

