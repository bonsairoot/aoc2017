#!/usr/bin/python3

PART = 2

with open('aoc5_input.txt') as f:
    maze = list(map(int, f.read().splitlines()))

curr_pos = 0
steps = 0

while True:
    old_pos = curr_pos
    curr_pos += maze[curr_pos]
    steps += 1
    if curr_pos < 0 or curr_pos > len(maze) - 1:
        break
    if PART == 1:
        maze[old_pos] += 1
    else:
        maze[old_pos] += -1 if maze[old_pos] >= 3 else 1

print(steps)
