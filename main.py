from machine import Pin
from utime import sleep

led_verde = Pin(15, Pin.OUT)
led_amarillo = Pin(2, Pin.OUT)
led_rojo = Pin(4, Pin.OUT)

while True:
  led_rojo.value (1)
  print ("pare")
  sleep(2)
  led_rojo.value(0)
  print ("detengase")

  led_amarillo.value (1)
  print ("prevencion")
  sleep(2)
  led_amarillo.value(0)
  print ("alistese")

  led_verde.value (1)
  print ("continue")
  sleep(2)
  led_verde.value(0)
  print ("siga")

