import os

directions_x = {'forward': 1}
directions_y = {'down': 1, 'up': -1}

def part1(input_array):
    pos_x = 0
    pos_y = 0

    for step in input_array:
        step_key = next(iter(step))
        step_value = step[step_key]

        if step_key in directions_x:
            step_x = int(step_value) * directions_x[step_key]
            pos_x += step_x
        elif step_key in directions_y:
            step_y = int(step_value) * directions_y[step_key]
            pos_y += step_y

    return pos_x * pos_y
    

def part2(input_array):
    pos_x = 0
    pos_y = 0
    aim = 0

    for step in input_array:
        step_key = next(iter(step))
        step_value = step[step_key]

        if step_key in directions_x:
            step_x = int(step_value) * directions_x[step_key]
            pos_x += step_x
            pos_y += step_x * aim
        elif step_key in directions_y:
            step_y = int(step_value) * directions_y[step_key]
            aim += step_y

    return pos_x * pos_y


if __name__ == "__main__":
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'input.txt')
    input_array = []
    
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            split = line.strip('\n').split(' ');
            input_array.append({split[0]: split[1]})

    print(part1(input_array))
    print(part2(input_array))