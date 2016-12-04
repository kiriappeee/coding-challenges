def is_triangle(points):
    if (points[0]+points[1]>points[2]) and (points[1] + points[2] > points[0]) and (points[0] + points[2] > points[1]):
        return True
    else:
        return False

if __name__ == "__main__":
    f = open('three/input', 'r')
    lines = f.readlines()
    count_of_correct_triangles = 0
    for line in lines:
        points = [int(n.strip()) for n in line.strip().split(' ') if n.isnumeric()]
        print(points)
        if is_triangle(points):
            count_of_correct_triangles += 1
    print(count_of_correct_triangles)
