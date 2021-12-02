import os
import sys

def part1(input_array):
    i = 0
    cnt = 0
    while i < len(input_array) - 1:
        if input_array[i] < input_array[i + 1]:
            cnt += 1
        i += 1

    return cnt
    

def part2(input_array):
    i = 0
    cnt = 0
    prev_sum = sys.maxsize
    while i < len(input_array) - 2:
        sum = input_array[i] + input_array[i + 1] + input_array[i + 2]
        if (sum > prev_sum):
            cnt += 1
        prev_sum = sum
        i += 1


    return cnt


if __name__ == "__main__":
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'input.txt')
    input_array = []
    with open(filename) as f:
        input_array = [int(x) for x in f]

    print(part1(input_array))
    print(part2(input_array))