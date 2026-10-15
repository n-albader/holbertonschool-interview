#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""
import sys


def print_statistics(total_file_size, status_counts):
    """Prints the accumulated file size and status code counts"""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


def main():
    """Main function to parse log data from stdin"""
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

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) >= 9:
                status_code = parts[-2]
                try:
                    file_size = int(parts[-1])
                    if status_code in status_counts:
                        status_counts[status_code] += 1
                    total_file_size += file_size
                    line_count += 1
                except ValueError:
                    pass

            if line_count == 10:
                print_statistics(total_file_size, status_counts)
                line_count = 0
    except KeyboardInterrupt:
        print_statistics(total_file_size, status_counts)
        raise

    print_statistics(total_file_size, status_counts)


if __name__ == "__main__":
    main()
