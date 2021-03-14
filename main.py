import sys
import random
import time

generationCount=10000

rowCount = 32
columnCount = 64
generation = 0
colony = []
seed=2

def main():
    global rowCount
    global columnCount
    global generation

    initializeColony()

    while (generation < generationCount):
        displayColony()
        createNextGeneration()
        generation = generation + 1
        time.sleep(0.3)

def initializeColony():
    global rowCount
    global columnCount
    global colony

    #if (len(sys.argv) != 4):
    #    print("usage: life.py <row> <columnCount> <seed>")
    #    sys.exit(1)
    #
    #try:
    #    rowCount=int(sys.argv[1])
    #    columnCount=int(sys.argv[2])
    #    seed=int(sys.argv[3])
    #except:
    #    for m in sys.exc_info(): print(m)
    #    sys.exit(1)

    for idx in range(0, rowCount):
        currentRow = []
        for jdx in range(0, columnCount):
            coin = int(random.random() * 100) % seed
            if (coin == 0):
                currentRow.append(True)
            else:
                currentRow.append(False);
        colony.append(currentRow)

def displayColony():
    rowNum = 1;
    for row in colony:
        for idx in range(0, columnCount):
            if (row[idx]):
                sys.stdout.write("#")
            else:
                sys.stdout.write(" ")
        if (rowNum < rowCount):
            rowNum = rowNum + 1
            sys.stdout.write("\n")

def createNextGeneration():
    global rowCount
    global columnCount
    global colony
    nextColony = []

    for idx in range(0, rowCount):
        currentRow = []
        for jdx in range(0, columnCount):
            currentRow.append(False)
        nextColony.append(currentRow)

    for y in range(0, rowCount):
        for x in range(0, columnCount):
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
                if (nx >= 0 and nx < columnCount and ny >= 0 and ny < rowCount):
                    if (colony[ny][nx]):
                        populatedNeighborCount = populatedNeighborCount + 1
            if (colony[y][x]):
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

    colony = nextColony

if (__name__ == "__main__"):
    main()
