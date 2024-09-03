# TASK 3- Creating a StopWatch App
# Overview
As part of my initial assignment during the internship at **Prodigy InfoTech** I developed a Python program that contains a basic stopwatch app implementation in Python using the Tkinter library for the graphical user interface (GUI). The app allows users to start, pause, and reset a timer, displaying the elapsed time in minutes, seconds, and milliseconds.
# StopWatch Algorithm
The stopwatch app uses a simple algorithm to update the timer display:
- **Initialize Timer Variables:** The app initializes the timer variables minutes, seconds, and milliseconds to 0.
- **Start Timer:** When the user clicks the start button, the app starts a thread that updates the timer display every millisecond.
- **Update Timer Display:** The app updates the timer display by incrementing the milliseconds variable every millisecond. When milliseconds reaches 1000, it resets to 0 and increments the seconds variable. When seconds reaches 60, it resets to 0 and increments the minutes variable.
- **Pause Timer:** When the user clicks the pause button, the app stops the timer thread and disables the pause button.
- **Reset Timer:** When the user clicks the reset button, the app resets the timer variables to 0 and enables the start button.

# App Components
The app consists of the following components:
- **GUI:** The graphical user interface is implemented using Tkinter and provides a simple and intuitive way for users to interact with the app.
- **Timer Display:** The timer display is implemented using a Label widget and displays the elapsed time in minutes, seconds, and milliseconds.
- **Start Button:** The start button is implemented using a Button widget and starts the timer when clicked.
- **Pause Button:** The pause button is implemented using a Button widget and pauses the timer when clicked.
- **Reset Button:** The reset button is implemented using a Button widget and resets the timer to 0 when clicked.

# Features
The app has the following features:
- **Timer Display:** The app displays the elapsed time in minutes, seconds, and milliseconds.
- **Start Button:** The app has a start button that starts the timer.
- **Pause Button:** The app has a pause button that pauses the timer.
- **Reset Button:** The app has a reset button that resets the timer to 0

# Requirements
- **Python 3.x**
- **Tkinter**
