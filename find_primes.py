"""
find_primes.py
--------------
Identify prime numbers from a given list of integers.

Usage examples:
    # Pass numbers directly as CLI arguments
    python3 find_primes.py --numbers 2 3 4 5 10 11 13 20 29

    # Read numbers from a file (one or more per line, whitespace/comma separated)
    python3 find_primes.py --file numbers.txt

If neither --numbers nor --file is given, a built-in default list is used.
"""

import argparse
import math
import re
import sys


def is_prime(n: int) -> bool:
    """Return True if n is a prime number, else False."""
    if not isinstance(n, int):
        return False
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Only check odd divisors up to sqrt(n)
    limit = int(math.isqrt(n))
    for divisor in range(3, limit + 1, 2):
        if n % divisor == 0:
            return False
    return True


def find_primes(numbers):
    """Return a list of primes from the input iterable, preserving order."""
    return [num for num in numbers if is_prime(num)]


def parse_numbers_from_file(file_path):
    """Read integers from a file. Accepts whitespace or comma separated values."""
    numbers = []
    with open(file_path, "r") as f:
        content = f.read()
    # Split on commas, whitespace, or newlines
    tokens = re.split(r"[\s,]+", content.strip())
    for token in tokens:
        if not token:
            continue
        try:
            numbers.append(int(token))
        except ValueError:
            print(f"Warning: skipping non-integer value '{token}'", file=sys.stderr)
    return numbers


def parse_args():
    parser = argparse.ArgumentParser(
        description="Identify prime numbers from a given list of integers."
    )
    parser.add_argument(
        "--numbers",
        type=int,
        nargs="+",
        help="One or more integers, space separated (e.g. --numbers 2 3 4 5 11)."
    )
    parser.add_argument(
        "--file",
        type=str,
        help="Path to a file containing integers (whitespace or comma separated)."
    )
    return parser.parse_args()


def main():
    args = parse_args()

    if args.numbers:
        numbers = args.numbers
    elif args.file:
        numbers = parse_numbers_from_file(args.file)
    else:
        # Default demo list when no input is supplied
        numbers = [1, 2, 3, 4, 5, 10, 11, 13, 15, 17, 19, 20, 23, 25, 29, 97, 100]
        print("No input provided — using default demo list.")

    print(f"Input numbers : {numbers}")
    primes = find_primes(numbers)
    print(f"Prime numbers : {primes}")
    print(f"Count of primes: {len(primes)}")


if __name__ == "__main__":
    main()
