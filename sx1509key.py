import board
import busio
import adafruit_sx1509
import digitalio

class SX1509_Keypad:
    def __init__(self, rows, cols):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.sx1509 = adafruit_sx1509.SX1509(i2c)
        self.rows = rows
        self.cols = cols
        self.keys = [
            ['1', '2', '3', 'A'],
            ['4', '5', '6', 'B'],
            ['7', '8', '9', 'C'],
            ['*', '0', '#', 'D']
        ]
        self.key_down = None
        
        # Set rows as input with pull-up
        for r in self.rows:
            self.sx1509.pin_mode(r, adafruit_sx1509.INPUT_PULLUP)
        
        # Set cols as output
        for c in self.cols:
            self.sx1509.pin_mode(c, adafruit_sx1509.OUTPUT)
        
        # Attach interrupt to rows
        for r in self.rows:
            self.sx1509.enable_interrupt(r, adafruit_sx1509.RISING)
            self
