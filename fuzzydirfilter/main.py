import argparse
import os
import sys
from operator import itemgetter

from fuzzywuzzy import fuzz

DEFAULT_THRESHOLD = 70


def fuzzydirfilter_main():
    default_threshold = os.getenv('FUZZYDIRFILTER_THRESHOLD', DEFAULT_THRESHOLD)

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--sort', action='store_true')
    parser.add_argument('--threshold', type=int, default=default_threshold)
    parser.add_argument('search_string', type=str)
    parser.add_argument('file', nargs='*', type=argparse.FileType('r'), default=[sys.stdin])

    args = parser.parse_args()

    entries = []
    for file in args.file:
        for line in file:
            directory_name = line.rstrip().split("/")[-1]
            score = fuzz.partial_ratio(args.search_string, directory_name)
            if score >= args.threshold:
                if args.sort:
                    entries.append((score, line))
                else:
                    print(line, end='')

    if args.sort:
        for e in sorted(entries, key=itemgetter(0)):
            print(e[1], end='')
