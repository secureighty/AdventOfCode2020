datastring = ""
for line in open("data"):
    datastring += line

passport_list = datastring.split("\n\n")
for i in range(0, len(passport_list)):
    passport_list[i] = passport_list[i].replace("\n", " ")

valids = 0
for passport in passport_list:
    num_of_fields = 0
    for field in passport.split(" "):
        if field:
            x = field[0:3]
            y = field[4:]
            if x == "byr":
                if 1920 <= int(y) <= 2002:
                    print(x + " is valid")
                    num_of_fields += 1
            elif x == "iyr":
                if 2010 <= int(y) <= 2020:
                    print(x + " is valid")
                    num_of_fields += 1
            elif x == "eyr":
                if 2020 <= int(y) <= 2030:
                    print(x + " is valid")
                    num_of_fields += 1
            elif x == "hgt":
                metric = y[len(y) - 2:]
                try:
                    num = int(y[:len(y) - 2])
                except:
                    num = -1
                if metric == "cm":
                    if 150 <= num <= 193:
                        print(x + " is valid")
                        num_of_fields += 1
                elif metric == "in":
                    if 59 <= num <= 76:
                        print(x + " is valid")
                        num_of_fields += 1
            elif x == "hcl":
                flag = False
                if y[0] == "#" and len(y) == 7:
                    flag = True
                    for char in y[1:]:
                        if char not in "1234567890abcdef":
                            flag = False
                if flag:
                    print(x + " is valid")
                    num_of_fields += 1
            elif x == "ecl":
                if y in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
                    print(x + " is valid")
                    num_of_fields += 1
            elif x == "pid":
                flag = False
                if len(y) == 9:
                    flag = True
                    for num in y:
                        if num not in "0987654321":
                            flag = False
                if flag:
                    print(x + " is valid")
                    num_of_fields += 1
    print("---")
    if num_of_fields == 7:
        valids += 1

print(passport_list)
print(valids)
