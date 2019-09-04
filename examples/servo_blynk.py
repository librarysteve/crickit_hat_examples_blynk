# Example for servo
# Use with slider widget 
# Set the range from 0 to the maximum rotation of your servo ex 180
# Max value goes in the box that by default has 255
import blynklib
from adafruit_crickit import crickit

BLYNK_AUTH = 'authkeyhere'

# exclude server and port for use with Blynk server (this is for a local server)
blynk = blynklib.Blynk(BLYNK_AUTH, server='SERVER_IP_HERE', port='8080')

@blynk.handle_event('write V5')
def move_servo1(pin, value):
    crickit.servo_1.angle = int(value[0])

while True:
    blynk.run()
