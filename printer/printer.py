from printer.ivy2 import Ivy2Printer
from printer.image import prepare_image
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, timedelta
from dateutil import tz

PRINTER_MAC = "60:6E:41:46:34:60"
CALIFORNIA_TZ = tz.gettz("America/Los_Angeles")
BLACK = (0, 0, 0)

def init():
    global printer
    printer = Ivy2Printer()
    printer.connect(PRINTER_MAC)


def print_new_fastpass():
    printer.print("./printer/fastpass_edited.jpg")


def prepare_fastpass():
    now = datetime.now(tz=CALIFORNIA_TZ)
    return_time_start = now + timedelta(hours=2)
    return_time_end = now + timedelta(hours=2, minutes=30)
    new_pass_time = now + timedelta(hours=4)
    image = Image.open('./printer/fastpass.png')
    drawn_image = ImageDraw.Draw(image)
    cascadia_large = ImageFont.truetype('./printer/CascadiaCode.ttf', 65)
    cascadia_small = ImageFont.truetype('./printer/CascadiaCode.ttf', 18)
    drawn_image.text((295, 702), new_pass_time.strftime("%I:%M:%S %p"), font=cascadia_small, fill=BLACK)
    drawn_image.text((100, 350), return_time_start.strftime("%I:%M:%S %p"), font=cascadia_large, fill=BLACK)
    drawn_image.text((100, 475), return_time_end.strftime("%I:%M:%S %p"), font=cascadia_large, fill=BLACK)
    image.save("./printer/fastpass_edited.png")

    image_data = prepare_image("./printer/fastpass_edited.png", 100, True)
    with open("./printer/fastpass_edited.jpg", "wb") as file:
        file.write(image_data)

