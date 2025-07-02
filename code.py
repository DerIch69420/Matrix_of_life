import board
import displayio
from adafruit_matrixportal.matrix import Matrix

from random import randint, choice
from time import sleep

# Setup matrix display
WIDTH: int = 32
HEIGHT: int = 32

matrix = Matrix(width=WIDTH, height=HEIGHT)
display = matrix.display
display.brightness = 0.3 # not working

# Create main group
main_group = displayio.Group()
display.root_group = main_group

# Bitmap: 32x32 pixels, 2 colors
bitmap = displayio.Bitmap(WIDTH, HEIGHT, 2)

# Color palette
palette = displayio.Palette(2)
palette[0] = 0x000000  # dead
palette[1] = 0x000040  # alive

# Create tile grid and show it
tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)
main_group.append(tile_grid)

from src.game import Game, Cell
game = Game(WIDTH, HEIGHT)

game.grid = [
    [Cell(choice([True, False])) for _ in range(WIDTH)]
    for _ in range(HEIGHT)
]

while True:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            bitmap[x, y] = 1 if game.grid[y][x].state else 0
                
    game.update()
    sleep(0.01)
