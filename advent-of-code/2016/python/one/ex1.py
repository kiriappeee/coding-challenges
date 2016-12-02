CURRENT_POSITION = (0,0)
CURRENT_DIRECTION = "NORTH"
def get_current_position():
    global CURRENT_POSITION
    return CURRENT_POSITION

def get_current_direction():
    global CURRENT_DIRECTION
    return CURRENT_DIRECTION

def move(instruction):
    global CURRENT_POSITION
    global CURRENT_DIRECTION
    move_direction = instruction[0]
    if CURRENT_DIRECTION == "NORTH":
        if move_direction == "R":
            CURRENT_DIRECTION = "EAST"
        elif move_direction == "L":
            CURRENT_DIRECTION = "WEST"
    elif CURRENT_DIRECTION == "SOUTH":
        if move_direction == "R":
            CURRENT_DIRECTION = "WEST"
        elif move_direction == "L":
            CURRENT_DIRECTION = "EAST"
    elif CURRENT_DIRECTION == "EAST":
        if move_direction == "R":
            CURRENT_DIRECTION = "SOUTH"
        elif move_direction == "L":
            CURRENT_DIRECTION = "NORTH"
    elif CURRENT_DIRECTION == "WEST":
        if move_direction == "R":
            CURRENT_DIRECTION = "NORTH"
        elif move_direction == "L":
            CURRENT_DIRECTION = "SOUTH"
    movement_distance = int(instruction[1:])
    if CURRENT_DIRECTION == "NORTH":
        CURRENT_POSITION = (CURRENT_POSITION[0], CURRENT_POSITION[1] + movement_distance)
    elif CURRENT_DIRECTION == "SOUTH":
        CURRENT_POSITION = (CURRENT_POSITION[0], CURRENT_POSITION[1] - movement_distance)
    elif CURRENT_DIRECTION == "EAST":
        CURRENT_POSITION = (CURRENT_POSITION[0] + movement_distance, CURRENT_POSITION[1])
    elif CURRENT_DIRECTION == "WEST":
        CURRENT_POSITION = (CURRENT_POSITION[0] - movement_distance, CURRENT_POSITION[1])
    return True

def get_distance_from_start():
    return abs(CURRENT_POSITION[0]+CURRENT_POSITION[1])

def reset_position():
    global CURRENT_POSITION
    global CURRENT_DIRECTION
    CURRENT_POSITION = (0,0)
    CURRENT_DIRECTION = "NORTH"

def do_test():
    f = open('one/ex1.input', 'r')
    info = f.read()
    steps = info.split(',')
    print(steps)
    reset_position()
    for step in steps:
        print(step.strip())
        move(step.strip())
    print(get_distance_from_start())
