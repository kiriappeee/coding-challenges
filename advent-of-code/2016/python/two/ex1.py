
def next_number(direction, current_number, number_matrix):
    if direction == "U":
        number_to_switch_to = (current_number[0], current_number[1] -1)
        if number_to_switch_to in number_matrix.keys():
            current_number = number_to_switch_to
    if direction == "D":
        number_to_switch_to = (current_number[0], current_number[1] +1)
        if number_to_switch_to in number_matrix.keys():
            current_number = number_to_switch_to
    if direction == "L":
        number_to_switch_to = (current_number[0] - 1, current_number[1])
        if number_to_switch_to in number_matrix.keys():
            current_number = number_to_switch_to
    if direction == "R":
        number_to_switch_to = (current_number[0] + 1, current_number[1])
        if number_to_switch_to in number_matrix.keys():
            current_number = number_to_switch_to
    return current_number

if __name__ == "__main__":
    number_matrix = {(0,0):'1', (1,0):'2', (2,0):'3',
            (0,1): '4', (1,1): '5', (2,1): '6',
            (0,2): '7', (1,2): '8', (2,2): '9'}
    current_number = (1,1)
    f = open('two/input', 'r')
    rows = f.readlines()
    code = ""
    for row in rows:
        for instruction in row:
            current_number = next_number(instruction, current_number, number_matrix)
        code += str(number_matrix[current_number])
    print(code)
