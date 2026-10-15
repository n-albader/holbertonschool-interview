#!/usr/bin/python3
"""Parse log lines and print statistics"""

import sys
import re


def print_statistics(total_file_size, status_counts):
    """Print the accumulated statistics."""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


def main():
    """Read log lines and calculate statistics"""
    total_file_size = 0
    status_counts = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }
    line_count = 0

    pattern = re.compile(
        r'^\S+ - \[.+\] ".+" (\d+) (\d+)$'
    )

    try:
        for line in sys.stdin:
            line_count += 1
            match = pattern.match(line.strip())

            if match:
                status_code = match.group(1)
                file_size = int(match.group(2))

                total_file_size += file_size

                if status_code in status_counts:
                    status_counts[status_code] += 1

            if line_count % 10 == 0:
                print_statistics(total_file_size, status_counts)

    except KeyboardInterrupt:
        print_statistics(total_file_size, status_counts)
        return

    if line_count % 10 != 0:
        print_statistics(total_file_size, status_counts)


if __name__ == "__main__":
    main()
