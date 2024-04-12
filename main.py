from printer import printer
from leds import leds
from nfc import nfc
import threading


def prepare_new_fastpass():
  printer.prepare_fastpass()


def print_fastpass():
  light_thread = threading.Thread(target=leds.start_print_pattern, name="Lights")
  light_thread.start()
  printer.print_new_fastpass()


def listen_for_magic_bands():
  nfc.init()
  printer.init()
  leds.init()

  while True:
    nfc.wait_for_scan()
    print_fastpass()


if __name__ == '__main__':
  bg_thread = threading.Thread(target=prepare_new_fastpass, name="Image Preparer")
  bg_thread.start()
  listen_for_magic_bands()
  
