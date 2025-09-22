"""Tests for the ``find_primes`` utility."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

# Ensure the project root is importable when tests are run from subdirectories.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import find_primes

EXPECTED_PRIMES = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113,
    127,
    131,
    137,
    139,
    149,
    151,
    157,
    163,
    167,
    173,
    179,
    181,
    191,
    193,
    197,
    199,
]


def test_primes_between_returns_expected_values() -> None:
    """The helper should return all primes between the bounds."""
    assert find_primes.primes_between(1, 200) == EXPECTED_PRIMES


def test_script_outputs_expected_primes() -> None:
    """The module should print the prime numbers when executed."""
    result = subprocess.run(
        [sys.executable, "find_primes.py"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert result.stdout.strip() == " ".join(str(value) for value in EXPECTED_PRIMES)
