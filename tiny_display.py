import os
import time
import logging

import board
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import adafruit_ssd1306
from raspberry import buffer

WIDTH = 128
HEIGHT = 64
BORDER = 2
SOME_FONT_FILE = '/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf'

logger = logging.getLogger(__name__)
i2c = board.I2C()
time.sleep(0.1)


class TinyDisplay:
    def __init__(self):
        self.oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C)
        if os.path.isfile(SOME_FONT_FILE):
            self.use_interesting_font = True
        else:
            self.use_interesting_font = False

    def clear(self):
        self.oled.fill(0)
        self.oled.show()

    def draw_image(self):
        self.clear()

        # image = Image.open('dpt64.jpg')
        # image = Image.open('dpt128x64.jpg')
        target_image = Image.new('1', (self.oled.width, self.oled.height))
        image = Image.open('dpt64.jpg')
        converted_image = image.convert('1')
        target_image.paste(converted_image, (32, 0))
        draw = ImageDraw.Draw(target_image)

        self.oled.image(target_image)
        self.oled.show()

    def draw_box(self):
        self.clear()
        image = Image.new('1', (self.oled.width, self.oled.height))
        draw = ImageDraw.Draw(image)

        draw.rectangle((0, 0, self.oled.width, self.oled.height), outline=255, fill=255)
        '''
        draw.rectangle(
            (BORDER, BORDER, self.oled.width - BORDER - 1, self.oled.height - BORDER - 1),
            outline=0,
            fill=0,
        )
        '''

        self.oled.image(image)
        self.oled.show()

    def draw_four(self, x, y):
        self.clear()
        image = Image.new('1', (self.oled.width, self.oled.height))
        draw = ImageDraw.Draw(image)

        draw.point((x, y), fill=255)
        draw.point((x, y+1), fill=255)
        draw.point((x+1, y), fill=255)
        draw.point((x+1, y+1), fill=255)

        y += 2
        draw.point((x, y), fill=255)
        draw.point((x, y+1), fill=255)
        draw.point((x+1, y), fill=255)
        draw.point((x+1, y+1), fill=255)

        y += 2
        draw.point((x, y), fill=255)
        draw.point((x, y+1), fill=255)
        draw.point((x+1, y), fill=255)
        draw.point((x+1, y+1), fill=255)

        y -= 4
        x += 2
        draw.point((x, y), fill=255)
        draw.point((x, y+1), fill=255)
        draw.point((x+1, y), fill=255)
        draw.point((x+1, y+1), fill=255)

        x += 2
        draw.point((x, y), fill=255)
        draw.point((x, y+1), fill=255)
        draw.point((x+1, y), fill=255)
        draw.point((x+1, y+1), fill=255)
        self.oled.image(image)
        self.oled.show()

    def draw_point(self, x, y):
        self.clear()
        image = Image.new('1', (self.oled.width, self.oled.height))
        draw = ImageDraw.Draw(image)

        draw.point((x, y), fill=255)
        draw.point((x, y-1), fill=255)
        draw.point((x, y+1), fill=255)
        draw.point((x-1, y), fill=255)
        draw.point((x+1, y), fill=255)
        self.oled.image(image)
        self.oled.show()

    def show_text(self, text, size):
        self.clear()
        image = Image.new('1', (self.oled.width, self.oled.height))
        draw = ImageDraw.Draw(image)
        if self.use_interesting_font:
            font = ImageFont.truetype(
                font=SOME_FONT_FILE,
                size=size
            )
        else:
            font = ImageFont.load_default()

        (font_width, font_height) = font.getsize(text)

        x = self.oled.width // 2 - font_width // 2
        y = self.oled.height // 2 - font_height // 2
        # y = font_height // 2
        # y = 0
        draw.text(
            (x, y),
            text,
            font=font,
            fill=255,
        )

        self.oled.image(image)
        self.oled.show()
