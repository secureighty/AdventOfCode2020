'''
Aedan (AT) Taylor
Advent of Code Day 1 Problem 1
find the 2 numbers from a large list that sum to 2020
return their product
'''

datafilename = "data"


def find_target_summands(datafilename, targetsum):
    '''
    :param datafilename: name of file with data
    :param targetsum: the desired sum.
    :return: a tuple containing the first found solution, or None if one is not found
    '''

    data_array = []
    for line in open(datafilename, "r"):
        data_array.append(int(line.strip()))
    data_array.sort()
    first_index = 0
    last_index = len(data_array)-1

    while(first_index != last_index):
        first = data_array[first_index]
        last = data_array[last_index]
        sum = first+last

        if sum > 2020:
            last_index -= 1
        elif sum < 2020:
            first_index += 1
        else:
            return first, last
    return None


def main():
    summands = find_target_summands(datafilename, 2020)
    print(summands)
    quotient = 1
    for i in summands:
        quotient *= i
    print(quotient)

main()
