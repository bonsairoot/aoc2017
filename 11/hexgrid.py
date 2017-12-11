#!/usr/bin/python3

import operator

with open('aoc11_input.txt') as f:
    moves = f.read().strip().split(',')

pos = [0, 0]
max_dist = 0
DIR = {
    'n': (0, 1),
    'ne': (1, 1),
    'nw': (-1, 1),
    'e': (1, 0),
    'se': (1, -1),
    's': (0, -1),
    'sw': (-1, -1),
    'w': (-1, 0)
}

for move in moves:
    pos = list(map(operator.add, pos, DIR[move]))
    absolutes = list(map(abs, pos))
    max_dist = max(max(absolutes), max_dist)

print("Part I:  %d" % max(absolutes))
print("Part II: %d" % max_dist)
