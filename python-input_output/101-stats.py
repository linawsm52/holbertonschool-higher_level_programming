#!/usr/bin/python3
"""
Log parsing
"""
import sys

status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

total_size = 0
line_count = 0


def print_stats():
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


try:
    for line in sys.stdin:
        parts = line.split()
        try:
            total_size += int(parts[-1])
            if parts[-2] in status_codes:
                status_codes[parts[-2]] += 1
        except (IndexError, ValueError):
            pass

        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise
