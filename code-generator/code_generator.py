# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import pprint


def parse_file(input_file_path):
    if input_file_path is None:
        return

    code_parameters = []

    with open(input_file_path, 'r') as input_file:
        for line in input_file.readlines():
            entry = line.strip()
            code_parameters.append(entry)

    return code_parameters


def write_header_file(code_parameters):
    base_file_name = code_parameters[0]
    file_output = ["extern const char* " + base_file_name.upper() + "_" + base_file_name + "s[];\n",
                   "typedef enum {" + "\n"]

    for param in code_parameters[1:]:
        file_output.append("\t" + param + "," + "\n")

    file_output.append("}" + base_file_name.upper() + "\n")

    with open(base_file_name + ".h", "w") as header_file:
        header_file.writelines(file_output)

def write_c_file(code_parameters):
    base_file_name = code_parameters[0]
    file_output = ["const char* " + base_file_name.upper() + "_" + base_file_name + "s[]={\n"]

    for param in code_parameters[1:]:
        file_output.append("\t\"" + param + "\"," + "\n")

    file_output.append("};\n")

    with open(base_file_name + ".c", "w") as header_file:
        header_file.writelines(file_output)


def main():
    input_file = sys.argv[1]
    code_parameters = parse_file(input_file)
    pprint.pprint(code_parameters)
    write_header_file(code_parameters)
    write_c_file(code_parameters)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
