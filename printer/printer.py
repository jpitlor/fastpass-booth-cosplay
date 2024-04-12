from printer.ivy2 import Ivy2Printer
from printer.image import prepare_image
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, timedelta

PRINTER_MAC = "60:6E:41:46:34:60"


def init():
    global printer
    printer = Ivy2Printer()
    printer.connect(PRINTER_MAC)


def print_new_fastpass():
    prepare_fastpass()
    printer.print("./printer/fastpass_edited.jpg")


def prepare_fastpass():
    now = datetime.now()
    return_time_start = now + timedelta(hours=3)
    return_time_end = now + timedelta(hours=3, minutes=30)
    image = Image.open('./printer/fastpass.png')
    drawn_image = ImageDraw.Draw(image)
    cascadia = ImageFont.truetype('./printer/CascadiaCode.ttf', 65)
    drawn_image.text((100, 350), return_time_start.strftime("%I:%M:%S %p"), font=cascadia, fill=(0, 0, 0), font_size=40)
    drawn_image.text((100, 475), return_time_end.strftime("%I:%M:%S %p"), font=cascadia, fill=(0, 0, 0), font_size=40)
    drawn_image.text((300, 705), return_time_end.strftime("%I:%M:%S %p"), font=cascadia, fill=(0, 0, 0), font_size=12)
    image.save("./printer/fastpass_edited.png")

    image_data = prepare_image("./printer/fastpass_edited.png", 100, True)
    with open("./printer/fastpass_edited.jpg", "wb") as file:
        file.write(image_data)

