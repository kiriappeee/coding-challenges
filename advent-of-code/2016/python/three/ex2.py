from three import ex1
def get_triangles_from_columns(lines):
    number_of_lines = len(lines)
    index_column = 0
    index_row = 0
    triangles = []
    while True:
        triangles.append([lines[index_row][index_column],
            lines[index_row+1][index_column],
            lines[index_row+2][index_column]])
        index_row += 3
        if index_row == number_of_lines:
            index_row = 0
            index_column += 1
            if index_column == 3:
                break
        if index_row > number_of_lines:
            print("BREAKING COS GREATER")
            break
    return triangles

if __name__ == "__main__":
    f = open('three/input', 'r')
    lines = f.readlines()
    rows = []
    for line in lines:
        rows.append([int(n.strip()) for n in line.strip().split(' ') if n.isnumeric()])
    triangles = get_triangles_from_columns(rows)
    count_of_correct_triangles = 0
    for triangle in triangles:
        if ex1.is_triangle(triangle):
            count_of_correct_triangles += 1

    print(count_of_correct_triangles)
