def read_input():
    with open("input.txt", "r") as f:
        data = f.readlines()
    return data

def find_first_number(line):
    for c in line:
        if c.isdigit():
            return int(c)

def get_calibrate_value(line):
    value = find_first_number(line) * 10
    value += find_first_number(line[::-1])
    return value


if __name__ == "__main__":
    data = read_input()
    print(sum([get_calibrate_value(line) for line in data]))
