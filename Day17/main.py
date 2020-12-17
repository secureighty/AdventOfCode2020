from Day17.Grid import Grid

data = ""
for line in open("data"):
    data += line

print(data)

testgrid = Grid(data, 3)

print(testgrid.get_cube([0, 3, 0]))
changedcube = testgrid.get_cube([-3, -8, 0])
changedcube.toggle()
print(changedcube)


testgrid.print_slice(0, 1, [0, 0, 0])