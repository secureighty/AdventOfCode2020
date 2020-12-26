datastring = ""
for line in open("data"):
    datastring += line

def part1():
    sum = 0
    for grouping in datastring.split("\n"):
        print(grouping)
        grouping.strip()
        chars = []
        for char in grouping:
            if char not in chars and char != "\n":
                chars.append(char)
        sum += len(chars)

    print(sum)

part1()