# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import pprint


def parse_file(input_file_path):
    if input_file_path is None:
        return

    command_list = []

    with open(input_file_path, 'r') as input_file:
        for line in input_file.readlines():
            entry = line.strip().split()
            command_list.append(entry)

    return command_list


def do_command(parsed_command):
    match parsed_command[0]:
        case "P":
            print("Select Pen #" + parsed_command[1])
        case "D" | "U":
            print("Pen Up/Down " + parsed_command[0])
        case "N" | "S" | "E" | "W":
            print("Move Pen " + parsed_command[0] + " " + parsed_command[1] + " steps")


def main():
    input_file = sys.argv[1]
    command_list = parse_file(input_file)

    for command in command_list:
        pprint.pprint(command)
        do_command(command)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
