#!/usr/bin/python3
import math

with open('aoc6_input.txt') as f:
    blocks = list(map(int, f.read().split()))

current_state = tuple(blocks)
states = {}
list_size = len(blocks)
iterations = 0

while not states.get(current_state, False):
    states[current_state] = iterations

    block_size = max(blocks)
    current_mem = blocks.index(block_size)
    blocks[current_mem] = 0

    # This avoids multiple iterations over the list
    base = math.floor(block_size / list_size)
    add_inc = block_size % list_size
    for i in range(1, len(blocks) + 1):
        if add_inc > 0:
            blocks[(current_mem + i) % list_size] += base + 1
            add_inc -= 1
        else:
            blocks[(current_mem + i) % list_size] += base

    current_state = tuple(blocks)
    iterations += 1

print("Part I:  %d" % iterations)
print("Part II: %d" % (iterations - states[current_state]))
