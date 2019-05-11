# urban-octo-system
This is a customizable mouse click automation tool. It's my first app!
### Features
- GUI w/ threaded callbacks
- adjustable delay between clicks
- left or right mouse button
- single or double clicks
- repeat set number of times or until stopped
- hotkeys to start and pause automation while in background
- 5 second delayed start

### Notes
F1 to start and F3 to stop. I understand this is not ideal for all situations, but it was created to suit a specific need of mine that does not have other functions bound to those keys. I would like to learn how to make multi-button hotkeys.
Originally I had built in the ability to pause the clicker on movement of the mouse, but using the mouse listener of pynput caused significant lag to the mouse. It would be great to learn a better implementation for this.

### To do
- customizable hotkeys
- customizable delayed start
- pause on mouse movement
- add better exception handling (does not break as is)

### Written with
- python
- tkinter library
- pynput library

### Acknowledgements
My inspiration for this app was from AutoClicker by mousetool, however I have neither seen nor used any of their code in the creation of this app. My goal was to use the knowledge I have gained of python and recently the tkinter and pynput libraries to create an original, similar looking app.
