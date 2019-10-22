'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
    n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines,
    which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.

Leetcode: https://leetcode.com/problems/container-with-most-water/

Approach:
    - the area formed between the two lines will always be limited by the shorter line
    - a two pointer approach is used, one starting at the beginning of the list, and the orther starting at the end
    - at each step, we find the area formed by the two lines and update max_area if required
    - * and then, move the pointer pointing to the shorter line inward
    (this is because, if we  try to move the pointer at the longer line inwards, we won't gain any increase in area,
    since it is limited by the shorter line. But moving the shorter line's pointer could turn out to be beneficial,
    as per the same argument, despite the reduction in the width. This is done since a relatively longer line obtained
    by moving the shorter line's pointer might overcome the reduction in area caused by the width reduction)

Time complexity:
    - single pass
    - so O(N) or linear

Space complexity:
    - O(1) or constant
'''

def max_area(height):
    # variable to keep a track of the maximum area
    max_area = 0
    # area will be measured b/w these two boundaries
    left, right = 0, len(height) - 1

    # until the two pointers meet
    while left < right:
        # calculate the area, and update max_area is required
        max_area = max(max_area, min(height[left], height[right]) * (right - left))
        # move the pointer pointing to the shorter line inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

# all leetcode tests pass
