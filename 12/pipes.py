#!/usr/bin/python3

import re
import time
neighbours = {}
visited = []


def connections(node):
    visited.append(node)
    nb_conns = 1
    for nb in neighbours[node]:
        if nb not in visited:
            nb_conns += connections(nb)
    return nb_conns


with open('aoc12_input.txt') as f:
    for line in f.readlines():
        progs = list(map(int, re.findall(r"\d+", line)))
        neighbours[progs[0]] = progs[1:]

print(connections(0))

groups = 1
for key, nb in neighbours.items():
    if key in visited:
        continue
    connections(key)
    groups += 1

print(groups)
