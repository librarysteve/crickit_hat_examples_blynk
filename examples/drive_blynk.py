import blynklib
from adafruit_crickit import crickit

# Copy and paste api key between single quotes:
BLYNK_AUTH = 'authkeyhere'

# For use with blynk service exclude the server and port declarations
blynk = blynklib.Blynk(BLYNK_AUTH, server='SERVER_IP_HERE', port='8080')

# Recommended settings for 5V solenoid
crickit.drive_1.frequency = 1000


@blynk.handle_event('write V5')
def actuate_solinoid(pin, value):
    drive = crickit.drive_1
    drive.fraction = int(value[0])


while True:
    blynk.run()
