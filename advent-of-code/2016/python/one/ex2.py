from . import ex1
LOCATIONS_VISITED = [(0,0)]
LAST_MOVE = (0,0)
def find_hq(move_list):
    global LOCATIONS_VISITED
    global LAST_MOVE
    for move in move_list:
        ex1.move(move.strip())
        positions_visited = get_positions_visited(ex1.get_current_position())
        print(positions_visited)
        for position in positions_visited:
            if position in LOCATIONS_VISITED:
                return position
            else:
                LOCATIONS_VISITED.append(position)
        LAST_MOVE = ex1.get_current_position()


def get_positions_visited(new_position):
    global LOCATIONS_VISITED
    global LAST_MOVE
    positions_visited = []
    if LAST_MOVE[0] == new_position[0]:
        if LAST_MOVE[1] > new_position[1]:
            y_positions_moved = sorted(list(range(new_position[1], LAST_MOVE[1])), reverse = True)
        else:
            y_positions_moved = list(range(LAST_MOVE[1] + 1, new_position[1]+1))
        for p in y_positions_moved:
            positions_visited.append((LAST_MOVE[0],p))
    if LAST_MOVE[1] == new_position[1]:
        if LAST_MOVE[0] > new_position[0]:
            y_positions_moved = sorted(list(range(new_position[0], LAST_MOVE[0])), reverse = True)
        else:
            y_positions_moved = list(range(LAST_MOVE[0] + 1, new_position[0]+1))
        for p in y_positions_moved:
            positions_visited.append((p,LAST_MOVE[1]))

    return positions_visited

    
def reset_position():
    global LOCATIONS_VISITED
    global LAST_MOVE
    LOCATIONS_VISITED = [(0,0)]
    LAST_MOVE = (0,0)


if __name__ == "__main__":
    f = open('one/ex1.input', 'r')
    info = f.read()
    steps = info.split(',')
    ex1.reset_position()
    ex1.CURRENT_POSITION = find_hq(steps)
    print(ex1.get_distance_from_start())
