#!/usr/bin/python3

import numpy as np
import operator
import time

rows = []
grid = []
INPUT = "xlqgujun"
visited = []

def fill_group(i, j):
    if (i, j) in visited:
        return
    visited.append((i, j))
    if i - 1 >= 0 and grid[i - 1][j]:
        fill_group(i - 1, j)
    if j - 1 >= 0 and grid[i][j - 1]:
        fill_group(i, j - 1)
    if i + 1 < 128 and grid[i + 1][j]:
        fill_group(i + 1, j)
    if j + 1 < 128 and grid[i][j + 1]:
        fill_group(i, j + 1)

for i in range(128):
    rows.append(list(map(ord, INPUT + "-" + str(i))) + [17, 31, 73, 47, 23])

# Fill Grid (from Day 10)
for (ind, row) in enumerate(rows):
    clist = range(256)
    list_size = len(clist)
    pos = 0
    step_size = 0
    for i in range(64):
        for seq in row:
            roll = pos + seq - list_size
            if roll > 0:
                clist = np.roll(clist, -roll)
                pos -= roll
            clist[pos:pos + seq] = clist[pos:pos + seq][::-1]
            if roll > 0:
                clist = np.roll(clist, roll)
                pos += roll
            pos = (pos + seq + step_size) % len(clist)
            step_size += 1

    chunks = [clist[i:i + 16] for i in range(0, len(clist), 16)]
    dense = [reduce(operator.xor, x) for x in chunks]
    hash = ''.join(map(lambda x: hex(x)[-3:-1].replace('x', '0'), dense))
    grid.append(list(map(int, bin(int(hash, 16))[2:].zfill(128))))

used = sum(sum(x) for x in grid)
print("Part I:  %d" % used)

groups = 0
for i in range(128):
    for j in range(128):
        if not grid[i][j] or (i, j) in visited:
            continue
        fill_group(i, j)
        groups += 1

print("Part II: %d" % groups)
