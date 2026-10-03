#!/usr/bin/python3
"""Defines a function to determine if all boxes can be unlocked."""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, otherwise False."""
    opened = {0}
    stack = [0]

    while stack:
        box = stack.pop()

        for key in boxes[box]:
            if key < len(boxes) and key not in opened:
                opened.add(key)
                stack.append(key)

    return len(opened) == len(boxes)
