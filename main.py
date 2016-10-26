#!/usr/bin/env python3
from numbers import Number

filename = 'data/catandmouse'
resolution = 16

def top_left(block):
    height = len(block)
    width = len(block[0])

    return [row[:width//2] for row in block[:height//2]]

def top_right(block):
    height = len(block)
    width = len(block[0])

    return [row[width//2:] for row in block[:height//2]]

def bottom_left(block):
    height = len(block)
    width = len(block[0])

    return [row[:width//2] for row in block[height//2:]]

def bottom_right(block):
    height = len(block)
    width = len(block[0])

    return [row[width//2:] for row in block[height//2:]]

#grays = ".:-=+*#%@"
grays = ".'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def display_block(block):
    for row in block:
        print("".join(grays[int(i*(len(grays)-1))] for i in row))
    print("")

def sum_of_block(block):
    return sum(sum(row) for row in block)

CORNERS = (top_right, bottom_right, bottom_left, top_left)

def block_to_tree(block):
    if len(block) == len(block[0]) == 1:
        return block[0][0]
    # Clockwise from top-right.
    node = [block_to_tree(f(block)) for f in CORNERS]
    if all(isinstance(n, Number) and n == node[0] for n in node):
        return node[0]
    return node

def tree_to_block(tree, resolution):
    if isinstance(tree, Number):
        expand = int(2**(resolution))
        return [[tree]*expand]*expand
    if resolution == 0:
        return [[approx_tree_color(tree)]]
    flattened_tree = [tree_to_block(n, resolution-1) for n in tree]

    top_tuples = zip(flattened_tree[3], flattened_tree[0])
    bottom_tuples = zip(flattened_tree[2], flattened_tree[1])

    return [a + b for a, b in top_tuples] + \
        [a + b for a, b in bottom_tuples]

def approx_tree_color(tree):
    if isinstance(tree, Number):
        return tree
    return sum(map(approx_tree_color, tree)) / 4.0

def tree_at_zoom(tree, level):
    if level == 0:
        return approx_tree_color(tree)
    if isinstance(tree, Number):
        return [tree_at_zoom(tree, level-1)]*4
    return (tree_at_zoom(t, level - 1) for t in tree)

def display_tree(tree, resolution):
    display_block(tree_to_block(tree, resolution))


if __name__ == "__main__":
    with open(filename, 'r') as f:
        block = [[int(c) for c in row.strip()] for row in f]

    tree = block_to_tree(block)

    for i in range(0, 5):
        for j in range(i, 6):
            display_tree(tree_at_zoom(tree, i), j)
