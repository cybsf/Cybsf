# DOCUMENTATION ON https://github.com/cybsf
#PACKAGE IMPORT
from tkinter import *
import time
import RPi.GPIO as GPIO
import time
import _thread
import pygame

# VARIABLES
global threadFlag1
threadFlag1 = False

# GUI VARIABLES
ROOT = Tk()
global frame
INPUT_USER = StringVar()
    
# PIN VARIABLE
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

# GPIO GLOBAL CONFIG
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
    
# GPIO PIN CONFIG
GPIO.setup(redLEDpin, GPIO.OUT)
GPIO.setup(greenLEDpin, GPIO.OUT)
GPIO.setup(blueLEDpin, GPIO.OUT)

GPIO.setup(button1pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(button2pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

GPIO.setup(servoPin,GPIO.OUT)
p = GPIO.PWM(servoPin, 50)

# FRAMES

def letterCodeSpel_FRAME_BEGIN():
    backgroundColor = "#0078D7"
    
    frame.forget()
    initGUI()
    frame.configure(bg=backgroundColor)

    #login label
    LABEL1 = Label(frame, text="Gelieve uw wachtwoord in te geven")
    LABEL1.configure(bg=backgroundColor,fg='white',font=('Helvetica',48))
    LABEL1.place(relx=0.5,rely=0.4, anchor='center')

    #login entry
    INPUT_USER.set("")
    ENTRY1 = Entry(frame, textvariable = INPUT_USER, show='*')
    ENTRY1.configure(font=('Helvetica',24), justify='center')
    ENTRY1.place(relx=0.5,rely=0.55, anchor="center")
    
    #login button
    BUTTON1 = Button(frame, text="Aanmelden", command=letterCodeSpel_AUTH)
    BUTTON1.configure(font=('Helvetica',24))
    BUTTON1.place(relx=0.5,rely=0.65, anchor="center")
    
    ROOT.update()

def LETTERCODEGAME_FRAME_WRONG():
    backgroundColor = "#0078D7"

    frame.forget()
    initGUI()
    frame.configure(bg=backgroundColor)

    #login label
    LABEL2 = Label(frame, text="Verkeerd wachtwoord, probeer opnieuw.")
    LABEL2.configure(bg=backgroundColor,fg='white',font=('Helvetica',48))
    LABEL2.place(relx=0.5,rely=0.4, anchor='center')

    #login entry
    INPUT_USER.set("")
    ENTRY2 = Entry(frame, textvariable = INPUT_USER, show='*')
    ENTRY2.configure(font=('Helvetica',24),justify='center')
    ENTRY2.place(relx=0.5,rely=0.55, anchor="center")

    #login button
    BUTTON2 = Button(frame, text="Aanmelden", command=letterCodeSpel_AUTH)
    BUTTON2.configure(font=('Helvetica',24))
    BUTTON2.place(relx=0.5,rely=0.65, anchor="center")
    
    ROOT.update()
    
def DEEPFRYER_FRAME_BEGIN():
    backgroundColor = "#0078D7"

    frame.forget()
    initGUI()
    frame.configure(bg=backgroundColor)
    
    #deepfryer label
    LABEL3 = Label(frame, text="Opgelet!\n\nEr is brand uitgebroken!\n\nVind het correcte blusmiddel en duw op de knop.")
    LABEL3.configure(bg=backgroundColor,fg='white',font=('Helvetica',48))
    LABEL3.place(relx=0.5,rely=0.4, anchor="center")
    
    ROOT.update()
    buttonDeepfryer_AUTH()
    
def DEEPFRYER_FRAME_WRONG():
    backgroundColor = "#0078D7"

    frame.forget()
    initGUI()
    frame.configure(bg=backgroundColor)    
    
    #deepfryer label
    LABEL3 = Label(frame, text="Verkeerd blusmiddel")
    LABEL3 = LABEL3.configure(bg=backgroundColor,fg='white',font=('Helvetica',48))
    LABEL3.place(relx=0.5,rely=0.4, anchor='center')

    ROOT.update()
    
def TELEPHONE_FRAME_BEGIN():
    backgroundColor = "#0078D7"
    
    frame.forget()
    initGUI()
    frame.configure(bg=backgroundColor)
    
    #telephone label
    LABEL2 = Label(frame, text="Uw frietketel stond zo net in brand.\n\nHet is aan te raden om na het blussen van een brand\nnog steeds de brandweer te bellen.\n\n\nNaar welk nummer bel je?")
    LABEL2.configure(bg=backgroundColor,fg='white',font=('Helvetica',48))
    LABEL2.place(relx=0.5,rely=0.4, anchor='center')

    #telephone entry
    INPUT_USER.set("")
    ENTRY2 = Entry(frame, textvariable = INPUT_USER)
    ENTRY2.configure(font=('Helvetica',24),justify='center')
    ENTRY2.place(relx=0.5,rely=0.7, anchor="center")

    #telephone button
    BUTTON2 = Button(frame, text="Bellen", command=telephoneNumber_AUTH)
    BUTTON2.configure(font=('Helvetica',24))
    BUTTON2.place(relx=0.5,rely=0.8, anchor="center")

    ROOT.update()
    
def TELEPHONE_FRAME_WRONG():
    backgroundColor = "#0078D7"
    
    frame.forget()
    initGUI()
    frame.configure(bg=backgroundColor)
    
    #telephone wrong label
    LABEL2 = Label(frame, text="Verkeerd nummer, probeer nogmaals:")
    LABEL2.configure(bg=backgroundColor,fg='white',font=('Helvetica',48))
    LABEL2.place(relx=0.5,rely=0.4, anchor='center')

    #telephone wrong entry
    INPUT_USER.set("")
    ENTRY2 = Entry(frame, textvariable = INPUT_USER)
    ENTRY2.configure(font=('Helvetica',24),justify='center')
    ENTRY2.place(relx=0.5,rely=0.6, anchor="center")

    #telephone button
    BUTTON2 = Button(frame, text="Bellen", command=telephoneNumber_AUTH)
    BUTTON2.configure(font=('Helvetica',24))
    BUTTON2.place(relx=0.5,rely=0.7, anchor="center")

    ROOT.update()
    
def SMOKEDETECTOR_FRAME_BEGIN():
    backgroundColor = "#0078D7"

    frame.forget()
    initGUI()
    frame.configure(bg=backgroundColor)

    #smokedetector label
    LABEL2 = Label(frame, text="Ga na of je rookmelder correct werkt.")
    LABEL2.configure(bg=backgroundColor,fg='white',font=('Helvetica',48))
    LABEL2.place(relx=0.5,rely=0.4, anchor='center')

    ROOT.update()
    buttonSmokedetector_AUTH()
    
def SMOKEDETECTOR_FRAME_RIGHT():
    backgroundColor = "#0078D7"

    frame.forget()
    initGUI()
    frame.configure(bg=backgroundColor)

    LABEL2 = Label(frame, text="Vind de juiste sleutel en ontsnap!")
    LABEL2.configure(bg=backgroundColor,fg='white',font=('Helvetica',48))
    LABEL2.place(relx=0.5,rely=0.4, anchor='center')

    ROOT.update()
    
# SIDE FUNCTIONS

def blinkRedLED():
    GPIO.output(redLEDpin, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(redLEDpin, GPIO.LOW)
    time.sleep(0.5)
    
def blinkGreenLED():
    print("blinkGreenLED")
    GPIO.output(greenLEDpin, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(greenLEDpin, GPIO.LOW)
    time.sleep(0.5)
    
def blinkFastBlueLED():
    GPIO.output(blueLEDpin, GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output(blueLEDpin, GPIO.LOW)
    time.sleep(0.25)
    
def turnOnRedLED():
    GPIO.output(redLEDpin, GPIO.HIGH)

def turnOffRedLED():
    GPIO.output(redLEDpin, GPIO.LOW)
    
def turnOnGreenLED():
    GPIO.output(greenLEDpin, GPIO.HIGH)
    
def turnOffGreenLED():
    GPIO.output(greenLEDpin, GPIO.LOW)
    
# THREAD FUNCTIONS
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
    
def thread2LED():
    print("thread2LED")
    global threadFlag1
    while threadFlag1 == False:
        blinkFastBlueLED()
        
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

def thread5PlayStarWars():
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/Documents/StarWars60.wav")
    pygame.mixer.music.play()
    time.sleep(5)
    pygame.mixer.music.stop()
    
# MAIN FUNCTIONS

def initGUI():
    global frame
    frame = Frame(ROOT)
    frame.pack(fill='both',expand=1)
    ROOT.attributes("-fullscreen", True)
    ROOT.update()
    
def letterCodeSpel_AUTH():
    if(INPUT_USER.get() == "ABC"):
        print(":)")
        LABEL1text = "JUIST"
        blinkGreenLED()
        DEEPFRYER_FRAME_BEGIN()
    else:
        LABEL1text = "FOUT"
        blinkRedLED()
        LETTERCODEGAME_FRAME_WRONG()
        print(":(")
        
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
    
def telephoneNumber_AUTH():
    if INPUT_USER.get() == "112":
        blinkGreenLED()
        thread5PlayStarWars()
        SMOKEDETECTOR_FRAME_BEGIN()
    else:
        blinkRedLED()
        TELEPHONE_FRAME_WRONG()
    
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

    
def startGame():
    letterCodeSpel_FRAME_BEGIN()

# BEGIN PROGRAM

if __name__ == '__main__':
    initGUI()
    startGame()