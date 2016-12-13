import argparse

def parse_instruction(instruction):
    instruction_parts = instruction.split(' ')
    parsed_instruction = {}
    if instruction_parts[0] == "rect":
        parsed_instruction["instruction"] = "rect"
        columns, rows = instruction_parts[1].split('x')
        parsed_instruction["column"] = int(columns)
        parsed_instruction["row"] = int(rows)
    elif instruction_parts[0] == "rotate":
        if instruction_parts[1] == "row":
            parsed_instruction["instruction"] = "right"
            parsed_instruction["row"] = int(instruction_parts[2][2:])
            parsed_instruction["column"] = int(instruction_parts[-1])
        else:
            parsed_instruction["instruction"] = "down"
            parsed_instruction["column"] = int(instruction_parts[2][2:])
            parsed_instruction["row"] = int(instruction_parts[-1])
    return parsed_instruction

def execute_instruction(instruction, panel):
    parsed_instruction = parse_instruction(instruction)
    temp_panel=[p[:] for p in panel[:]]
    number_of_columns = len(panel[0])
    number_of_rows = len(panel)
    no_switch_off = []
    if parsed_instruction["instruction"] == "rect":
        for i in range(parsed_instruction["row"]):
            for j in range(parsed_instruction["column"]):
                panel[i][j] = 1
    elif parsed_instruction["instruction"] == "down":
        for i in range(0, number_of_rows):
            if temp_panel[i][parsed_instruction["column"]] == 0:
                #print("continuing")
                continue

            row_to_switch_on = (i+parsed_instruction["row"])%number_of_rows 
            panel[row_to_switch_on][parsed_instruction["column"]] = 1
            no_switch_off.append((row_to_switch_on, parsed_instruction["column"]))
            if (i, parsed_instruction["column"]) not in no_switch_off:
                panel[i][parsed_instruction["column"]] = 0
    elif parsed_instruction["instruction"] == "right":
        for i in range(0, number_of_columns):
            if temp_panel[parsed_instruction["row"]][i] == 0:
                #print("continuing")
                continue
            column_to_switch_on = (i+parsed_instruction["column"])%number_of_columns 
            panel[parsed_instruction["row"]][column_to_switch_on] = 1
            no_switch_off.append((parsed_instruction["row"], column_to_switch_on))
            if (parsed_instruction["row"], i) not in no_switch_off:
                panel[parsed_instruction["row"]][i] = 0

    return panel

def count_number_of_lights_on(panel):
    count = 0
    for r in panel:
        for c in r:
            count += c
    return count

def print_panel(panel):
    print("\n")
    for r in panel:
        row_string = ""
        for c in r:
            if c == 0:
                row_string += ". "
            else:
                row_string += "* "
        print(row_string[:-1])
def initialize_panel(col=1, row=1):
    #panel = [[0]*row]*col
    panel = []
    for i in range(row):
        panel.append([])
        for j in range(col):
            panel[i].append(0)
    return panel

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--part', type=int)
    args = parser.parse_args()
    f = open('eight/input', 'r')
    lines = [line.strip() for line in f.readlines()]
    panel = initialize_panel(row=6, col=50)
    if args.part == 1:
        for i in lines:
            panel = execute_instruction(i, panel)
        print_panel(panel)
        print(count_number_of_lights_on(panel))
    elif args.part == 2:
        pass
