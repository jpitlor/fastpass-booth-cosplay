import board
import busio
from digitalio import DigitalInOut
from adafruit_pn532.spi import PN532_SPI


def init():
    global pn532
    spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
    cs_pin = DigitalInOut(board.D5)
    pn532 = PN532_SPI(spi, cs_pin, debug=False)
    
    ic, ver, rev, support = pn532.firmware_version
    print("Found PN532 with firmware version: {0}.{1}".format(ver, rev))
    pn532.SAM_configuration()


def wait_for_scan():
    print("Waiting for RFID/NFC card...")
    while True:
        uid = pn532.read_passive_target(timeout=0.5)
        print(".")
        if not uid is None:
            break
    print("Found card with UID:", [hex(i) for i in uid])
