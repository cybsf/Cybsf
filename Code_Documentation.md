# DEMO_v1 BPa escape room

## Description

This file contains a detailed documentation for the python program DEMO_v1 from top to bottom.
This program is used as a GUI for an escape room containing different buttons, LEDs, servo's, and such.
Visit https://github.com/cybsf for a demo video and a better layout.

## Code

```
from tkinter import *
import time
import RPi.GPIO as GPIO
import time
import _thread
import pygame
```

- **tkinter**: 	package for building the GUI
- **time**: 	package for using `time.sleep()`
- **_thread**:	package for using multithreading
- **pygame**:	package for playing the `.wav` files

```
global threadFlag1
threadFlag1 = False
```

- **threadFlag1**:	variable used to synchronize the threads

```
ROOT = Tk()
global frame
INPUT_USER = StringVar()
```

- **ROOT = Tk()**:				Initialize & declare the tkinter GUI root screen
- **global frame**:				Initialize the frame that fills up the root screen
- **INPUT_USER = StringVar()**:	Initialize & declare the input prompt variable

```
global redLEDpin
redLEDpin = 18
global greenLEDpin
greenLEDpin = 23
global blueLEDpin
blueLEDpin = 12

global button1pin
button1pin = 4
global button2pin
button2pin = 27

global servoPin
servoPin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
    
GPIO.setup(redLEDpin, GPIO.OUT)
GPIO.setup(greenLEDpin, GPIO.OUT)
GPIO.setup(blueLEDpin, GPIO.OUT)

GPIO.setup(button1pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(button2pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

GPIO.setup(servoPin,GPIO.OUT)
p = GPIO.PWM(servoPin, 50) # GPIO 17 for PWM with 50Hz
```

The code above initializes and declares all the GPIO pins used to interact with the program. Feel free to use your own pins instead of the once used in this program.
Mind that switching `GPIO.IN` to `GPIO.OUT` and vice versa could destroy your Raspberry Pi.

Some examples of the following code:
- **global redLEDpin; redLEDpin = 18**: 							Initialize and declare the GPIO pin for the red LED
- **global button1pin; button1pin = 4**:							Initialize and declare the GPIO pin for button1
- **global servoPin; servoPin = 21**:								Initialize and declare the GPIO pin for the servo
- **GPIO.setmode(GPIO.BCM)**:										Use the Broadcom GPIO numbers instead of board pin numbers
- **GPIO.setwarnings(False)**:										Turn off GPIO warnings
- **GPIO.setup(redLEDpin, GPIO.OUT)**:								Configure the redLEDpin (18) as an output
- **GPIO.setup(button1pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)**:	Configure the button1pin (4) as an input and place this in GPIO_UP (HIGH) state
- **GPIO.setup(servoPin,GPIO.OUT)**:								Configure the servoPin (21) as an output
- **p = GPIO.PWM(servoPin, 50)**:									Configure the servoPin for Pulse Width Modulation on 50Hz

```
def letterCodeSpel_FRAME_BEGIN():
    backgroundColor = "#0078D7"
    frame.forget()
    initGUI()
    frame.configure(bg=backgroundColor)
	
	LABEL1 = Label(frame, text="Gelieve uw wachtwoord in te geven")
    LABEL1.configure(bg=backgroundColor,fg='white',font=('Helvetica',48))
    LABEL1.place(relx=0.5,rely=0.4, anchor='center')
	
    #login entry
    INPUT_USER.set("")
    ENTRY1 = Entry(frame, textvariable = INPUT_USER, show='*')
    ENTRY1.configure(font=('Helvetica',24), justify='center')
    ENTRY1.place(relx=0.5,rely=0.55, anchor="center")
    time.sleep(0.25)
    #login button
    BUTTON1 = Button(frame, text="Aanmelden", command=letterCodeSpel_AUTH)
    BUTTON1.configure(font=('Helvetica',24))
    BUTTON1.place(relx=0.5,rely=0.65, anchor="center")
    time.sleep(0.25)
    print("end rootupdate")
    ROOT.update()
```

This code defines a single frame `letterCodeSpel_FRAME_BEGIN()` from the GUI. The other frames will not be explained because of the similarities

- **frame.forget()**:						Forget the previous frame
- **initGUI()**		:						Selfmade function to reload the GUI
- **frame.configure(bg=backgroundColor)**:	Configure the background color of the frame
- **LABEL1**:								Configure a label and place it on the frame
- **ENTRY1**:								Configure an entry and place it on the frame
- **BUTTON1**:								Configure a button and place it on the frame and run `letterCodeSpel_AUTH()` when pressed
- **ROOT.update()**:						Update the GUI

```
def blinkRedLED():
    GPIO.output(redLEDpin, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(redLEDpin, GPIO.LOW)
    time.sleep(0.5)
```

This code blinks the LED. The other LED functions will not be explained because of the similarities

- **GPIO.output(redLEDpin, GPIO.HIGH)**:	Turn on the LED
- **GPIO.output(redLEDpin, GPIO.LOW)**:		Turn off the LED
- **time.sleep(0.5)**:						Let the wait/sleep for 0.5sec

The following threadfunctions are used by the main functions of the program.

```
def thread1buttons():
    global threadFlag1
    threadFlag1 = False
    
    while threadFlag1 == False:
        time.sleep(0.25)
        button1status = GPIO.input(button1pin)
        button2status = GPIO.input(button2pin)
        
        if button1status == GPIO.LOW:
            blinkGreenLED()
            print("Right button!")
            time.sleep(0.5)
            threadFlag1 = True
                    
        if button2status == GPIO.LOW:
            blinkRedLED()
            print("Wrong button!")
            time.sleep(0.5)
```

