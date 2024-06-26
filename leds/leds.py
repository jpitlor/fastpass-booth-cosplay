import time
from rpi_ws281x import PixelStrip, Color
import math

LED_COUNT = 15        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


def init():
    global strip
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()


def start_print_pattern():
    width = 5
    pixels = strip.numPixels()
    for cycle in range(50):
        for offset in range(pixels):
            for light in range(pixels):
                will_overflow = offset + width >= pixels
                if light in range(offset, offset + width) or (will_overflow and light in range(0, (offset + width) % pixels)):
                    strip.setPixelColor(light, Color(0, 255, 0))
                else:
                    strip.setPixelColor(light, 0)
            strip.show()
            wait_ms = 50 * (math.cos(cycle * math.pi / 12) + 1) + 15
            print(wait_ms)
            time.sleep(wait_ms / 1000)


