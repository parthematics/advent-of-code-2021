from collections import Counter

def get_list_from_file(filename):
    with open(filename, 'r') as file:
        formatted_input = [list(line.strip()) for line in file]
    return formatted_input

# Part 1
def get_power_consumption(filename='inputs/day3_input.txt'):
    binary_numbers = get_list_from_file(filename)
    gamma, epsilon = '', ''
    for index in range(len(binary_numbers[0])):
        most_common = get_common_bit(binary_numbers, index, most_common=True)
        if most_common == '0':
            gamma, epsilon = gamma + '0', epsilon + '1'
        else:
            gamma, epsilon = gamma + '1', epsilon + '0'
    gamma, epsilon = int(gamma, 2), int(epsilon, 2)
    return gamma * epsilon
            
# Part 2
def get_life_support_rating(filename='inputs/day3_input.txt'):
    report_numbers = get_list_from_file(filename)
    oxygen_generator_rating = int(propagate_deletions(report_numbers.copy(), most_common=True), 2)
    co2_scrubber_rating = int(propagate_deletions(report_numbers.copy(), most_common=False), 2)
    return (oxygen_generator_rating * co2_scrubber_rating)

def propagate_deletions(binary_numbers, most_common=True):
    for index in range(len(binary_numbers[0])):
        if len(binary_numbers) == 1:
            break
        delete_indices = []
        curr_common_bit = get_common_bit(binary_numbers, index, most_common)
        for i in range(len(binary_numbers)):
            if binary_numbers[i][index] != curr_common_bit:
                delete_indices.append(i)
        for delete_index in sorted(delete_indices, reverse=True):
            del binary_numbers[delete_index]
    return ''.join(binary_numbers[0])
            
def get_common_bit(binary_numbers, index, most_common=True):
    columns = list(zip(*binary_numbers))
    frequencies = Counter(columns[index])
    if most_common:
        if frequencies['0'] > frequencies['1']:
            return '0'
        else:
            return '1'
    else:
        if frequencies['0'] > frequencies['1']:
            return '1'
        else:
            return '0'
