__author__ = 'Yann Trudel'
__date__ = "Summer 2015"

from tkinter import *  # Importing the module tkinter for use in the gui
from math import sin, floor  # Importing maths, for the equation of the perfect CS


class GUI(Tk):  # Graphical User Interface. Used for the creation of the window that will show the CS

    def __init__(self):

        """
        Initialization of all the variable use in the process of the CS Counter.
        Will return a running window showing a StopWatch and information about CS.
        """

        super().__init__()
        self.title("CS Counter")  # Title of the GUI
        self.cslabelper = Label(self, text="CS total :", font=1000)  # Text for 100% CS
        self.cslabelwanted = Label(self, text="CS 85% :", font=1000)  # Text for 85% CS
        self.time = Label(self, text="Time spent :", font=1000)  # Time spent in the game
        self.startb = Button(self, text="Start", command=self.start, font=1000)  # Start the timer
        self.stopb = Button(self, text="Stop", command=self.stop, font=1000)  # Stop the timer
        self.resetb = Button(self, text="Reset", command=self.reset, font=1000)  # Reset the timer to 0
        self.textcsper = Label(self, font=1000)  # Number of perfect CS
        self.textcswanted = Label(self, font=1000)  # Number of CS wanted
        self.timecount = IntVar()  # Variable that will be use to the incrementation of time in second.
        self.timeshow = StringVar()  # Time shown in string as for the use of mm:ss, graphical utility only.
        self.timeshow = "00:00"  # First show of the time
        self.timecount = 0  # Setting up the variable at 0
        self.csperf = IntVar()  # CS as 100% will be done. Setting up the variable as a Integer "Perfect CS".
        self.csperf = 0  # Setting the variable at 0
        self.texttime = Label(self, text=self.timeshow)  # Time spent in game in second use as a label, only graphical
        self.state = False  # Setting up the variable state, state will be use as if the counter is running or not
        self.timeinmin = IntVar()  # Setting up the variable to use after timecount, timeinmin will represent in mm:ss
        self.cswanted = IntVar()  # Peurcent as 85% for the moment, the variable is set up in cscalculus.
        self.cswanted = 0  # Setting at 0 the beginning. I want to make the 85% adjustable in the future,
        # as for now it will be used hardcoded.

        """ Placement in the window using a grid. Replacing grid with pack may help here """

        self.cslabelper.grid(column=0, row=0)  # Placement for the label
        self.cslabelwanted.grid(column=0, row=1)  # Placement for the label
        self.time.grid(column=0, row=2)  # Placement time
        self.startb.grid(column=0, row=3)  # Placement Start Button
        self.stopb.grid(column=1, row=3)  # Placement stop button
        self.resetb.grid(column=2, row=3)  # Placement reset button
        self.textcsper.grid(column=1, row=0)  # Placement text CS perfect
        self.textcswanted.grid(column=1, row=1)  # Placement text CS wanted
        self.texttime.grid(column=1, row=2)  # Placement text Time spent in game

    def updatewindow(self):

        """
        Use to update the root window.
        Will refresh the Perfect CS Counter, the CS Wanted and the time.
        """
        if self.state is True:  # If the state of the counter is on
            self.timecount += 1  # Adding one second to the time counter
            self.timeshow = str(floor(self.timecount / 60)).zfill(2) + ":" + str(round(self.timecount % 60)).zfill(2)
            # Setting up time shown in the mm:ss visual
            self.cscalculus()  # Calling the math behind the progression of perfect CS and wanted CS
            self.texttime.config(text=self.timeshow, font=1000)  # Updating the interface for the time shown
            self.textcsper.config(text=self.csperf, font=1000)  # Updating the interface for the 100% CS
            self.textcswanted.config(text=self.cswanted, font=1000)  # Updating the interface for the wanted mark
            self.after(1000, self.updatewindow)  # The function repeat itself after 1000ms = 1s

    def start(self):

        """
        Function when the button start will be clicked.
        :return: Change the state of the stopwatch
        """
        self.state = True  # Change the state to true, making run the stopwatch
        self.updatewindow()  # The function updatewindow being called to start the counter

    def stop(self):

        """
        Function when the stop button is clicked.
        :return: Change the state to false, stopping the stopwatch
        """
        self.state = False
        self.updatewindow()

    def reset(self):

        """
        Function called when the reset button is clicked. Used to reset the text shown on the screen back to 0 for the
        CS Perfection, CS Wanted and the time
        :return:
        """
        self.state = False
        self.timecount = "00:00"  # Writing back the timer to 00:00
        self.cswanted = 0  # Percent done by the time back to 0
        self.csperf = 0  # The perfect cs expected back to 0
        self.textcsper.config(text=self.csperf)  # Updating the visual
        self.textcswanted.config(text=self.cswanted)  # Updating the visual
        self.texttime.config(text=self.timecount)  # Updating the visual
        self.updatewindow()  # Calling the function to stop the stopwatch at the same time

    def cscalculus(self):

        """
        This is where the magic happens. The math behind the Perfect CS and the CS Wanted is done here
        :return: Change the value of the perfect CS and the cs wanted. As for now Perfect = 100% and Wanted = 85%
        """
        self.timeinmin = int(self.timecount / 60)  # Putting the timer in minutes, in base 10.
        time = self.timeinmin  # Changing to time only for a easier use in the math formula.
        self.csperf = 12.9 * time + ((3.68 * time * sin(12.8 * time) + 12.3 * sin((164 * time) * (164 * time)) + \
                                      22 * sin(16.7 * time - 3.68 * time * sin(12.8 * time)) - 104 * time) / (
                                     3.09 + 4.43 * time))  # Pure magic. Lots of work behind it.
        self.csperf = round(self.csperf, 2)  # Rounding the perfect cs to 2 digits.
        self.cswanted = 0.85 * self.csperf  # Setting up the CS wanted as 85% of the perfect CS
