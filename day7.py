# Day 7 - 1
high_cards = []
one_pairs = []
two_pairs = []
three_of_kinds = []
full_houses = []
four_of_kinds = []
five_of_kinds = []


def card_check(card):
    set_card = set(card)
    if len(set_card) == 1:
        five_of_kinds.append(card)
    elif len(set_card) == 5:
        high_cards.append(card)
    elif len(set_card) == 4:
        one_pairs.append(card)
    elif len(set_card) == 2:
        for c in card:
            if card.count(c) == 3:
                full_houses.append(card)
                break
            elif card.count(c) == 4:
                four_of_kinds.append(card)
                break
    elif len(set_card) == 3:
        for c in card:
            if card.count(c) == 3:
                three_of_kinds.append(card)
                break
            elif card.count(c) == 2:
                two_pairs.append(card)
                break


def calculate_total_winning(data):
    acc = 0
    all_hands = []
    card_dict = {}
    for hand in data:
        card = (
            hand[:5]
            .replace("A", "E")
            .replace("T", "A")
            .replace("J", "B")
            .replace("Q", "C")
            .replace("K", "D")
        )
        value = int(hand[6:])
        card_dict[card] = value
        card_check(card)

    all_hands = (
        sorted(high_cards)
        + sorted(one_pairs)
        + sorted(two_pairs)
        + sorted(three_of_kinds)
        + sorted(full_houses)
        + sorted(four_of_kinds)
        + sorted(five_of_kinds)
    )

    for idx, card in enumerate(all_hands, start=1):
        acc += idx * card_dict[card]
    return acc


with open("input_files\\day7_1.txt") as f:
    data = list(map(str.strip, f.readlines()))
print(calculate_total_winning(data=data))


high_cards.clear()
one_pairs.clear()
two_pairs.clear()
three_of_kinds.clear()
full_houses.clear()
four_of_kinds.clear()
five_of_kinds.clear()


def card_check_with_jokers(card):  # 32A3C
    set_card = set(card)
    if len(set_card) == 1:
        five_of_kinds.append(card)
    elif len(set_card) == 5:
        if "1" in set_card:
            one_pairs.append(card)
        else:
            high_cards.append(card)
    elif len(set_card) == 4:
        if "1" in set_card:
            three_of_kinds.append(card)
        else:
            one_pairs.append(card)
    elif len(set_card) == 2:
        for c in card:
            if card.count(c) == 3:
                if "1" in card:
                    five_of_kinds.append(card)
                    break
                else:
                    full_houses.append(card)
                    break
            elif card.count(c) == 4:
                if "1" in card:
                    five_of_kinds.append(card)
                    break
                else:
                    four_of_kinds.append(card)
                    break
    elif len(set_card) == 3:
        for c in card:
            if card.count(c) == 3:
                if "1" in card:
                    four_of_kinds.append(card)
                    break
                else:
                    three_of_kinds.append(card)
                    break
            elif card.count(c) == 2:
                if "1" in card:
                    if card.count("1") == 1:
                        full_houses.append(card)
                        break
                    else:
                        four_of_kinds.append(card)
                        break
                else:
                    two_pairs.append(card)
                    break


print(one_pairs)


def calculate_total_winning_with_jokers(data):
    acc = 0
    all_hands = []
    card_dict = {}
    for hand in data:
        card = (
            hand[:5]
            .replace("A", "D")
            .replace("T", "A")
            .replace("J", "1")
            .replace("Q", "B")
            .replace("K", "C")
        )
        value = int(hand[6:])
        card_dict[card] = value
        card_check_with_jokers(card)

    all_hands = (
        sorted(high_cards)
        + sorted(one_pairs)
        + sorted(two_pairs)
        + sorted(three_of_kinds)
        + sorted(full_houses)
        + sorted(four_of_kinds)
        + sorted(five_of_kinds)
    )

    for idx, card in enumerate(all_hands, start=1):
        acc += idx * card_dict[card]
    return acc


with open("input_files\\day7_1.txt") as f:
    data = list(map(str.strip, f.readlines()))
print(calculate_total_winning_with_jokers(data=data))
