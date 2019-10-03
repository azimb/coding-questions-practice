'''
GfG: https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
YouTube: https://www.youtube.com/watch?v=xCbYmUPvc2Q&t=26s
'''

def knapSack(cap, W, V, n):
	# 2D array for dyn.prog -- bottom up approach
    dp_arr = [[0 for x in range(cap+1)] for y in range(n+1)]

    # max value with no items is always 0
    # max value with no capacity is always 0
    
    for row in range(1, len(dp_arr)):
        for col in range(1, len(dp_arr[row])):
            # don’t take the item
            # same weight, just remove the item
            val_one = dp_arr[row-1][col]

            # take the item
            # reduced weight, based on the items weight
            val_two = 0 if col <  W[row-1] else V[row - 1] + dp_arr[row-1][col - W[row-1] ]

            # maximize the amount of value of the items in the bag
            dp_arr[row][col] = max(val_one, val_two)

    # get the global optimal solution
    return dp_arr[-1][-1]

# Driver program to test above function 
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print(knapSack(W, wt, val, n)) # must print 220
