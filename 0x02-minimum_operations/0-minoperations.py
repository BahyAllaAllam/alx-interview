#!/usr/bin/python3
"""
Script that computes a minimum operations
needed in a CopyAll - Paste task
"""


def minOperations(n):
    """
    Method for compute the minimum number
    of operations for task Copy All and Paste
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2
    
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    
    return operations
