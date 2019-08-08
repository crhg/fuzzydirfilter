import argparse
import os
import sys
from operator import itemgetter

from fuzzywuzzy import fuzz

DEFAULT_THRESHOLD = 70


def fuzzydirfilter_main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--sort', action='store_true')
    parser.add_argument('--threshold', type=int, default=None)
    parser.add_argument('search_string', type=str)
    parser.add_argument('file', nargs='*', type=argparse.FileType('r'), default=[sys.stdin])

    args = parser.parse_args()

    if args.sort:
        do_sort(args.search_string, args.file)
    else:
        threshold = args.threshold
        if threshold is None:
            threshold = os.getenv('FUZZYDIRFILTER_THRESHOLD', DEFAULT_THRESHOLD)

        do_filter(args, args.file, threshold)


def do_filter(search_string, files, threshold):
    for file in files:
        for line in file:
            directory_name = line.rstrip().split("/")[-1]
            score = fuzz.partial_ratio(search_string, directory_name)
            if score >= threshold:
                print(line, end='')


def do_sort(search_string, files):
    entries = []
    for file in files:
        for line in file:
            directory_name = line.rstrip().split("/")[-1]
            score = fuzz.ratio(search_string, directory_name)
            entries.append((score, line))

    entries.reverse()
    for e in sorted(entries, key=itemgetter(0), reverse=True):
        print(e[1], end='')

