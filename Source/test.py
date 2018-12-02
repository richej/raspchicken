import lcddriver
import time
import RPi.GPIO as GPIO
import datetime
import ChickenDoorState.State as State


mode=GPIO.getmode()

GPIO.cleanup()

Forward=8
Backward=10
TasterHoch=18
TasterRunter=16
KontaktUnten=36
KontaktOben=38

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)

def Hochfahren():
    GPIO.output(Forward, GPIO.HIGH)
    print("Hoch")

def BewegungStop():
    GPIO.output(Forward, GPIO.LOW)
    lcd.lcd_clear()
    lcd.lcd_backlight("off")
    print("Stopp")

def Runterfahren():
    GPIO.output(Backward, GPIO.HIGH)
    print("Runter")

def TasterHoch():
    print("Taster HOCH gedrückt")
    lcd.lcd_clear()
    lcd.lcd_backlight("on")  
    Hochfahren()
    lcd.lcd_display_string("HOCH",1)

def TasterRunter():
    print("Taster RUNTER gedrückt")
    lcd.lcd_clear()
    lcd.lcd_backlight("on")  
    Runterfahren()
    lcd.lcd_display_string("RUNTER",1)




lcd = lcddriver.lcd()


GPIO.setmode(GPIO.BOARD)
GPIO.setup(TasterHoch, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(TasterRunter, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(KontaktOben, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(KontaktUnten, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.output(Forward, GPIO.LOW)
GPIO.output(Backward, GPIO.LOW)

# Ereignis-Prozedur für Eingang HIGH
def doIfHigh(channel):
    if channel == TasterHoch:    
        TasterHoch()
    elif channel == TasterRunter:  
        TasterRunter()
    elif channel == KontaktOben:
        BewegungStop()
    elif channel == KontaktUnten:
        BewegungStop()
   # else:                  # if port 25 != 1  
   #     lcd.lcd_clear()
    #    lcd.lcd_backlight("off")
     #   BewegungStop()


 
# Ereignis deklarieren
GPIO.add_event_detect(TasterHoch, GPIO.RISING, callback = doIfHigh, bouncetime = 200)
GPIO.add_event_detect(TasterRunter, GPIO.RISING, callback = doIfHigh, bouncetime = 200)
GPIO.add_event_detect(KontaktOben, GPIO.RISING, callback = doIfHigh, bouncetime = 200)
GPIO.add_event_detect(KontaktUnten, GPIO.RISING, callback = doIfHigh, bouncetime = 200)


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