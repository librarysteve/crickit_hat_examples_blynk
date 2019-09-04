import blynklib
from adafruit_crickit import crickit

#Obtained from the app or server admin page
BLYNK_AUTH = 'authkeyhere'

#initialize Blynk in this script. The port for a local instance is 8080
blynk = blynklib.Blynk(BLYNK_AUTH, server='server_ip_address', port='8080')

'''
Blynk event handler breakdown:
@blynk.handle_event('write V0')
@blynk.handle_event = This section tells the script to wait for an action
('write V0') = "write" in this case means writing 
				to the pin(ie: turning the pin on)
				"V0" means virtual pin 0. 
You can set the on and off values of the virtual pin in the app
'''

# The edit this section to change how the app works.
# Define a function to happen here.
# Give the function parameters of 'pin' and 'value'
# Value returns a list so so use value[0] to get the base value
# Be sure to use float if you're using half speed on dc motors
@blynk.handle_event('write V0')
def when_button_is_pressed(pin, value):
    speed = float(value[0])
    motor1 = crickit.dc_motor_1 # This is how to call the dc motor object
    motor1.throttle = speed     # This is one way of defining the speed
	
# Run forever or until keyboard interrupt. 
while True:
    blynk.run()
