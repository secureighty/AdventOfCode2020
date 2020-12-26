'''
Aedan (AT) Taylor
Advent of Code Day 1
find the 2/3 numbers from a large list that sum to 2020
return their product
'''

datafilename = "data"

#data import
data_array = []
for line in open(datafilename, "r"):
    data_array.append(int(line.strip()))
data_array.sort()


def find_two_target_summands(data_array, targetsum):
    '''
    :param data_array: all numbers
    :param targetsum: the desired sum.
    :return: an array containing the first found solution, or None if one is not found
    '''
    first_index = 0
    last_index = len(data_array)-1

    while(first_index != last_index):
        first = data_array[first_index]
        last = data_array[last_index]
        sum = first+last

        if sum > targetsum:
            last_index -= 1
        elif sum < targetsum:
            first_index += 1
        else:
            return [first, last]
    return None


def find_target_summands(data_array, targetsum, numofsummands):
    '''
    a recursive function to find target summands
    :param data_array: all the numbers
    :param targetsum: the desired sum
    :param numofsummands: how many summands must sum to the desired sum
    :return: an array containing the first found solution, or None if one is not found
    '''
    #bounds
    if data_array is not None:
        # base cases
        if numofsummands == 1:
            if targetsum in data_array:
                return targetsum
            else:
                return None

        elif numofsummands == 2:
            return find_two_target_summands(data_array, targetsum)

        elif numofsummands > 2:
            for i in data_array:

                data_array.remove(i)
                summands = find_target_summands(data_array, targetsum-i, numofsummands-1)
                data_array.append(i)

                if summands is not None:
                    return summands + [i]

    return None






def main():
    #summands = find_target_summands(data_array, 2020, 2)
    summands = find_target_summands(data_array, 2020, 3)
    if summands is not None:
        print(summands)
        quotient = 1
        for i in summands:
            quotient *= i
        print(quotient)
    else:
        print("answer not found")

main()
