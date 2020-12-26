
data_array = []
for line in open("data"):
    data_array += [line.strip()]

def traverse(down, across):
    trees = 0
    x = 0
    y = 0

    while y < len(data_array):
        if x >= len(data_array[y]):
            x -= len(data_array[y])
        print(str(x), str(y), data_array[y][x])
        if data_array[y][x] == "#":
            trees += 1

        x += across
        y += down
    return trees
# part 1
# print(traverse(1, 3))
# part 2

ans = 1
for i in (1,1),(1,3),(1,5),(1,7),(2,1):
    ans *= traverse(i[0], i[1])
print(ans)