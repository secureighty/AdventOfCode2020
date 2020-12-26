datastring = ""
for line in open("data"):
    datastring += line

def part1():
    sum = 0
    groups = datastring.split("\n\n")
    for group in groups:
        forms = group.split("\n")
        distinct_chars = []
        for form in forms:
            for char in form:
                if char not in distinct_chars:
                    distinct_chars.append(char)
        sum += len(distinct_chars)
    print(sum)

def part2():
    sum = 0
    groups = datastring.split("\n\n")
    for group in groups:
        # build up a list of distinct characters in a group
        forms = group.split("\n")
        distinct_chars = []
        for form in forms:
            for char in form:
                if char not in distinct_chars and char:
                    distinct_chars.append(char)
        shared_chars = []
        # check which of the distinct characters are shared by all forms in the group
        for char_to_check in distinct_chars:
            flag = True
            for form in forms:
                if form:
                    if char_to_check not in form:
                        flag = False
            if flag:
                shared_chars.append(char_to_check)
        sum += len(shared_chars)
    print(sum)


part1()
part2()