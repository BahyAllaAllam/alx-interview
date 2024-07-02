#!/usr/bin/python3
"""
0x01. Lockboxes 
"""


def canUnlockAll(boxes):
  """
  A function that determines 
  if all the boxes can be opened
  """
  n = len(boxes)
  opened = set([0])
  stack = [0]
  
  if not boxes:
    return False

  while stack:
    box_index = stack.pop()
    for key in boxes[box_index]:
      if key not in opened and key < n:
        opened.add(key)
        stack.append(key)

  return len(opened) == n
