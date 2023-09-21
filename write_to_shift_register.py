import RPi.GPIO as GPIO
import time
import threading
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 
clk = 21
clk_freq = 0.1
data = 20
GPIO.cleanup()
GPIO.setup(clk, GPIO.OUT)
GPIO.setup(data, GPIO.OUT)

try :
    in_stream = sys.argv[1] 

except :
    in_stream = (input("input : "))


def write(inp, clk_pin, clk_freq, data_pin) :
    GPIO.output(clk_pin, GPIO.LOW)
    GPIO.output(data_pin, GPIO.LOW)
    i = 0
    time.sleep(clk_freq)
    for bit in inp :
        GPIO.output(clk_pin, GPIO.LOW)
        GPIO.output(data_pin, int(bit))
        time.sleep(clk_freq)
        GPIO.output(clk_pin, GPIO.HIGH) 
        time.sleep(clk_freq)
        GPIO.output(clk_pin, GPIO.LOW)
        print(str(i) + " bit Written : " + bit)
        i+=1


write(in_stream, clk, clk_freq, data)
