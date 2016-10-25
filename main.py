#!/usr/bin/env python3

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

def display_block(block):
    for row in block:
        print("".join("X" if i else "." for i in row))
    print()

def sum_of_block(block):
    return sum(sum(row) for row in block)

def block_to_tree(block):
    if len(block) == len(block[0]) == 1:
        return block[0][0]
    # Clockwise from top-right.
    return list(map(
        block_to_tree,
        (top_right(block), bottom_right(block),
         bottom_left(block), top_left(block))
    ))

def tree_to_block(tree):
    if type(tree) == int:
        return [[tree]]
    flattened_tree = list(map(tree_to_block, tree))

    top_tuples = zip(flattened_tree[3], flattened_tree[0])
    bottom_tuples = zip(flattened_tree[2], flattened_tree[1])

    return [a + b for a, b in top_tuples] + \
        [a + b for a, b in bottom_tuples]

## __main__

with open(filename, 'r') as f:
    block = [[int(c) for c in row.strip()] for row in f]

display_block(tree_to_block(block_to_tree(block)))
