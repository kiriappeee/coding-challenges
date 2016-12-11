import argparse

def find_common_character_in_column(column_index, input, least=False):
    character_count = {}
    for row in input:
        if row[column_index] not in character_count:
            character_count[row[column_index]] = 1
        else:
            character_count[row[column_index]] += 1
    if not least:
        return sorted(character_count.items(), key=lambda item: item[1], reverse=True)[0][0]
    else:
        return sorted(character_count.items(), key=lambda item: item[1], reverse=False)[0][0]


def get_error_corrected_message(input, decoding_method="MOST"):
    input_length = len(input[0])
    correct_message = ""
    for i in range(0,input_length):
        if decoding_method == "MOST":
            correct_message += find_common_character_in_column(i, input)
        else:
            correct_message += find_common_character_in_column(i, input, least=True)

    return correct_message


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--part', type=int)
    args = parser.parse_args()
    f = open('six/input', 'r')
    input_string = f.readlines()
    input = [s.strip() for s in input_string]
    if args.part == 1:
        print(get_error_corrected_message(input))
    elif args.part == 2:
        print(get_error_corrected_message(input, decoding_method="LEAST"))

