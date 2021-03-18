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
GENERATION_TIME = 0.5
i2c = board.I2C()
time.sleep(0.1)


class Colony:
    def __init__(self, **kwargs):
        seed = kwargs.get('seed', None)
        pattern = kwargs.get('pattern', None)

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
            self.start_pulsar()

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
        self.colony[4][5] = True
        self.colony[5][5] = True
        self.colony[6][4] = True
        self.colony[6][6] = True
        self.colony[7][5] = True
        self.colony[8][5] = True
        self.colony[9][5] = True
        self.colony[10][5] = True
        self.colony[11][4] = True
        self.colony[11][6] = True
        self.colony[12][5] = True
        self.colony[13][5] = True

    def start_pulsar(self):
        self.blank()
        self.colony[2][4] = True
        self.colony[2][5] = True
        self.colony[2][6] = True
        self.colony[2][10] = True
        self.colony[2][11] = True
        self.colony[2][12] = True

        self.colony[4][2] = True
        self.colony[4][7] = True
        self.colony[4][9] = True
        self.colony[4][14] = True

        self.colony[5][2] = True
        self.colony[5][7] = True
        self.colony[5][9] = True
        self.colony[5][14] = True

        self.colony[6][2] = True
        self.colony[6][7] = True
        self.colony[6][9] = True
        self.colony[6][14] = True

        self.colony[7][4] = True
        self.colony[7][5] = True
        self.colony[7][6] = True
        self.colony[7][10] = True
        self.colony[7][11] = True
        self.colony[7][12] = True

        self.colony[9][4] = True
        self.colony[9][5] = True
        self.colony[9][6] = True
        self.colony[9][10] = True
        self.colony[9][11] = True
        self.colony[9][12] = True

        self.colony[10][2] = True
        self.colony[10][7] = True
        self.colony[10][9] = True
        self.colony[10][14] = True

        self.colony[11][2] = True
        self.colony[11][7] = True
        self.colony[11][9] = True
        self.colony[11][14] = True

        self.colony[12][2] = True
        self.colony[12][7] = True
        self.colony[12][9] = True
        self.colony[12][14] = True

        self.colony[14][4] = True
        self.colony[14][5] = True
        self.colony[14][6] = True
        self.colony[14][10] = True
        self.colony[14][11] = True
        self.colony[14][12] = True

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
        self.clear()
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
