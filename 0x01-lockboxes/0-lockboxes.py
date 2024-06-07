#!/usr/bin/python3
"""
Lockboxes module
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Parameters:
    boxes (list of lists): List of boxes with keys to other boxes

    Returns:
    bool: True if all boxes can be opened, False otherwise
    """
    n = len(boxes)
    unlocked = set()
    keys = [0]

    while keys:
        box = keys.pop()
        if box not in unlocked:
            unlocked.add(box)
            for key in boxes[box]:
                if key < n and key not in unlocked:
                    keys.append(key)

    return len(unlocked) == n
