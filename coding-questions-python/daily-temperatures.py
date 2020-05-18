'''
LC: https://leetcode.com/problems/daily-temperatures/

Approach:
    - we will use a decrement stack
    - for each temperature, we check whether the top of stack is smaller than the current element
    - if it is, the current temperature is the temperature that is the first bigger temperature than that elem

    - we also push the current elem to the stack, so that we will (potentially) find the next bigger temperature
    for the current temperature

Complexity analysis:
    - O(N) time and O(N) space
'''

def dailyTemperatures(T):
    # the resultant array
    ans = [0 for _ in range(len(T))]
    # stack to track the temperatures that we haven't found the answer for
    stack = []

    for i in range(len(T)):
        temp = T[i]
        # update the answer for all temperatures we have seen so far, which are smaller than the current temperature
        while stack and stack[-1][0] < temp:
            (_, index) = stack.pop()
            ans[index] = i - index

        # append the current temperature to the stack, it's answer will be found in the coming iterations
        stack.append((temp, i))

    return ans

# all leetcode tests pass as of May 15 2020
