def read_input():
    with open("input.txt", "r") as f:
        data = f.read().splitlines()
    return data

def check_neighbors_has_symbol(data, x, y):
    for i in range(x - 1, x + 2):
        for k in range(y - 1, y + 2):
            if i < 0 or k < 0 or i >= len(data) or k >= len(data[x]):
                continue
            if data[i][k] != "." and not data[i][k].isdigit():
                return True
    return False

def find_value_in_engine(data):
    sum_of_numbers = 0
    for i in range(len(data)):
        number = ""
        part_of_engine = False
        for k in range(len(data[i])):
            if data[i][k].isdigit():
                number += data[i][k]
                if not part_of_engine and check_neighbors_has_symbol(data, i, k):
                    part_of_engine = True
            else:
                if number and part_of_engine:
                    sum_of_numbers += int(number)
                number = ""
                part_of_engine = False
        if part_of_engine:
            sum_of_numbers += int(number)
    return sum_of_numbers


if __name__ == "__main__":
    data = read_input()
    print(find_value_in_engine(data))
