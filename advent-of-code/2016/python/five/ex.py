from hashlib import md5
import argparse

def find_next_hash_character(door_id, current_hash_index):
    while True:
        hash = md5(bytes(door_id + str(current_hash_index), 'ascii')).hexdigest()
        if hash.startswith('00000'):
            return (hash[5], current_hash_index, hash)
        current_hash_index += 1

def find_next_hash_character_two(door_id, current_hash_index):
    result = find_next_hash_character(door_id, current_hash_index)
    if result[2][5].isnumeric():
        which_character = int(result[2][5])
    else:
        return ('', None, result[1])
    
    if which_character < 8:
        return (result[2][6], which_character, result[1])
    else:
        return ('', None, result[1])

def find_password(door_id):
    password = ""
    current_hash_index = 0
    for i in range(0,8):
        result = find_next_hash_character(door_id, current_hash_index)
        current_hash_index = result[1] + 1
        password += result[0]
    return password

def find_password_door_two(door_id):
    current_hash_index = 0
    characters = [" "]*8
    password = " "*8
    while password.find(" ") != -1:
        result  = find_next_hash_character_two(door_id, current_hash_index)
        current_hash_index = result[2] + 1
        if result[0] == "":
            continue
        if characters[result[1]] == " ":
            characters[result[1]] = result[0]
        password = "".join(characters)
    return password
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--part', type=int)
    args = parser.parse_args()
    f = open('five/input', 'r')
    door_id = f.read().strip()
    if args.part == 1:
        print(find_password(door_id))
    elif args.part == 2:
        print(find_password_door_two(door_id))
