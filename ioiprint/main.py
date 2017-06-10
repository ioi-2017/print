#! /usr/bin/env python3
import sys

from ioiprint.print import print_file


def print_usage_and_exit():
    print("Usage")
    exit(1)


def main():
    if len(sys.argv) < 2:
        print_usage_and_exit()
    command = sys.argv[1]
    if command == 'translation':
        if len(sys.argv) < 6:
            print_usage_and_exit()
        file_path = sys.argv[2]
        country_code = sys.argv[3]
        country_name = sys.argv[4]
        count = int(sys.argv[5])
        # TODO
    elif command == 'cms':
        if len(sys.argv) < 4:
            print_usage_and_exit()
        request_message = sys.argv[2]
        ip = sys.argv[3]
        # TODO
    elif command == 'contestant':
        if len(sys.argv) < 4:
            print_usage_and_exit()
        file_path = sys.argv[2]
        ip = sys.argv[3]
        # TODO
    elif command == 'mass':
        if len(sys.argv) < 5:
            print_usage_and_exit()
        file_path = sys.argv[2]
        printer = sys.argv[3]
        count = int(sys.argv[4])
        for _ in range(count):
            print_file(file_path, printer)
    else:
        print_usage_and_exit()

if __name__ == '__main__':
    main()
