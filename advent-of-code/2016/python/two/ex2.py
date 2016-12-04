from . import ex1
NUMBER_MATRIX = {(0,2):'1',
        (1,1): '2', (1,2): '3', (1,3): '4',
        (2,0): '5', (2,1): '6', (2,2): '7', (2,3): '8', (2,4): '9',
        (3,1): 'A', (3,2): 'B', (3,3): 'C',
        (4,2): 'D'}
CURRENT_NUMBER = (2,0)

if __name__ == "__main__":
    current_number = (0,2)
    number_matrix = {(2,0):'1',
    (1,1): '2', (2,1): '3', (3,1): '4',
    (0,2): '5', (1,2): '6', (2,2): '7', (3,2): '8', (4,2): '9',
    (1,3): 'A', (2,3): 'B', (3,3): 'C',
    (2,4): 'D'}
    f = open('two/input', 'r')
    rows =f.readlines()
    code = ""
    for row in rows:
        for instruction in row:
            current_number = ex1.next_number(instruction, current_number, number_matrix)
        code += str(number_matrix[current_number])
    print(code)
