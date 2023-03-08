import time
import board
import busio
import adafruit_sx1509
from digitalio import DigitalInOut, Direction
from sx1509_led import SX1509_LED
from sx1509_keypad import SX1509_Keypad
#sx1509 implementatie in CircuitPython geschreven door ChatGPT op 20230308.

# Initialize LED and keypad
led = SX1509_LED(0)
keypad = SX1509_Keypad([1, 2, 3, 4], [5, 6, 7, 8])

# Set initial LED parameters
led.set_brightness(0)
led.breathe(5)

# Loop forever
while True:
    # Check if a key was pressed
    if keypad.key_down is not None:
        # Toggle LED flashing if 'Q' key was pressed
        if keypad.keys[keypad.key_down[0]][keypad.key_down[1]] == 'Q':
            led.stop_breathe()
            led.blink(2)
            time.sleep(0.5)
            led.stop_blink()
            led.breathe(5)
            
        # Clear key_down
        keypad.key_down = None
        
    # Update LED
    led.update()
    
    # Sleep for a bit to prevent busy looping
    time.sleep(0.01)
