'''
LC: https://leetcode.com/problems/divide-two-integers/
YouTube (confusing approach, but well-explained): https://www.youtube.com/watch?v=htX69j1jf5U

Approach:
  - usually
    * we take divisor away from dividend as many times as possible and count
  
  - our approach
    * we won't take one instance of divisor (away from the dividend) at a time
    * instead, we will double the divisor as many times as possible before it becomes greater than dividend
      and then we will take it out
    * this process is repeated on the reamining dividend
    
    ex: 10 / 3
    * we can take 3(3*2^0), 6(3*2^1) away from 10 but not 12(2*2^2). So we remove 6 from 10,
      and the remainder dividend is 4
    * we can now take 3(3*2^0) away from 4
    * reamining dividend is 1 (which is > 3) so we stop
'''

def divide(self, dividend, divisor):
  # int min/max will help us catch overflow
  int_min, int_max = -(2**31), (2**31)-1

  # edge case -- overflow
  # dividend is INT_MIN and the divisor is -1. Quotient will be INT_MAX + 1 so overflow
  if dividend == int_min and divisor == -1: return int_max

  # taking the abs values so the division is easier
  a, b  = abs(dividend), abs(divisor)

  # it will track the quotient
  result = 0

  # can we take divisor out of (what's left in) the dividend at least once
  while a - b >= 0:
    # it's the power of 2 we are going to take away, ex: 2^0
    x = 0

    # ex: 10 - (3 << 1 << x)   ->  10 - 6 = 4
    while a - (b << 1 << x) >= 0: x += 1

    # how many times can we double b (divisor) and it will still be less than what's left in the dividend
    result += 1 << x

    # take away from dividend, how many times we've doubled divisor
    a -= b << x

  # check for the minus signs
  return result if ((dividend >= 0) == (divisor >= 0)) else -result
  
# all leetcode tests pass as of 8th Nov 2019
