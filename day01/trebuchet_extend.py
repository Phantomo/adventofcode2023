def read_input():
    with open("input.txt", "r") as f:
        data = f.readlines()
    return data


def find_first_number(line, reverse=False):
    digit_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    for pos, c in enumerate(line):
        if c.isdigit():
            return int(c)
        for digit in digit_dict.keys():
            if reverse:
                reverse_digit = digit[::-1]
                if reverse_digit == line[pos: pos + len(digit)]:
                    return digit_dict.get(digit)
            else:
                if digit == line[pos: pos + len(digit)]:
                    return digit_dict.get(digit)


def get_calibrate_value(line):
    print(line)
    value = find_first_number(line) * 10
    print(value)
    value += find_first_number(line[::-1], reverse=True)
    print(value)
    return value


if __name__ == "__main__":
    data = read_input()
    print(sum([get_calibrate_value(line) for line in data]))
