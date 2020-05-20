"""
LC: https://leetcode.com/problems/sort-array-by-parity/

Approach:
    - we are essentially creating two partitions (for odd and even numbers)
    - we use two pointers a,b and the invariant is that:
    * all elements before the a pointer are even numbers
    * all elements after the b pointer are odd numbers

    - the strategy essentially is to iterate over the array and "move" all odd numbers to the end

Complexity Analysis:
    - O(N) time and O(1) space complexity
"""


def sort_array_by_parity(A):
    # two pointers -- all elems before "even" are even, and all elements after "odd" are odd
    even, odd = 0, len(A) - 1

    # make two partitions
    while even < odd:
        # if even, don't swap
        if A[even] % 2 == 0:
            even += 1

        # if even, put it to the end
        else:
            A[even], A[odd] = A[odd], A[even]
            odd -= 1

    # we did this in place, so return the same array
    return A

# all leetcode tests pass as of May 18 2020
