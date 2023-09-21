import RPi.GPIO as GPIO
import time
import threading
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 
clk = 21
r_clk = 16
clk_freq = 0
data = 20
GPIO.cleanup()
GPIO.setup(clk, GPIO.OUT)
GPIO.setup(r_clk, GPIO.OUT)
GPIO.setup(data, GPIO.OUT)

try :
    in_stream = sys.argv[1] 

except :
    in_stream = (input("input : "))


def write(inp, clk_pin, r_clk_pin, clk_freq, data_pin) :
    print("Writing ...")
    GPIO.output(r_clk_pin, GPIO.LOW)
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
        print(str(i) + "'th bit Written : " + bit)
        i+=1
    print("Writing completed!")
    print("set to output ...")
    GPIO.output(r_clk_pin, GPIO.HIGH)


write(in_stream, clk, r_clk, clk_freq, data)
