

def check(line, pol):

    print("----------------------------")
    first_num = int(line[0:line.index("-")])
    print(first_num)
    second_num = int(line[line.index("-")+1:line.index(" ")])
    print(second_num)
    checked_char = line[line.index(":")-1]
    print(checked_char)
    pw = line[line.index(":")+2:]
    print(pw)
    num = 0
    if pol == 1:
        for i in pw:
            if i == checked_char:
                num += 1
        if first_num <= num <= second_num:
            return True
        else:
            return False
    elif pol == 2:
        num = 0
        for i in first_num, second_num:
            print("does "+pw[i-1]+" equal "+checked_char)
            if pw[i-1] == checked_char:
                print("matches")
                num += 1
        if num == 1:
            print("valid")
            return True
        else:
            print("invalid")
            return False


valid_pws = 0
for line in open("data"):
    if check(line, 2):
    # if check(line, 1):
        valid_pws += 1
print(valid_pws)