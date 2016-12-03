NUMBER_MATRIX = {(0,0):1, (1,0):2, (2,0):3,
        (0,1): 4, (1,1): 5, (2,1): 6,
        (0,2): 7, (1,2): 8, (2,2): 9}
CURRENT_NUMBER = (1,1)

def next_number(direction):
    global CURRENT_NUMBER
    global NUMBER_MATRIX
    if direction == "U":
        number_to_switch_to = (CURRENT_NUMBER[0], CURRENT_NUMBER[1] -1)
        if number_to_switch_to in NUMBER_MATRIX.keys():
            CURRENT_NUMBER = number_to_switch_to
    if direction == "D":
        number_to_switch_to = (CURRENT_NUMBER[0], CURRENT_NUMBER[1] +1)
        if number_to_switch_to in NUMBER_MATRIX.keys():
            CURRENT_NUMBER = number_to_switch_to
    if direction == "L":
        number_to_switch_to = (CURRENT_NUMBER[0] - 1, CURRENT_NUMBER[1])
        if number_to_switch_to in NUMBER_MATRIX.keys():
            CURRENT_NUMBER = number_to_switch_to
    if direction == "R":
        number_to_switch_to = (CURRENT_NUMBER[0] + 1, CURRENT_NUMBER[1])
        if number_to_switch_to in NUMBER_MATRIX.keys():
            CURRENT_NUMBER = number_to_switch_to

if __name__ == "__main__":
    f = open('two/input', 'r')
    CURRENT_NUMBER = (1,1)
    rows = f.readlines()
    code = ""
    for row in rows:
        for instruction in row:
            next_number(instruction)
        code += str(NUMBER_MATRIX[CURRENT_NUMBER])
    print(code)
