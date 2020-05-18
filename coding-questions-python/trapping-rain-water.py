'''
LC: https://www.youtube.com/watch?v=HmBbcDiJapY&t=8s

Approach:
    - note that the water level must reach equilibrium
    - divide and conquer strategy can make this problem easier to solve
    - each building (or index) will have a certain amount of water on top of it
    - if we can sum the amount for every single index, then that would add up the amount of water
    trapped by the entire elevation map

    - but how do we find out the amount of water on top of a single building (or index)
    - at each index, the amount of water stored must be at equilibrium
    - this means that the water at that index must be surrounded by two buildings, one on each side
    - the water, w, on top of an index can be at most the min(tallest building on the left, tallest building on right)
    - but the building at that index of height m takes away m units of water that can be stored on the
    - then, the height at that index would be w - m

    - essentially, at each index, we just need to know the tallest building to the left, max_to_left,
    and tallest building to the right, max_to_right
    - we basically maintain two arrays, max_to_left and max_to_right, where arr[i] = max height to the right/left of i
    - finally, we compute the amount of water accumulated on top of each index and sum them up

Complexity:
    - generating max_to_left, and max_to_right -> O(2N) or O(N)
    - calculating total accumulated water -> O(N)
    - so, the time complexity is O(N)

    - using two auxiliary arrays, each of size len(input_array)
    - so, the space complexity is O(N)

Note: there is O(N) time and O(1) two pointer approach available on leetcode
'''


def trap(height):
    # store the height of the tallest building to the left/right of i
    max_on_left, max_on_right = [0] * len(height), [0] * len(height)
    for i in range(1, len(height)): max_on_left[i] = max(max_on_left[i - 1], height[i - 1])
    for i in range(len(height) - 2, - 1, -1): max_on_right[i] = max(max_on_right[i + 1], height[i + 1])

    # total accumulated water = sum of accumulated water on top of each building
    # water on top of a building = min (max_height_to_left, max_height_to, right), or 0
    accumulated_water = 0
    for i in range(len(height)):
        water_on_top = min(max_on_left[i], max_on_right[i]) - height[i]
        accumulated_water += max(0, water_on_top)

    return accumulated_water

# all leetcode tests pass as of May 05 2020
