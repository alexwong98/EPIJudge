from test_framework import generic_test


def divide(x: int, y: int) -> int:
    print(x, y)
    if y > x:
        return 0

    num_shifts = 1

    while (y << num_shifts) <= x and (y << num_shifts > y << (num_shifts - 1)):
        num_shifts += 1

    quotient = 1 << (num_shifts - 1)

    return quotient + divide(x - (y << (num_shifts - 1)), y)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
