#!/usr/bin/python3
"""Parse log lines and print accumulated statistics"""

import sys
import re


def print_stats(total_size, status_codes):
    """Print the accumulated log statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


def main():
    """Read logs from stdin and compute statistics"""
    total_size = 0
    status_codes = {}
    valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    line_count = 0

    pattern = re.compile(
        r'^\S+ - \[.+\] ".+" (\d+) (\d+)$'
    )

    try:
        for line in sys.stdin:
            line_count += 1
            match = pattern.match(line.strip())

            if match:
                status = int(match.group(1))
                size = int(match.group(2))

                if status in valid_codes:
                    total_size += size
                    status_codes[status] = (
                        status_codes.get(status, 0) + 1
                    )

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

        if line_count % 10 != 0 or line_count == 0:
            print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
