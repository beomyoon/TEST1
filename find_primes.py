"""Utility to find and display prime numbers from 1 to 200."""
from __future__ import annotations

from typing import List


def is_prime(number: int) -> bool:
    """Return True if ``number`` is a prime number."""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    limit = int(number ** 0.5) + 1
    for candidate in range(3, limit, 2):
        if number % candidate == 0:
            return False
    return True


def primes_between(start: int, end: int) -> List[int]:
    """Return a list of primes between ``start`` and ``end`` inclusive."""
    return [value for value in range(start, end + 1) if is_prime(value)]


def main() -> None:
    """Print the prime numbers between 1 and 200 inclusive."""
    primes = primes_between(1, 200)
    print(" ".join(str(value) for value in primes))


if __name__ == "__main__":
    main()
