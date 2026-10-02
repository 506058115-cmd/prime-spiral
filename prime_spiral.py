#!/usr/bin/env python3
"""Draw prime positions in a square Ulam spiral."""

import argparse
from math import isqrt


MAX_SIZE = 101


def main():
    parser = argparse.ArgumentParser(description="Draw an ASCII Ulam spiral with prime values marked.")
    parser.add_argument("--size", type=int, default=21, help="odd grid width from 3 to 101 (default: 21)")
    args = parser.parse_args()
    if args.size < 3 or args.size > MAX_SIZE or args.size % 2 == 0:
        parser.error(f"size must be an odd number from 3 to {MAX_SIZE}")

    total = args.size * args.size
    prime = [True] * (total + 1)
    prime[0] = prime[1] = False
    for factor in range(2, isqrt(total) + 1):
        if prime[factor]:
            for multiple in range(factor * factor, total + 1, factor):
                prime[multiple] = False

    grid = [[0] * args.size for _ in range(args.size)]
    middle = args.size // 2
    grid[middle][middle] = 1
    x = y = turn = 0
    value = 1
    length = 1
    directions = ((1, 0), (0, -1), (-1, 0), (0, 1))
    while value < total:
        for _pair in range(2):
            dx, dy = directions[turn % 4]
            for _step in range(length):
                if value == total:
                    break
                x += dx
                y += dy
                value += 1
                grid[middle - y][middle + x] = value
            turn += 1
            if value == total:
                break
        length += 1

    print(f"Ulam spiral {args.size}×{args.size}: # prime, . composite or 1")
    for row in grid:
        print("".join("#" if prime[number] else "." for number in row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
