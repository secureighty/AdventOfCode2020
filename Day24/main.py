import math
from Day24.HexGrid import HexGrid
from Day24.Tile import Tile


grid = HexGrid()
for line in open("data"):
    dimension_info = [0.0, 0.0]
    while line != "":
        next_instruction = line[0]
        line = line[1:]
        if next_instruction == "n" or next_instruction == "s":
            next_instruction += line[0]
            line = line[1:]

        # move logic #
        if next_instruction == "e":
            dimension_info[1] += 100.0
        if next_instruction == "ne":
            dimension_info[0] = round(dimension_info[0] + (100 * math.sqrt(3)), 1)
            dimension_info[1] += 50.0
        if next_instruction == "se":
            dimension_info[0] = round(dimension_info[0] - (100 * math.sqrt(3)), 1)
            dimension_info[1] += 50.0

        if next_instruction == "w":
            dimension_info[1] -= 100.0
        if next_instruction == "nw":
            dimension_info[0] = round(dimension_info[0] + (100 * math.sqrt(3)), 1)
            dimension_info[1] -= 50.0
        if next_instruction == "sw":
            dimension_info[0] = round(dimension_info[0] - (100 * math.sqrt(3)), 1)
            dimension_info[1] -= 50.0
        # ---------- #

    if dimension_info[0] == 0:
        dimension_info[0] = 0.0
    if dimension_info[1] == 0:
        dimension_info[1] = 0.0

    grid.get_tile(dimension_info).toggle()


print(grid.get_active_tiles())

# ---------- #
# for i in grid.loaded_tiles.values():
#     print(i)
for i in range(0, 100):
    grid.cycle()
    print(grid.get_active_tiles())
