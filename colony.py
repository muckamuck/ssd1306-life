import os
import logging
import sys
import random
import time

import board
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import adafruit_ssd1306

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
WIDTH = 128
HEIGHT = 64
BORDER = 2
SOME_FONT_FILE = '/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf'
MAX_GEN_COUNT = 10000
SEED = 2
i2c = board.I2C()
time.sleep(0.1)


class Colony:
    def __init__(self):
        self.colony = []
        self.row_count = 32
        self.column_count = 64
        for idx in range(0, self.row_count):
            currentRow = []
            for jdx in range(0, self.column_count):
                coin = int(random.random() * 100) % SEED
                if (coin == 0):
                    currentRow.append(True)
                else:
                    currentRow.append(False)
            self.colony.append(currentRow)

        self.oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C)
        if os.path.isfile(SOME_FONT_FILE):
            self.use_interesting_font = True
        else:
            self.use_interesting_font = False

    def clear(self):
        self.oled.fill(0)
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

    def displayColony(self):
        rowNum = 1
        rowNum = 0  # TODO: is the 0 right or the old 1?
        for row in self.colony:
            for idx in range(0, self.column_count):
                if (row[idx]):
                    sys.stdout.write("#")
                else:
                    sys.stdout.write(" ")
            if (rowNum < self.row_count):
                rowNum = rowNum + 1
                sys.stdout.write("\n")

    def createNextGeneration(self):
        nextColony = []

        for idx in range(0, self.row_count):
            currentRow = []
            for jdx in range(0, self.column_count):
                currentRow.append(False)
            nextColony.append(currentRow)

        for y in range(0, self.row_count):
            for x in range(0, self.column_count):
                populatedNeighborCount = 0
                neighbors = []
                neighbors.append((x-1, y-1))
                neighbors.append((x, y-1))
                neighbors.append((x+1, y-1))
                neighbors.append((x-1, y))
                neighbors.append((x+1, y))
                neighbors.append((x-1, y+1))
                neighbors.append((x, y+1))
                neighbors.append((x+1, y+1))
                for point in neighbors:
                    (nx, ny) = point
                    if (nx >= 0 and nx < self.column_count and ny >= 0 and ny < self.row_count):
                        if (self.colony[ny][nx]):
                            populatedNeighborCount = populatedNeighborCount + 1
                if (self.colony[y][x]):
                    if (populatedNeighborCount == 0 or populatedNeighborCount == 1):
                        nextColony[y][x] = False
                    elif (populatedNeighborCount == 2 or populatedNeighborCount == 3):
                        nextColony[y][x] = True
                    else:
                        nextColony[y][x] = False
                else:
                    if (populatedNeighborCount == 3):
                        nextColony[y][x] = True
                    else:
                        nextColony[y][x] = False

        self.colony = nextColony


def main():
    colony = Colony()
    colony.draw_four(10, 10)

    generation = 0
    while (generation < MAX_GEN_COUNT):
        colony.displayColony()
        colony.createNextGeneration()
        generation = generation + 1
        time.sleep(0.9)


if (__name__ == "__main__"):
    main()
