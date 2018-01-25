import argparse
import os
import sys

from fuzzywuzzy import fuzz

DEFAULT_THRESHOLD = 70


def fuzzydirfilter_main():
    default_threshold = os.getenv('FUZZYDIRFILTER_THRESHOLD', DEFAULT_THRESHOLD)

    parser = argparse.ArgumentParser()
    parser.add_argument('--threshold', type=int, default=default_threshold)
    parser.add_argument('search_string', type=str)
    parser.add_argument('file', nargs='*', type=argparse.FileType('r'), default=[sys.stdin])

    args = parser.parse_args()

    for file in args.file:
        for line in file:
            directory_name = line.rstrip().split("/")[-1]
            if fuzz.partial_ratio(args.search_string, directory_name) >= args.threshold:
                print(line, end='')
