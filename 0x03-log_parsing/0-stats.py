#!/usr/bin/python3
"""
log parsing problem
"""
import re
from sys import stdin


if __name__ == '__main__':
    state_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                   403: 0, 404: 0, 405: 0, 500: 0}

    def print_codes(codes, total_size):
        """
        Print file sizes and status codes.
        """
        print(f'File size: {total_size}')
        for k, v in sorted(codes.items()):
            if v != 0:
                print(f'{k}: {v}')

    count, filesize = 0, 0
    lines = []

    try:
        for line in stdin:
            count += 1
            splitted = line.split(' ')
            try:
                code = int(splitted[-2])
                if code in state_codes:
                    state_codes[code] += 1
            except BaseException:
                pass
            try:
                filesize += int(splitted[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print_codes(state_codes, filesize)
        print_codes(state_codes, filesize)
    except BaseException:
        print_codes(state_codes, filesize)
