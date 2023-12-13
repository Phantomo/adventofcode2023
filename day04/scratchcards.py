def read_input():
    with open("input.txt", "r") as f:
        data = f.read().splitlines()
    return data


def find_card_points(card):
    winning_numbers, numbers = card.strip(" ").split("|")
    winning_numbers = winning_numbers.strip(" ").split(" ")
    winning_numbers = [number for number in winning_numbers if number.strip(" ")]
    numbers = numbers.strip(" ").split(" ")
    card_winning_numbers_count = 0
    for number in winning_numbers:
        if number in numbers:
            card_winning_numbers_count += 1
    return pow(2, card_winning_numbers_count - 1) if card_winning_numbers_count > 0 else 0


def count_winning_points(data) -> int:
    result = 0
    for card in data:
        card_number, card_data = card.split(":")
        card_points = find_card_points(card_data)
        result += card_points
    return result


if __name__ == "__main__":
    data = read_input()
    print(count_winning_points(data))
