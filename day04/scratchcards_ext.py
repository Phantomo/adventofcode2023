def read_input():
    with open("input.txt", "r") as f:
        data = f.read().splitlines()
    return data


def clear_data(card_data):
    data = {}
    for i, card in enumerate(card_data, start=1):
        data[i] = {"count": 1}
        card_number, card = card.split(":")
        winning_numbers, numbers = card.strip().split("|")
        winning_numbers = winning_numbers.strip().split()
        numbers = numbers.strip().split()
        data[i]["winning_numbers"], data[i]["numbers"] = winning_numbers, numbers
    return data


def point_cards(cards):
    for i in range(1, len(cards) + 1):
        count = 0
        for number in cards[i]["winning_numbers"]:
            if number in cards[i]["numbers"]:
                count += 1
        for k in range(i + 1, i + count + 1):
            if cards.get(k):
                cards[k]["count"] += cards[i]["count"]
    return cards


def count_winning_points(data) -> int:
    result = 0
    for key in data.keys():
        result += data[key]["count"]
    return result


if __name__ == "__main__":
    data = read_input()
    clean_data = clear_data(data)
    data = point_cards(clean_data)
    print(count_winning_points(data))
