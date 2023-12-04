import re


def find_winning_and_my_numbers(text):
    winning_numbers = set(
        map(int, re.findall("Card[ ]*\d+: ([0-9 ]+) ", text)[0].split())
    )
    my_numbers = set(map(int, re.findall("\|[ ]*([0-9 ]+)", text)[0].split()))
    return winning_numbers.intersection(my_numbers)


def p1(data):
    acc = 0
    for text in data:
        matching_numbers = find_winning_and_my_numbers(text)
        if len(matching_numbers):
            acc += 2 ** (len(matching_numbers) - 1)
    return acc


def p2(data):
    scratch_cards = 0
    card_dicts = {f"{i}": 0 for i in range(1, len(data) + 1)}
    for idx, text in enumerate(data, start=1):
        matching_numbers = find_winning_and_my_numbers(text)
        for i in range(idx + 1, idx + len(matching_numbers) + 1):
            card_dicts[str(i)] += card_dicts[str(idx)] + 1
    for k in card_dicts.keys():
        scratch_cards += 1 + card_dicts[k]
    return scratch_cards


with open("input_files\\day4_1.txt") as f:
    data = list(map(str.strip, f.readlines()))

print(p2(data))
