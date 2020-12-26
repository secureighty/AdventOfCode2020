
cup_circle = []
for line in open("data"):
    for char in line:
        cup_circle.append(int(char))
cup_circle_length = len(cup_circle)
current_cup = cup_circle[0]
dest_cup = None
held_cups = []


def cycle():
    print(cup_circle)
    print("curr: "+str(current_cup))
    pick_up_cups()
    print(held_cups)
    pick_destination_cup()
    print("dest: "+str(dest_cup))
    put_down_cups()
    pick_new_current_cup()


def pick_up_cups():
    for i in range(0, 3):
        if cup_circle.index(current_cup) == len(cup_circle)-1:
            target_cup = cup_circle[0]
        else:
            target_cup = cup_circle[cup_circle.index(current_cup)+1]
        held_cups.append(target_cup)
        cup_circle.remove(target_cup)


def pick_destination_cup():
    global dest_cup
    new_cup = current_cup-1
    while True:
        if new_cup < 0:
            new_cup = cup_circle_length
        if new_cup in cup_circle:
            dest_cup = new_cup
            return True
        else:
            new_cup -= 1


def put_down_cups():
    global cup_circle
    global held_cups
    held_cups.reverse()
    for i in range(0, 3):
        cup_circle.insert(cup_circle.index(dest_cup)+1, held_cups[i])
    held_cups = []


def pick_new_current_cup():
    global current_cup
    new_cup_index = cup_circle.index(current_cup)+1
    if new_cup_index > cup_circle_length-1:
        new_cup_index = 0
    current_cup = cup_circle[new_cup_index]

for i in range (0, 100):
    print("--- move "+str(i+1)+" ---")
    cycle()
print("final: " + str(cup_circle))