import time  # Import time for delays

# Mock the LED class for simulation
class LED:
    def __init__(self, pin):
        self.pin = pin
        print(f"LED initialized on GPIO {pin}")

    def on(self):
        print("LED ON")

    def off(self):
        print("LED OFF")

# Initialize the LED on GPIO pin 17
led = LED(17)

# Blink the LED 5 times
for _ in range(5):  # Use an underscore (_) as a variable when it's not needed
    led.on()  # Turn the LED on
    time.sleep(1)  # Wait for 1 second
    led.off()  # Turn the LED off
    time.sleep(1)  # Wait for 1 second
