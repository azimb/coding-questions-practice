'''
LC: https://leetcode.com/problems/powx-n/

Approach:
	- the idea is to halve n in each recursive call, in order to acheive logarithmic runtime complexity
	- the trick here is that x*n is the same as (x^2) * (n/2)

Complexity analysis:
	- we will divide n by 2 in each call, then total log(n) recursive calls
	- so the runtime complexity is O(log(n))
	
	- recursive calls will use the stack space, and at most log(n) recursive calls
	- so the space complexity is O(log(n))

Inspired by: https://leetcode.com/problems/powx-n/discuss/19560/Shortest-Python-Guaranteed
'''

 def myPow(x, n):
	# base case
	if n == 0: return 1
	# handling negative exponent
	if n < 0: return myPow(1/x, -n)
	# handing both odd and even cases:
	#    odd: x^n = x * (x^2) * (n/2)
	#    even: x^n =    (x^2) * (n/2)
	return myPow(x**2, n/2) if (n%2 == 0) else x * myPow(x**2, n/2)
	
# all leetcode tests pass as of 25th April 2020