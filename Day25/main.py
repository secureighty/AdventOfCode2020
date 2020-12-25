import time

start_time = time.time()


def transform_for_7s():
    subject = 7
    num = 1
    sevens = [None, None]
    i = 0
    while None in sevens:
        i += 1
        num *= subject
        num %= 20201227
        if num == keys[0]:
            sevens[0] = i
        elif num == keys[1]:
            sevens[1] = i
    return sevens


def transform(subject, loop_size):
    num = 1
    for i in range(0, loop_size):
        num *= subject
        num %= 20201227
    return num


keys = []
size = 100000
for line in open("data"):
    keys.append(int(line.strip()))
print(keys)
sevens = transform_for_7s()

y = transform(keys[1], sevens[0])
x = transform(keys[0], sevens[1])
if y == x:
    print(x)
print("--- %s seconds ---" % (time.time() - start_time))