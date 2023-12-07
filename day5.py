import re
import numpy as np


with open("input_files\\day5_1.txt") as f:
    data = f.read()


def remove_empty_string(data):
    while True:
        if "" in data:
            data.remove("")
        else:
            return data


def get_data(map_name):
    return list(
        map(
            str.strip,
            re.findall(
                "[0-9 ]*",
                re.findall(f"{map_name} map:\n([0-9  \n]+)\n", data)[0].strip(),
            ),
        )
    )


liste = []
seeds = list(map(int, re.findall("seeds: ([0-9 ]+)", data)[0].split()))
seeds = np.concatenate(
    [np.arange(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
)

soils = get_data("seed-to-soil")
soils = remove_empty_string(soils)


fertilizers = get_data("soil-to-fertilizer")
fertilizers = remove_empty_string(fertilizers)
waters = get_data("fertilizer-to-water")
waters = remove_empty_string(waters)
lights = get_data("water-to-light")
lights = remove_empty_string(lights)
temperatures = get_data("light-to-temperature")
temperatures = remove_empty_string(temperatures)
humidities = get_data("temperature-to-humidity")
humidities = remove_empty_string(humidities)
locations = get_data("humidity-to-location")
locations = remove_empty_string(locations)
location_list = []


def split_values(data):
    data_destination = int(data.split()[0])
    data_source = int(data.split()[1])
    data_range = int(data.split()[2])
    return (data_destination, data_source, data_range)


def control_block(data_source, data_range, previous_value):
    if data_range > 0:
        if (
            previous_value >= data_source
            and previous_value <= data_source + data_range - 1
        ):
            return True
    else:
        if previous_value == data_source:
            return True
    return False


for seed in seeds:
    soil_result = seed
    for soil in soils:
        soil_destination, soil_source, soil_range = split_values(soil)
        if control_block(soil_source, soil_range, seed):
            soil_result = soil_destination + seed - soil_source

    fertilizer_result = soil_result
    for fertilizer in fertilizers:
        fertilizer_destination, fertilizer_source, fertilizer_range = split_values(
            fertilizer
        )
        if control_block(fertilizer_source, fertilizer_range, soil_result):
            fertilizer_result = fertilizer_destination + soil_result - fertilizer_source

    water_result = fertilizer_result
    for water in waters:
        water_destination, water_source, water_range = split_values(water)
        if control_block(water_source, water_range, fertilizer_result):
            water_result = water_destination + fertilizer_result - water_source

    light_result = water_result
    for light in lights:
        light_destination, light_source, light_range = split_values(light)
        if control_block(light_source, light_range, water_result):
            light_result = light_destination + water_result - light_source

    temperature_result = light_result
    for temperature in temperatures:
        temperature_destination, temperature_source, temperature_range = split_values(
            temperature
        )
        if control_block(temperature_source, temperature_range, light_result):
            temperature_result = (
                temperature_destination + light_result - temperature_source
            )
    humidity_result = temperature_result
    for humidity in humidities:
        humidity_destination, humidity_source, humidity_range = split_values(humidity)
        if control_block(humidity_source, humidity_range, temperature_result):
            humidity_result = (
                humidity_destination + temperature_result - humidity_source
            )

    location_result = humidity_result
    for location in locations:
        location_destination, location_source, location_range = split_values(location)
        if control_block(location_source, location_range, humidity_result):
            location_result = location_destination + humidity_result - location_source
    location_list.append(location_result)
print(min(location_list))
