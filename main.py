from printer import printer
from leds import leds
from nfc import nfc

def print_fastpass():
  # printer.print_new_fastpass()
  leds.start_print_pattern()


def listen_for_magic_bands():
  nfc.init()
  # printer.init()
  leds.init()

  while True:
    nfc.wait_for_scan()
    print_fastpass()


if __name__ == '__main__':
  listen_for_magic_bands()
  
