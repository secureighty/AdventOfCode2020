instructions = []

for line in open("data"):
    instructions.append([0, line[0], int(line[4:len(line)-1])])
print(instructions)

def run(instructions):
    index = 0
    accumulator = 0
    flag = True
    while flag:
        try:
            current_instruction = instructions[index]
        except IndexError:
            for instruction in instructions:
                instruction[0] = 0
            return "program exits cleanly with acc: "+str(accumulator)
        current_instruction[0] += 1
        if current_instruction[0] > 1:
            flag = False
        elif current_instruction[1] == "n":
            index += 1
        elif current_instruction[1] == "a":
            accumulator += current_instruction[2]
            index += 1
        elif current_instruction[1] == "j":
            index += current_instruction[2]
        else:
            print("faulty input")
    for instruction in instructions:
        instruction[0] = 0
    return accumulator

print(run(instructions))


for instruction in instructions:
    if instruction[1] == "j":
        instruction[1] = "n"

    elif instruction[1] == "n":
        instruction[1] = "j"
    try:
        int(run(instructions))
    except:
        print(run(instructions))

    if instruction[1] == "j":
        instruction[1] = "n"

    elif instruction[1] == "n":
        instruction[1] = "j"