#!/usr/bin/env python3
import argparse
import os
import random
import re
import sys
from pathlib import Path


def split(phrase: str) -> list[str]:
    return re.split(r"[ ,]", phrase)


def read_random_words(filename: os.PathLike) -> str:
    """read a file and return a list of words."""
    # get number of lines in file
    num_lines_in_file = sum(1 for _ in Path(filename).open())
    longest_line = max(Path(filename).open(), key=len)
    MIN_LEN = 30

    if len(longest_line) < MIN_LEN:
        print(
            f"Longest line is {len(longest_line)} characters, which is too short to investigate the claim effectively. Please use another file with at least {MIN_LEN} characters in a line"
        )
        sys.exit()

    line_num = random.randrange(num_lines_in_file)
    with Path(filename).open() as f:
        for _ in range(line_num):
            line = f.readline()
    line = line.rstrip()  # avoid trailing newline
    # if too short, retry
    return line if len(line) >= MIN_LEN else read_random_words(filename)


def scramble(word: str) -> str:
    """will fail on apostrophes."""
    if len(word) <= 3:  # avoids tuple unpacking error
        return word
    first, *middle, last = word
    random.shuffle(middle)
    return "".join([first, *middle, last])


def scramble_all(phrase: str) -> str:
    return " ".join(scramble(word) for word in split(phrase))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--file", help="file to read", type=Path, default=Path("input.txt")
    )
    args = parser.parse_args()

    rand_line = read_random_words(args.file)
    print(scramble_all(rand_line))
    print(rand_line)
