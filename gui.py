from tkinter import *
from thresh import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # Start fishing button
        fishButton = Button(self, text="Start Fishing", highlightbackground='#3E4149', command=self.clickStartFishing)
        fishButton.pack(side=TOP, anchor=W, fill=X, expand=YES)

        # Calibrate button
        calibrateButton = Button(self, text="Calibrate", highlightbackground='#3E4149', command=self.clickCalibration)
        calibrateButton.pack(side=TOP, anchor=W, fill=X, expand=YES)

        # exit Button
        exitButton = Button(self, text="Exit", highlightbackground='#3E4149', command=self.clickExitButton)
        exitButton.pack(side=TOP, anchor=W, fill=X, expand=YES)


    def clickExitButton(self):
        exit()
    
    def clickCalibration(self):
        print('calibrate!')
        bb.calibration_check_required()
    
    def clickStartFishing(self):
        print('fish!')
        bb.start()

bb = bobber_bot()
gui = Tk()
app = Window(gui)
gui.wm_title("Bobberbot")
#gui.geometry("320x200")
gui.mainloop()
