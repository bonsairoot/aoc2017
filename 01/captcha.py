#!/usr/bin/python3

FILE = "aoc01_input.txt"

circlist = None
with open(FILE) as f:
    circlist = f.read()

list_size = len(circlist)
captcha_one = 0
captcha_two = 0
for i in range(list_size):
    if circlist[i] == circlist[(i + 1) % (list_size - 1)]:
        captcha_one += int(circlist[i])
    if circlist[i] == circlist[(i + int(list_size / 2)) % (list_size - 1)]:
        captcha_two += int(circlist[i])

print("Part 1: %d\nPart 2: %d" % (captcha_one, captcha_two))
