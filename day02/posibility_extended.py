def read_input():
    with open("input.txt", "r") as f:
        data = f.readlines()
    return data


def clean_attemps_data(data):
    cube_positions = {
        "red": 0,
        "green": 1,
        "blue": 2
    }
    games = data.split(';')
    clean_data = []
    for game in games:
        empty_game = [0, 0, 0]
        cubes = game.rstrip("\n").split(',')
        for cube in cubes:
            cube_value, cube_color = cube.strip(" ").split(" ")
            empty_game[cube_positions.get(cube_color)] = int(cube_value)
        clean_data.append(empty_game)
    return clean_data

def prepera_data(data):
    clean_data = {}
    for line in data:
        game, tries = line.split(":")
        clean_data[int(game.split(" ")[1])] = clean_attemps_data(tries)
    return clean_data


def list_eq_or_smaller(lst, compare):
    for i in range(len(lst)):
        if lst[i] > compare[i]:
            return False
    return True


def get_max_power_of_colors(game):
    result = 1
    for i in range(len(game[0])):
        result *= max([try_[i] for try_ in game])
    return result


if __name__ == "__main__":
    data = read_input()
    data = prepera_data(data)
    print(sum([get_max_power_of_colors(value) for key, value in data.items()]))