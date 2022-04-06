from tkinter import *
import tkinter
import sys
import RPi.GPIO as IO
import DHT22
from picamera import PiCamera
from Adafruit_ADS1x15 import ADS1115
from smbus import SMBus
import time
import datetime
from PIL import ImageTk, Image

root = Tk()
root.title("Wetterstation")
root.config(bg="#444444")
root.geometry("800x500+300+300")
IO.setmode(IO.BCM)
IO.setwarnings(False)

adc = ADS1115()
i2cbus = SMBus(1)
adc.start_adc(1)

cam = PiCamera()
cam.resolution = (550,420)

path = "file.jpg"
cam.capture(path)
img = Image.open(path)
img = ImageTk.PhotoImage(img)
    
def refresh():
    
    #Temperatur:
    temperature = "Fehler"
    while temperature=="Fehler" or temperature=="None":
        temperature = str(DHT22.getTemperature())
        print(temperature)
    temp.configure(text=temperature + "°C")
    
    #Feuchtigkeit:
    humidity = "Fehler"
    while humidity=="Fehler" or humidity=="None":
        humidity = str(DHT22.getHumidity())
        print(humidity)
    hum.configure(text=humidity + "%")
    
    #Bild
    cam.capture(path)
    img = Image.open(path)
    img = ImageTk.PhotoImage(img)
    panel.config(image = img)
    panel.image = img
    
    #Helligkeit:
    value = adc.read_adc(1)
    print(value)
    bright.config(font="Verdana 11 bold")
    if value<3000:
        weather = "Sonnenfinsternis"
        #bright.config(font="Verdana 20 bold")
    elif value>3000 and value<15000:
        weather = "Stark bewölkt"
    elif value>15000 and value<20000:
        weather = "Leicht bewölkt"
    elif value>20000:
        bright.config(font="Verdana 20 bold")
        weather = "Sonne"
    bright.config(text = weather)
    
    now = datetime.datetime.now()
    day = now.strftime("+%w")
    if day=="+0":
        day = "Sonntag"
    elif day=="+1":
        day = "Montag"
    elif day=="+2":
        day = "Dienstag"
    elif day=="+3":
        day = "Mittwoch"
    elif day=="+4":
        day = "Donnerstag"
    elif day=="+5":
        day = "Freitag"
    elif day=="+6":
        day = "Samstag"
    curTime = now.strftime("    %d - %m - %Y    %H : %M : %S")
    labelString = day + curTime
    timeLabel.config(text = labelString)

def close():
    
    print ("Programm beendet")
    cam.close()
    IO.cleanup()
    sys.exit()
    


tempLabel = Label(root,text="Temperatur:", bg="white", font="Verdana 12 bold", highlightthickness=2, highlightbackground="black", highlightcolor="black")
tempLabel.place(x=10, y=15, width=150, height=30)

temp = Label(root, bg="white", font="Verdana 20 bold", highlightthickness=2, highlightbackground="black", highlightcolor="black")
temp.place(x=10, y=50, width=150, height=50)

humLabel = Label(root,text="Feuchtigkeit:", bg="white", font="Verdana 12 bold", highlightthickness=2, highlightbackground="black", highlightcolor="black")
humLabel.place(x=10, y=110, width=150, height=30)

hum = Label(root, bg="white", font="Verdana 20 bold", highlightthickness=2, highlightbackground="black", highlightcolor="black")
hum.place(x=10, y=145, width=150, height=50)

brightLabel = Label(root,text="Wetter:", bg="white", font="Verdana 12 bold", highlightthickness=2, highlightbackground="black", highlightcolor="black")
brightLabel.place(x=10, y=205, width=150, height=30)

bright = Label(root, bg="white", font="Verdana 20 bold", highlightthickness=2, highlightbackground="black", highlightcolor="black")
bright.place(x=10, y=240, width=150, height=50)

timeLabel = Label(root, bg="white", font="Verdana 14 bold", highlightthickness=2, highlightbackground="black", highlightcolor="black")
timeLabel.place(x=200, y=450, width=550, height=30)

refreshBtn = Button(root, font="Verdana 10 bold", text="Aktualisieren", command = refresh, bg="#888888",highlightthickness=2, highlightbackground="black", highlightcolor="black")
refreshBtn.place(x=10, y=405, width=150, height=40)

exitBtn = Button(root, font="Verdana 10 bold", text="Beenden", command = close, bg="#888888",highlightthickness=2, highlightbackground="black", highlightcolor="black")
exitBtn.place(x=10, y=450, width=150, height=40)


panel = Label(root, image = img)
panel.image = img
panel.place(x=200, y=15, width=550, height=420)

refresh()

root.mainloop()