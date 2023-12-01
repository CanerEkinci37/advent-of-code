# Day 1-1


def calculate_calibration_with_just_numbers(line_list):
    calibration_value = 0
    for text in line_list:
        digit_list = []
        text = text.strip()
        for char in text:
            if char.isdigit():
                digit_list.append(char)

        if len(digit_list) == 1:
            calibration_value += int(digit_list[0] * 2)
        else:
            calibration_value += int(digit_list[0] + digit_list[-1])
    return calibration_value


with open("input_files\\day1_1.txt") as f:
    data = f.readlines()
print(calculate_calibration_with_just_numbers(data))


# Day 1-2


def calculate_value(line_list):
    calibration_value = 0
    for text in line_list:
        digit_list = []
        text = (
            text.strip()
            .replace("one", "o1e")
            .replace("two", "t2o")
            .replace("three", "t3e")
            .replace("four", "4")
            .replace("five", "5e")
            .replace("six", "6")
            .replace("seven", "7n")
            .replace("eight", "e8t")
            .replace("nine", "n9e")
        )

        for char in text:
            if char.isdigit():
                digit_list.append(char)

        if len(digit_list) == 1:
            calibration_value += int(digit_list[0] * 2)
        else:
            calibration_value += int(digit_list[0] + digit_list[-1])

    return calibration_value


with open("input_files\\day1_2.txt") as f:
    data = f.readlines()
print(calculate_value(data))
