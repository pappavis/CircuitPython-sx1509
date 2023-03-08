import board
import busio
import adafruit_sx1509
#SX1509 circuitPython met ChatGPT
# datasheet https://cdn.sparkfun.com/datasheets/BreakoutBoards/sx1509.pdf

class SX1509_LED:
    def __init__(self, pin):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.sx1509 = adafruit_sx1509.SX1509(i2c)
        self.pin = pin
        
        # Set pin as output
        self.sx1509.pin_mode(self.pin, adafruit_sx1509.OUTPUT)
        
        # Set default values
        self.brightness = 255
        self.blink_rate = 0
        self.breathe_rate = 0
        
    def on(self):
        self.sx1509.digital_write(self.pin, True)
        
    def off(self):
        self.sx1509.digital_write(self.pin, False)
        
    def set_brightness(self, brightness):
        self.brightness = brightness
        self.sx1509.analog_write(self.pin, brightness)
        
    def blink(self, rate):
        self.blink_rate = rate
        self.sx1509.blink(self.pin, rate)
        
    def stop_blink(self):
        self.blink_rate = 0
        self.sx1509.stop_blink(self.pin)
        
    def breathe(self, rate):
        self.breathe_rate = rate
        self.sx1509.breathe(self.pin, rate)
        
    def stop_breathe(self):
        self.breathe_rate = 0
        self.sx1509.stop_breathe(self.pin)
        
    def update(self):
        if self.blink_rate > 0:
            self.sx1509.blink(self.pin, self.blink_rate)
        elif self.breathe_rate > 0:
            self.sx1509.breathe(self.pin, self.breathe_rate)
        else:
            self.sx1509.analog_write(self.pin, self.brightness)
