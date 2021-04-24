import sys
import logging
import random
import time

import board
from PIL import Image
from PIL import ImageDraw
import adafruit_ssd1306

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
WIDTH = 128
HEIGHT = 64
BORDER = 2
SOME_FONT_FILE = '/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf'
MAX_GEN_COUNT = 1000
SEED = 5
GENERATION_TIME = 0.2
i2c = board.I2C()
time.sleep(0.1)


class Colony:
    def __init__(self, **kwargs):
        seed = kwargs.get('seed', None)
        pattern = kwargs.get('pattern', None)
        logger.debug(seed)
        logger.debug(pattern)

        self.colony = []
        self.row_count = 32
        self.column_count = 64
        if seed is not None:
            # self.generate_random(seed)
            # self.start_box()
            # self.start_blinker()
            # self.start_toad()
            # self.start_beacon()
            # self.start_glider()
            # self.start_penta_decathlon()
            # self.start_pulsar()
            self.start_gun()

        self.oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C)

    def generate_random(self, seed):
        for idx in range(0, self.row_count):
            current_row = []
            for jdx in range(0, self.column_count):
                coin = int(random.random() * 100) % seed
                if (coin == 0):
                    current_row.append(True)
                else:
                    current_row.append(False)
            self.colony.append(current_row)

    def start_box(self):
        self.blank()
        self.colony[1][1] = True
        self.colony[1][2] = True
        self.colony[2][1] = True
        self.colony[2][2] = True

    def start_blinker(self):
        self.blank()
        self.colony[1][1] = True
        self.colony[2][1] = True
        self.colony[3][1] = True

    def start_toad(self):
        self.blank()
        self.colony[3][6] = True
        self.colony[3][7] = True
        self.colony[3][8] = True
        self.colony[4][5] = True
        self.colony[4][6] = True
        self.colony[4][7] = True

    def start_beacon(self):
        self.blank()
        self.colony[1][1] = True
        self.colony[1][2] = True
        self.colony[2][1] = True
        self.colony[2][2] = True

        self.colony[3][3] = True
        self.colony[3][4] = True
        self.colony[4][3] = True
        self.colony[4][4] = True

    def start_glider(self):
        self.blank()
        self.colony[0][0] = True
        self.colony[1][1] = True
        self.colony[1][2] = True
        self.colony[2][0] = True
        self.colony[2][1] = True

    def start_penta_decathlon(self):
        self.blank()
        x = 34
        y = 12
        self.colony[y][x] = True
        self.colony[y+1][x] = True
        self.colony[y+2][x-1] = True
        self.colony[y+2][x+1] = True
        self.colony[y+3][x] = True
        self.colony[y+4][x] = True
        self.colony[y+5][x] = True
        self.colony[y+6][x] = True
        self.colony[y+7][x-1] = True
        self.colony[y+7][x+1] = True
        self.colony[y+8][x] = True
        self.colony[y+9][x] = True

    def start_pulsar(self):
        self.blank()
        x = 26
        y = 8
        self.colony[y+2][x+4] = True
        self.colony[y+2][x+5] = True
        self.colony[y+2][x+6] = True
        self.colony[y+2][x+10] = True
        self.colony[y+2][x+11] = True
        self.colony[y+2][x+12] = True

        self.colony[y+4][x+2] = True
        self.colony[y+4][x+7] = True
        self.colony[y+4][x+9] = True
        self.colony[y+4][x+14] = True

        self.colony[y+5][x+2] = True
        self.colony[y+5][x+7] = True
        self.colony[y+5][x+9] = True
        self.colony[y+5][x+14] = True

        self.colony[y+6][x+2] = True
        self.colony[y+6][x+7] = True
        self.colony[y+6][x+9] = True
        self.colony[y+6][x+14] = True

        self.colony[y+7][x+4] = True
        self.colony[y+7][x+5] = True
        self.colony[y+7][x+6] = True
        self.colony[y+7][x+10] = True
        self.colony[y+7][x+11] = True
        self.colony[y+7][x+12] = True

        self.colony[y+9][x+4] = True
        self.colony[y+9][x+5] = True
        self.colony[y+9][x+6] = True
        self.colony[y+9][x+10] = True
        self.colony[y+9][x+11] = True
        self.colony[y+9][x+12] = True

        self.colony[y+10][x+2] = True
        self.colony[y+10][x+7] = True
        self.colony[y+10][x+9] = True
        self.colony[y+10][x+14] = True

        self.colony[y+11][x+2] = True
        self.colony[y+11][x+7] = True
        self.colony[y+11][x+9] = True
        self.colony[y+11][x+14] = True

        self.colony[y+12][x+2] = True
        self.colony[y+12][x+7] = True
        self.colony[y+12][x+9] = True
        self.colony[y+12][x+14] = True

        self.colony[y+14][x+4] = True
        self.colony[y+14][x+5] = True
        self.colony[y+14][x+6] = True
        self.colony[y+14][x+10] = True
        self.colony[y+14][x+11] = True
        self.colony[y+14][x+12] = True

    def start_gun(self):
        self.blank()
        self.colony[2][26] = True

        self.colony[3][24] = True
        self.colony[3][26] = True

        self.colony[4][14] = True
        self.colony[4][15] = True
        self.colony[4][22] = True
        self.colony[4][23] = True
        self.colony[4][36] = True
        self.colony[4][37] = True

        self.colony[5][13] = True
        self.colony[5][17] = True
        self.colony[5][22] = True
        self.colony[5][23] = True
        self.colony[5][36] = True
        self.colony[5][37] = True

        self.colony[6][2] = True
        self.colony[6][3] = True
        self.colony[6][12] = True
        self.colony[6][18] = True
        self.colony[6][22] = True
        self.colony[6][23] = True

        self.colony[7][2] = True
        self.colony[7][3] = True
        self.colony[7][12] = True
        self.colony[7][16] = True
        self.colony[7][18] = True
        self.colony[7][19] = True
        self.colony[7][24] = True
        self.colony[7][26] = True

        self.colony[8][12] = True
        self.colony[8][18] = True
        self.colony[8][26] = True

        self.colony[9][13] = True
        self.colony[9][17] = True

        self.colony[10][14] = True
        self.colony[10][15] = True

    def blank(self):
        for _ in range(0, self.row_count):
            current_row = []
            for _ in range(0, self.column_count):
                current_row.append(False)
            self.colony.append(current_row)

    def clear(self):
        self.oled.fill(0)
        self.oled.show()

    def display_colony(self):
        # self.clear()
        image = Image.new('1', (self.oled.width, self.oled.height))
        draw = ImageDraw.Draw(image)

        row_num = 0  # TODO: is the 0 right or the old 1?
        for row in self.colony:
            y = 2 * row_num
            for idx in range(0, self.column_count):
                if (row[idx]):
                    x = 2 * idx
                    draw.point((x, y), fill=255)
                    draw.point((x, y+1), fill=255)
                    draw.point((x+1, y), fill=255)
                    draw.point((x+1, y+1), fill=255)
            if (row_num < self.row_count):
                row_num = row_num + 1

        self.clear()
        self.oled.image(image)
        self.oled.show()

    def create_next_gen(self):
        next_colony = []

        for idx in range(0, self.row_count):
            current_row = []
            for jdx in range(0, self.column_count):
                current_row.append(False)
            next_colony.append(current_row)

        for y in range(0, self.row_count):
            for x in range(0, self.column_count):
                neighbor_count = 0
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
                            neighbor_count = neighbor_count + 1
                if (self.colony[y][x]):
                    if (neighbor_count == 0 or neighbor_count == 1):
                        next_colony[y][x] = False
                    elif (neighbor_count == 2 or neighbor_count == 3):
                        next_colony[y][x] = True
                    else:
                        next_colony[y][x] = False
                else:
                    if (neighbor_count == 3):
                        next_colony[y][x] = True
                    else:
                        next_colony[y][x] = False

        self.colony = next_colony

    def draw_image(self):
        self.clear()

        target_image = Image.new('1', (self.oled.width, self.oled.height))
        image = Image.open('me.jpg')
        converted_image = image.convert('1')
        target_image.paste(converted_image, (32, 0))
        self.oled.image(target_image)
        self.oled.show()


def main():
    try:
        seed = int(sys.argv[1])
    except Exception as wtf:
        logger.info(wtf)
        seed = SEED
    colony = Colony(seed=seed)

    generation = 0
    while (generation < MAX_GEN_COUNT):
        colony.display_colony()
        colony.create_next_gen()
        generation += 1
        logger.info('generation: %s', generation)
        time.sleep(GENERATION_TIME)

    time.sleep(5)
    colony.draw_image()


if (__name__ == "__main__"):
    logging.basicConfig(
        level=logging.INFO,
        stream=sys.stdout,
        format='[%(levelname)s] %(asctime)s (%(module)s) %(message)s',
        datefmt='%Y/%m/%d-%H:%M:%S'
    )

    main()
