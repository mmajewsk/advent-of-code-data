#!/usr/bin/env python

import time
import datetime

import argparse
from .get import get_data
from .exceptions import PuzzleLockedError

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[31m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "day",
        type=int,
    )
    parser.add_argument("--year", type=int, default=None)
    args = parser.parse_args()
    while True:
        try:
            new_day_data= get_data(day=args.day, year=args.year)

        except PuzzleLockedError:
            pass
            print(bcolors.BOLD, datetime.datetime.now(), bcolors.ENDC)
            time.sleep(0.35)
            continue

        filename = 'p{}.in'.format(args.day)
        with open(filename,'w') as f:
            f.write(new_day_data)
        beg, mid, end = new_day_data[:50], new_day_data[50:-50], new_day_data[-50:]
        beg_msg = bcolors.RED + beg
        end_msg = bcolors.RED + end + bcolors.ENDC
        mid_msg = "{}[... {} chars ...]{}".format(bcolors.ENDC, len(mid), bcolors.ENDC)
        msg = "{}{}{}".format(beg_msg, mid_msg, end_msg)
        print(msg)
        break

    print("Creation start")
