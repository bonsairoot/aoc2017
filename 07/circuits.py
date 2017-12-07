#!/usr/bin/python3

import re
from collections import Counter


class Program():
    def __init__(self, name, weight=None, children=None, parent=None):
        self.name = name
        self.weight = weight
        self.children = children
        self.parent = parent

    def add_attr(self, weight, children):
        self.children = children
        self.weight = weight
        for child in children:
            tree_index[child].parent = self.name


def recSumOfWeights(node):
    child_weights = []
    path = []
    for child in node.children:
        (cpath, cw) = recSumOfWeights(tree_index[child])
        path += cpath
        child_weights.append(cw)

    for i, v in Counter(child_weights).items():
        if v == 1:
            culprit_index = child_weights.index(i)
            offset = i - child_weights[(culprit_index + 1) % len(child_weights)]
            offset = tree_index[node.children[culprit_index]].weight - offset
            path.append((node.children[culprit_index], offset))

    return (path, sum(child_weights) + node.weight)


tree_index = {}
with open('aoc7_input.txt') as f:
    for line in f.readlines():
        matches = re.match(r"(\w+)\s+\((\d+)\)\s*-?>?\s*([\w, ]+)?", line)
        (name, weight, children) = matches.groups()
        weight = int(weight)
        children = [] if children is None else children.replace(' ',
                                                                '').split(',')
        for child in children:
            if child not in tree_index:
                tree_index[child] = Program(child, parent=name)
            else:
                tree_index[child].parent = name
        if not name in tree_index:
            tree_index[name] = Program(name, weight, children)
        else:
            tree_index[name].add_attr(weight, children)

# Get a "random" node
current_node = list(tree_index.keys())[0]
while tree_index[current_node].parent is not None:
    current_node = tree_index[current_node].parent

print("Part I: %s" % (current_node))
(root_path, root_total) = recSumOfWeights(tree_index[current_node])
print("Part II: %d" % (root_path[0][1]))