This function checks if the button is pressed or not. After pressing the right button a green LED will blink and the threadflag will be set on true which 
stops the other threads used by the main function `buttonDeepfryer_AUTH()`. If the wrong button is pressed a red LED will blink.

- **button1/2status = GPIO.input(button1/2pin)**:	Checks if the button is pressed or not

```
def thread2LED():
    global threadFlag1
    while threadFlag1 == False:
        blinkFastBlueLED()
```

This function blinks the blue LED until the threadFlag1 from function `thread1buttons()`is True. 

```
def thread3servo():
    global threadFlag1

    while threadFlag1 == False:
        p.start(2)
        p.ChangeDutyCycle(4)
        time.sleep(0.25)
        p.ChangeDutyCycle(0)
        time.sleep(3.75)
        p.ChangeDutyCycle(2)
        time.sleep(0.25)
        p.ChangeDutyCycle(0)
        time.sleep(3.75)
```

This function turns the servo that has positions 2 to 12 that can be operated by the Raspberry Pi. 
This will continue until the threadFlag1 from function `thread1buttons()`is True. 

- **p.start(2)**:			Turn the servo to the start position (2)
- **p.ChangeDutyCycle(4)**:	Turn the servo to position 4

```
def Thread4FireSound():
    global threadFlag1
    mixer = pygame.mixer
    mixer.init()
	
    pygame.mixer.music.load("/home/pi/Documents/brand_intro.wav")
    pygame.mixer.music.play()
    time.sleep(3)
    
    while threadFlag1 == False:
        pygame.mixer.music.load('/home/pi/Documents/brand_main.wav')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True and threadFlag1 == False:
            continue
    
    pygame.mixer.music.load("/home/pi/Documents/brand_outro.wav")
    pygame.mixer.music.play()
```

This function plays an audio file on repeat until the threadFlag1 from function `thread1buttons()`is True. This is similar to the  `def thread5PlayStarWars()` function.

- **mixer = pygame.mixer**:		 												Declare the sound mixer
- **mixer.init()**:																Initialize the sound mixer
- **pygame.mixer.music.load("/home/pi/Documents/brand_intro.wav")**:			Load an audio file
- **pygame.mixer.music.play()**													Plays the audio file
- **while pygame.mixer.music.get_busy() == True and threadFlag1 == False:**:	Plays the audio file on repeat until threadFlag1 is true and the previous audio file is finished playing

The following functions are the main functions of this program
```
def initGUI():
    global frame
    frame = Frame(ROOT)
    frame.pack(fill='both',expand=1)
    ROOT.attributes("-fullscreen", True)
    time.sleep(0.25)
    ROOT.update()
```

- **frame = Frame(ROOT)**:					Initialize the frame into the root screen
- **frame.pack(fill='both',expand=1)**:		Packs the frame into the screen
- **ROOT.attributes("-fullscreen", True)**:	Sets the frame to fullscreen

```
def letterCodeSpel_AUTH():
    if(INPUT_USER.get() == "ABC"):
        LABEL1text = "JUIST"
        blinkGreenLED()
        DEEPFRYER_FRAME_BEGIN()
    else:
        LABEL1text = "FOUT"
        blinkRedLED()
        LETTERCODEGAME_FRAME_WRONG()
```

Ask the user for a lettercode input. If correct blink the LED green and continue to the following frame `DEEPFRYER_FRAME_BEGIN()`.
Otherwise blink the LED red and go to the 'try again' frame `LETTERCODEGAME_FRAME_WRONG()`.

```
def buttonDeepfryer_AUTH():
    global threadFlag1
    threadFlag1 = False
    
    _thread.start_new_thread(thread1buttons,())
    _thread.start_new_thread(thread2LED,())
    _thread.start_new_thread(thread3servo,())
    _thread.start_new_thread(Thread4FireSound,())
    
    while threadFlag1 == False:
        pass
    
    TELEPHONE_FRAME_BEGIN()
```

Starts 4 of the 5 threads and wait untill the right button is pressed in function`def thread1buttons()`. After the button press the function will start
the next frame `TELEPHONE_FRAME_BEGIN()`

```
def telephoneNumber_AUTH():
    if INPUT_USER.get() == "112":
        blinkGreenLED()
        thread5PlayStarWars()
        SMOKEDETECTOR_FRAME_BEGIN()
    else:
        blinkRedLED()
        TELEPHONE_FRAME_WRONG()
```

Ask the user for a lettercode input. If correct blink the LED green, play an audio file and continue to the following frame `SMOKEDETECTOR_FRAME_BEGIN`.
Otherwise blink the LED red and go to the 'try again' frame `TELEPHONE_FRAME_WRONG()`.

```
def buttonSmokedetector_AUTH():
    turnOnRedLED()
    buttonPushed1 = False;
    buttonPushed2 = False;
    while buttonPushed1 == False:
        button1status = GPIO.input(button1pin)
        
        if button1status == GPIO.LOW:
            turnOffRedLED()
            turnOnGreenLED()
            SMOKEDETECTOR_FRAME_RIGHT()
            buttonPushed1 = True
    
    while buttonPushed2 == False:
        button2status = GPIO.input(button2pin)
                    
        if button2status == GPIO.LOW:
            turnOffGreenLED()
            letterCodeSpel_FRAME_BEGIN()
            buttonPushed2 = True
```

Wait for the user to press the "smoke detector" button. If button pressed turn of the red LED, turn on the green LED and load the next frame `SMOKEDETECTOR_FRAME_RIGHT()`.
After that the reset button can be pressed to restart the game by running the function `letterCodeSpel_FRAME_BEGIN()`.

```
def startGame():
    letterCodeSpel_FRAME_BEGIN()

# BEGIN PROGRAM

if __name__ == '__main__':
    initGUI()
    startGame()
```

Both functions start the game and are used as initializers for the program.