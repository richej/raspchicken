import lcddriver
import time
import RPi.GPIO as GPIO
import datetime
import ChickenDoorState


mode=GPIO.getmode()

GPIO.cleanup()

AktuellerStatus = ChickenDoorState.State.Oben
BewHoch=8
BewRunter=10
TasterHoch=18
TasterRunter=16
KontaktUnten=24
KontaktOben=22

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BewHoch, GPIO.OUT)
GPIO.setup(BewRunter, GPIO.OUT)

def SetText(text,lineNum):
    lcd.lcd_display_string("%s                          "%text,lineNum)
   

def Hochfahren():
    GPIO.output(BewHoch, GPIO.HIGH)
    print("Hoch")

def Runterfahren():
    GPIO.output(BewRunter, GPIO.HIGH)
    print("Runter")

def BewegungStopOben():
    GPIO.output(BewHoch, GPIO.LOW)
    GPIO.output(BewRunter, GPIO.LOW)
    SetText("Stopp Oben",1)
    print("Stopp")

def BewegungStopUnten():
    GPIO.output(BewHoch, GPIO.LOW)
    GPIO.output(BewRunter, GPIO.LOW)
    SetText("Stopp Unten",1)
    print("Stopp")



def TasterHochGedrueckt():
    print("Taster HOCH gedrückt")
    SetText("Hoch",1)
    Hochfahren()

def TasterRunterGedrueckt():
    print("Taster RUNTER gedrückt")
    SetText("Runter",1)
    Runterfahren()




lcd = lcddriver.lcd()

print("TasterHoch: %s"%(TasterHoch))
GPIO.setmode(GPIO.BOARD)
GPIO.setup(TasterHoch, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(TasterRunter, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(KontaktOben, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(KontaktUnten, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.output(BewRunter, GPIO.LOW)
GPIO.output(BewHoch, GPIO.LOW)

# Ereignis-Prozedur für Eingang HIGH
def doIfHigh(channel):
    print("Channel %s is HIGH"%channel)
    if channel == TasterHoch:    
        TasterHochGedrueckt() 
    elif channel == TasterRunter:  
        TasterRunterGedrueckt()
    elif channel == KontaktOben:
        BewegungStopOben()
    elif channel == KontaktUnten:
        BewegungStopUnten()
   # else:                  # if port 25 != 1  
   #     lcd.lcd_clear()
    #    lcd.lcd_backlight("off")
     #   BewegungStop()



# Ereignis deklarieren
GPIO.add_event_detect(TasterHoch, GPIO.RISING, callback = doIfHigh, bouncetime = 2000)
GPIO.add_event_detect(TasterRunter, GPIO.RISING, callback = doIfHigh, bouncetime = 2000)
GPIO.add_event_detect(KontaktOben, GPIO.RISING, callback = doIfHigh, bouncetime = 2000)
GPIO.add_event_detect(KontaktUnten, GPIO.RISING, callback = doIfHigh, bouncetime = 2000)


if GPIO.input(KontaktUnten):
    AktuellerStatus = ChickenDoorState.State.Unten
else:
    AktuellerStatus = ChickenDoorState.State.StopMitte

    
GPIO.output(BewHoch, GPIO.HIGH)

lcd.lcd_backlight("on")  
lcd.lcd_display_string("Willkommen!",1)
time.sleep(3)
lcd.lcd_backlight("off")
lcd.lcd_clear()

while 1:
    time.sleep(0.1)
#lineA = 1
#lineB = 2
#for i in range(1, 5):
#    lcd.lcd_clear()
#    lcd.lcd_display_string("MIA",lineA)
#    lcd.lcd_display_string("LOTTA",lineB)
#    time.sleep(1)
#    tmp = lineA
#    lineA = lineB
#    lineB = tmp

print("hallo welt")