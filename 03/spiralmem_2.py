#!/usr/bin/python3
from enum import Enum

INPUT = 265149
# Setting Listsize is not clean but simplifies code and visualization
# of the grid and in this case we know that the value most probably won't
# be outside these bounds
LISTSIZE = 500

class Dir(Enum):
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3

current_val = 0
current_step = 1
second_time = False
step_size = 1
moving = Dir.RIGHT
pos = [LISTSIZE/2,LISTSIZE/2]
grid = [[0 for x in range(LISTSIZE)] for y in range(LISTSIZE)]
grid[LISTSIZE/2][LISTSIZE/2] = 1

def calc_current_val():
    cell_val = 0
    ranges = [-1,0,1]
    for x in ranges:
        for y in ranges:
            cell_val += grid[pos[0] + x][pos[1] + y]
    return cell_val

while(current_val<INPUT):
    current_step -= 1
    if moving == Dir.RIGHT:
        pos[0] += 1
    elif moving == Dir.UP:
        pos[1] += 1
    elif moving == Dir.LEFT:
        pos[0] -= 1
    else:
        pos[1] -= 1
    current_val = calc_current_val()
    grid[pos[0]][pos[1]] = current_val

    if current_step == 0:
        moving = Dir((moving.value + 1) % 4)
        if second_time:
            step_size += 1
        second_time = not second_time
        current_step = step_size

print(current_val)
