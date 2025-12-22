#!/usr/bin/python3
"""
Log parsing
"""
import sys


def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def main():
    status_codes = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }
    total_size = 0
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()

            try:
                total_size += int(parts[-1])
                code = parts[-2]
                if code in status_codes:
                    status_codes[code] += 1
            except (IndexError, ValueError):
                pass

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        pass
    finally:
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
