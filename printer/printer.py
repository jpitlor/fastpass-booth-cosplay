PRINTER_MAC = "60:6E:41:46:34:60"


def init():
    global printer
    printer = Ivy2Printer()
    printer.connect(PRINTER_MAC)


def print_new_fastpass():
    printer.print("./assets/fastpass.png")


def prepare_fastpass():
    print("prepare_fastpass")

