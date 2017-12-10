#!/usr/bin/python3

import numpy as np
import operator

PART = 2

with open('aoc10_input.txt') as f:
    if PART == 1:
        seqs = list(map(int, f.read().split(',')))
    else:
        seqs = list(map(ord, f.read().strip())) + [17, 31, 73, 47, 23]

clist = range(256)
list_size = len(clist)
pos = 0
step_size = 0
for i in range(64):
    for seq in seqs:
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
    if i == 0 and PART == 1:
        print("Part I: %d" % (clist[0] * clist[1]))
        break

chunks = [clist[i:i + 16] for i in range(0, len(clist), 16)]
dense = [reduce(operator.xor, x) for x in chunks]
hash = ''.join(map(lambda x: hex(x)[-3:-1].replace('x', '0'), dense))
print("Part II: %s" % hash)
