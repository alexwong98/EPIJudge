from typing import List

from test_framework import generic_test, test_utils


def generate_power_set(input_set: List[int]) -> List[List[int]]:
    # TODO - you fill in here.
    soln = []
    _generate_power_set(input_set, 0, [], soln)
    return soln


# Time: O(|S|2^|S|) bc 2^|S| sets, each required to go down the entire length of |S| to get value
# Space: O(|S|) bc we store only one powerset at a time, recursion only goes up to |S| length (stack height)
def _generate_power_set(elems: list, curr_idx: int, curr_ps: list, soln: list):
    if curr_idx == len(elems):
        soln.append(curr_ps.copy())
        return

    curr_ps.append(elems[curr_idx])
    _generate_power_set(elems, curr_idx + 1, curr_ps, soln)
    curr_ps.pop()
    _generate_power_set(elems, curr_idx + 1, curr_ps, soln)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
