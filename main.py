import sys
from firebase import firebase
import Adafruit_DHT
import time
import RPi.GPIO as GPIO

PIN_A = 29
GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.OUT)
done = False
state = True


firebase = firebase.FirebaseApplication('https://raspberry3-8cb8d.firebaseio.com/',None)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, '4')
    time.sleep(5)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        firebase.patch('/data',{'temp':temperature , 'humd':humidity})
        if temperature > 30:
            print(temperature)
            try:
                while not done:
                        GPIO.output(PIN_A, state)

                        if state:
                                state = False
                        else:
                                state = True
                        time.sleep(0.2)
                GPIO.cleanup()
            except KeyboardInterrupt:
                    GPIO.cleanup()


    
   
