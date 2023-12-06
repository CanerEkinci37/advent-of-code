import re
import numpy as np

pattern = ":[ ]+([0-9 ]+)"


def calculate_multiple_numbers_of_way(times, distances):
    numbers_of_way = 1
    for i in range(len(times)):
        time_start = 0
        time_end = times[i]
        count = 0
        while time_start <= times[i]:
            if (time_start * time_end) > distances[i]:
                count += 1
            time_start += 1
            time_end -= 1
        numbers_of_way *= count
    return numbers_of_way


def calculate_one_numbers_of_way(time, distance):
    numbers_of_way = 0
    for i in range(time):
        if i * (time - i) > distance:
            numbers_of_way += 1
    return numbers_of_way


with open("input_files\\day6_1.txt") as f:
    data = list(map(str.strip, f.readlines()))
times = list(map(int, re.findall(pattern, data[0])[0].split()))
distances = list(map(int, re.findall(pattern, data[1])[0].split()))
print(calculate_multiple_numbers_of_way(times, distances))

time = int("".join(re.findall(pattern, data[0])[0].split()))
distance = int("".join(re.findall(pattern, data[1])[0].split()))
print(calculate_one_numbers_of_way(time, distance))
