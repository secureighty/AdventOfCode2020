from Day17.Grid import Grid
import time
start_time = time.time()

data = ""
for line in open("data"):
    data += line

final_grid = Grid(data, 4)
#Grid(data, 3)

for i in range(0, 6):
    final_grid.cycle()
print(final_grid.get_active_cube_count())
print("--- %s seconds ---" % (time.time() - start_time))
