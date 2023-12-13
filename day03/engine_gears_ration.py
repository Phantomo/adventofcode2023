def read_input():
    with open("input.txt") as f:
        data = f.read().splitlines()
    return data


def find_two_digit_neighbors(data, x, y):
    neighbors = []
    for i in range(x - 1, x + 2):
        for k in range(y - 1, y + 2):
            if i < 0 or k < 0 or i >= len(data) or k >= len(data[x]):
                continue
            if data[i][k].isdigit():
                neighbors.append((i, k))
    if len(neighbors) > 1:
        return neighbors


def find_number_coordinate_by_one_pos(data, start_pos_x, start_pos_y):
    start_coordinate_y = 0
    line = data[start_pos_x]
    for i in sorted(range(0, start_pos_y + 1), reverse=True):
        # print(i, "----")
        if not line[i].isdigit():
            start_coordinate_y = i + 1
            break
    for n in range(start_coordinate_y, len(line)):
        if not line[n].isdigit():
            return (start_pos_x, start_coordinate_y), (start_pos_x, n)
    return (start_pos_x, start_coordinate_y), (start_pos_x, len(line))


def multiply_list(lst: list[int]) -> int:
    result = 1
    for i in lst:
        result *= i
    return result


def find_gears(data):
    sum_of_gear_ratios = 0
    for i in range(len(data)):
        for k in range(len(data[i])):
            if data[i][k] == "*":
                neighbors = find_two_digit_neighbors(data, i, k)
                if neighbors:
                    unique_coordinates = set(
                         [find_number_coordinate_by_one_pos(data, coord[0], coord[1]) for coord in neighbors]
                    )
                    if len(unique_coordinates) == 2:
                        sum_of_gear_ratios += multiply_list([int(data[coord[0][0]][coord[0][1]:coord[1][1]]) for coord in unique_coordinates])

    return sum_of_gear_ratios


if __name__ == "__main__":
    data = read_input()
    print(find_gears(data))
