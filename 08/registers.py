#!/usr/bin/python3

import re
import operator

PATTERN = r"(\w+) (\w+) ([-\d]+) if ((\w+).*)$"
registers = {}
max_regval = 0
operators = {"inc": operator.add, "dec": operator.sub}

with open('aoc8_input.txt') as f:
    for line in f.readlines():
        (reg, fn, value, condition, creg) = re.findall(PATTERN, line)[0]
        condition = condition.replace(creg, "registers.get(creg,0)")
        if eval(condition):
            new_val = operators[fn](registers.get(reg, 0), int(value))
            max_regval = max(max_regval, new_val)
            registers[reg] = new_val

biggest_regval = max(list(registers.values()))
print("Part I: %d" % (biggest_regval))
print("Part II: %d" % (max_regval))
