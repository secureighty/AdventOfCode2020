from Day17.Grid import Grid
import Day17.Cube

data = ""
for line in open("data"):
    data += line

print(data)

testgrid = Grid(data, 4)

testgrid.print_slice(0, 1, [0, 0, 0, 0])
for i in range(0, 6):
    testgrid.cycle()
    testgrid.print_slice(0, 1, [0, 0, 0, 0])

    print(testgrid.get_active_cube_count())


print(testgrid.get_active_cube_count())
# print(testgrid.get_cube([1,0,0]))
# for i in range(0, 1):
#     testgrid.cycle()
