import math

from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    if x == 0:
        return '0'

    s = []
    if x < 0:
        s.append("-")
        x *= -1

    curr_pow = int(math.log10(x))
    while curr_pow >= 0:
        digit = x // (pow(10, curr_pow))
        s.append(str(digit))
        x -= digit * pow(10, curr_pow)
        curr_pow -= 1

    return ''.join(s)


def string_to_int(s: str) -> int:
    if not s:
        raise Exception("empty string")

    if s[0] == "+" or s[0] == "-":
        start_idx = 1
    else:
        start_idx = 0

    val = 0

    for i in range(start_idx, len(s)):
        curr_char = s[i]
        val += (ord(curr_char) - ord('0')) * (pow(10, len(s) - i - 1))

    if s[0] == '-':
        return val * -1

    return val


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        print("a", string_to_int(s))
        print("b", x)
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
