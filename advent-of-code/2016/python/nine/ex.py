import re
import argparse
def decompress_message(message):
    matches = re.finditer("\([0-9]+x[0-9]+\)", message)
    current_index = 0
    decompressed_string = ""
    for match in matches:
        if match.start() < current_index:
            continue
        decompressed_string += message[current_index:match.start()]
        match_string = message[match.start()+1:match.end()-1]
        number_of_characters = int(match_string.split('x')[0])
        number_of_repeats = int(match_string.split('x')[1])
        characters_to_repeat = message[match.end():match.end()+number_of_characters]
        decompressed_string += characters_to_repeat*number_of_repeats
        current_index = match.end() + number_of_characters
    decompressed_string += message[current_index:]
    return decompressed_string

def find_decompress_length(message, sub_call = False):
    matches = re.finditer("\([0-9]+x[0-9]+\)", message)
    current_index = 0
    length = 0
    for match in matches:
        if match.start() < current_index:
            continue
        length += len(message[current_index:match.start()])
        number_of_characters, number_of_repeats, characters_to_repeat = get_match_parts(message, match)
        sub_matches = list(re.finditer("\([0-9]+x[0-9]+\)", characters_to_repeat))
        if sub_matches:
            length += number_of_repeats * find_decompress_length(characters_to_repeat, sub_call=True)
        else:
            if sub_call:
                length += number_of_repeats * number_of_characters
            else:
                length += number_of_repeats*number_of_characters
        current_index = match.end() + number_of_characters
    length += len(message[current_index:])
    return length

def get_match_parts(message, match):
    match_string = message[match.start()+1:match.end()-1]
    number_of_characters = int(match_string.split('x')[0])
    number_of_repeats = int(match_string.split('x')[1])
    characters_to_repeat = message[match.end():match.end()+number_of_characters]
    return number_of_characters, number_of_repeats, characters_to_repeat

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--part', type=int)
    args = parser.parse_args()
    f = open('nine/input', 'r')
    message = f.read().replace('\n', '')
    if args.part == 1:
        print(message)
        print(len(decompress_message(message)))
    elif args.part == 2:
        print(find_decompress_length(message))
