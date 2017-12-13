#!/usr/bin/python3

import re

with open('aoc13_input.txt') as f:
    matches = re.findall(r"(\d+): (\d+)", f.read())
    layers = {int(x[0]): int(x[1]) for x in matches}


def get_severity(delay):
    severity = 0
    caught = False
    for layer, depth in layers.items():
        if (layer + delay) % ((depth - 1) * 2) == 0:
            caught = True
            severity += layer * depth
    return (severity, caught)


severity, caught = get_severity(0)
print("Part I: %d" % severity)

delay = 0
while caught:
    delay += 1
    severity, caught = get_severity(delay)

print("Part II: %d" % delay)
