def get_list_from_file(filename):
    with open(filename, 'r') as file:
        formatted_input = [int(line.strip()) for line in file]
    return formatted_input

def count_number_of_depth_increases(depths=[], get_from_file=False):
    if get_from_file:
        depths = get_list_from_file('inputs/day1_input.txt')
    num_increases = 0
    for i in range(len(depths) - 1):
        if depths[i + 1] > depths[i]:
            num_increases += 1
    return num_increases

def count_number_of_sliding_window_increases(depths=[], width=3, get_from_file=False):
    if get_from_file:
        depths = get_list_from_file('inputs/day1_input.txt')
    num_window_increases = 0
    for i in range(len(depths) - width):
        curr_sum, next_sum = 0, 0
        for j in range(width):
            curr_sum += depths[i + j]
            next_sum += depths[i + j + 1]
        if next_sum > curr_sum:
            num_window_increases += 1
    return num_window_increases
    