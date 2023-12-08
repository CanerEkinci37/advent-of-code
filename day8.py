import re


def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


def lcm(x, y):
    return (x * y) // gcd(x, y)


def multiple_lcm(numbers):
    if len(numbers) < 2:
        return None
    lcm_value = numbers[0]
    for i in range(1, len(numbers)):
        lcm_value = lcm(lcm_value, numbers[i])
    return lcm_value


# Day 8 - 1
def calculate_steps(instruction, nodes):
    idx = 0
    step = 0
    current_state = nodes["AAA"]
    while idx < len(instruction):
        if instruction[idx] == "L":
            if current_state[0] == "ZZZ":
                step += 1
                break
            else:
                current_state = nodes[current_state[0]]
                step += 1
        else:
            if current_state[1] == "ZZZ":
                step += 1
                break
            else:
                current_state = nodes[current_state[1]]
                step += 1
        idx += 1
        if idx == len(instruction):
            idx = 0
    return step


# Day 8 - 2
def calculate_steps_simultaneously(instruction, nodes):
    current_states = [node for node in nodes if node.endswith("A")]
    find_states = [0 for i in range(len(current_states))]

    for i in range(len(current_states)):
        idx = 0
        step = 0
        while idx < len(instruction):
            step += 1
            if instruction[idx] == "L":
                current_states[i] = nodes[current_states[i]][0]
            else:
                current_states[i] = nodes[current_states[i]][1]
            idx += 1
            if current_states[i].endswith("Z"):
                find_states[i] = step
                break
            if idx == len(instruction):
                idx = 0
    val = 1
    for value in find_states:
        val *= value

    return find_states


nodes = {}
with open("input_files\\day8_1.txt") as f:
    data = list(map(str.strip, f.readlines()))
instruction = data[0]
for i in range(2, len(data)):
    nodes[data[i][:3]] = (data[i][7:10], data[i][12:15])
print(multiple_lcm(sorted(calculate_steps_simultaneously(instruction, nodes))))
