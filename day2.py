def get_list_from_file(filename):
    with open(filename, 'r') as file:
        formatted_input = [line.strip().split() for line in file]
    return formatted_input

# Part 1
def get_final_position_and_depth_without_aim(filename='inputs/day2_input.txt'):
    commands = get_list_from_file(filename)
    horiz_position, depth = 0, 0
    for command in commands:
        horiz_position, depth = change_position_without_aim(command, horiz_position, depth)
    return (horiz_position, depth, horiz_position * depth)
    
def change_position_without_aim(command, horiz_position, depth):
    direction, amount = command[0], int(command[1])
    if direction == 'forward':
        horiz_position += amount
    elif direction == 'down':
        depth += amount
    else:
        depth -= amount
    return (horiz_position, depth)

# Part 2
def get_final_position_and_depth_with_aim(filename='inputs/day2_input.txt'):
    commands = get_list_from_file(filename)
    horiz_position, depth, aim = 0, 0, 0
    for command in commands:
        horiz_position, depth, aim = change_position_with_aim(command, horiz_position, depth, aim)
    return (horiz_position, depth, horiz_position * depth)
    
def change_position_with_aim(command, horiz_position, depth, aim):
    direction, amount = command[0], int(command[1])
    if direction == 'forward':
        horiz_position += amount
        depth += (aim * amount)
    elif direction == 'down':
        aim += amount
    else:
        aim -= amount
    return (horiz_position, depth, aim)