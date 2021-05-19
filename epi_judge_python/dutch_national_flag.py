import functools
from collections import defaultdict
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition_count_sort_impl(pivot_index: int, A: List[int]) -> None:
    counts = defaultdict(lambda: 0)
    for val in A:
        counts[val] += 1

    pivot_val = A[pivot_index]

    curr_idx = 0
    # Add all vals less than pivot val
    for val in range(0, pivot_val):
        for val_instance in range(counts[val]):
            A[curr_idx] = val
            curr_idx += 1

    for val_instance in range(counts[pivot_val]):
        A[curr_idx] = pivot_val
        curr_idx += 1

    for val in range(pivot_val + 1, 3):
        for val_instance in range(counts[val]):
            A[curr_idx] = val
            curr_idx += 1

    return

def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot_val = A[pivot_index]
    more_cnt, less_cnt = 0, 0

    for val in A:
        if val < pivot_val:
            less_cnt += 1
        elif val > pivot_val:
            more_cnt += 1

    # first pass, do a quicksort-esque algo to partition less and greater
    low_idx, high_idx = 0, len(A) - 1

    while low_idx < high_idx:
        # Move pointers until we have a proper switch
        while low_idx < high_idx and A[low_idx] <= pivot_val:
            low_idx += 1

        while low_idx < high_idx and A[high_idx] >= pivot_val:
            high_idx -= 1

        if low_idx < high_idx:
            A[low_idx], A[high_idx] = A[high_idx], A[low_idx]
            low_idx += 1
            high_idx -= 1

    # second pass, move all pivot val values into proper place
    pivot_reorder_idx = less_cnt

    low_idx, high_idx = 0, len(A) - 1
    for i in range(pivot_reorder_idx, len(A) - more_cnt):
        if A[i] < pivot_val:
            while A[low_idx] < pivot_val:
                low_idx += 1
            A[i], A[low_idx] = A[low_idx], A[i]
        elif A[i] > pivot_val:
            while A[high_idx] > pivot_val:
                high_idx -= 1
            A[i], A[high_idx] = A[high_idx], A[i]
        else:
            continue

    return


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))