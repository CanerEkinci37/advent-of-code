import re
import numpy as np

# Day 2 - 1


def calculate_sum_of_id(data):
    id_list = []
    for i in range(len(data)):
        red_cube_count = np.array([list(map(int, re.findall("(\d*) red", data[i])))])
        blue_cube_count = np.array([list(map(int, re.findall("(\d*) blue", data[i])))])
        green_cube_count = np.array(
            [list(map(int, re.findall("(\d*) green", data[i])))]
        )

        if (
            len(red_cube_count[red_cube_count > 12]) > 0
            or len(green_cube_count[green_cube_count > 13]) > 0
            or len(blue_cube_count[blue_cube_count > 14]) > 0
        ):
            continue

        id_list.append(i + 1)
    return sum(id_list)


with open("input_files\\day2_1.txt") as f:
    data = list(map(str.strip, f.readlines()))
print(calculate_sum_of_id(data=data))


# Day 2 - 2


def calculate_sum_power_of_sets(data):
    power_of_sets = []
    for text in data:
        max_red_cube = max(list(map(int, re.findall("(\d*) red", text))))
        max_green_cube = max(list(map(int, re.findall("(\d*) green", text))))
        max_blue_cube = max(list(map(int, re.findall("(\d*) blue", text))))

        power_of_sets.append(max_red_cube * max_green_cube * max_blue_cube)
    return sum(power_of_sets)


with open("input_files\\day2_2.txt") as f:
    data = list(map(str.strip, f.readlines()))
print(calculate_sum_power_of_sets(data=data))
