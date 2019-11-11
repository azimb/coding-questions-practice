'''
LC: https://leetcode.com/problems/product-of-array-except-self/

Approach 1:
  - this approach is called left and right product lists
  - instead of dividing the product of all the numbers in the array by the number at a given index to get the corresponding product, 
    we can make use of the product of all the numbers to the left and all the numbers to the right of the index
  - multiplying these two individual products would give us the desired result as well
  
  - for every given index, we will make use of the product of all the numbers to the left of it and multiply it by 
   the product of all the numbers to the right
  - this will give us the product of all the numbers except the one at the given index
 
  - O(3N) time and O(2N) space, so O(N) time and space complexity
 
Approach:
  - for this discussion, the output array does not count towards the space complexity
  - basically, we will be using the output array as one of L or R and we will be constructing the other one on the fly
  
  - O(2N), O(1) time and space
  - so O(N) time and constant space complexity
  - we don't use any additional array for our computations
  - the problem statement mentions that using the answeranswer array doesn't add to the space complexity
'''

'''
# approach 01
# O(N) time and space
def productExceptSelf(self, nums):
  # the left and right arrays as described in the algorithm
  # L[i] contains the product of all the elements to the left
  # R[i] contains the product of all the elements to the right
  left, right = [1] * len(nums), [1] * len(nums)

  # Note: for the element at index '0', there are no elements to the left, so the L[0] would be 1
  # L[i - 1] already contains the product of elements to the left of 'i - 1'
  # Simply multiplying it with nums[i - 1] would give the product of all elements to the left of index 'i'
  for i in range(1, len(nums)): left[i] = left[i-1] * nums[i-1]

  # Note: for the element at index 'length - 1', there are no elements to the right, so the R[length - 1] would be 1
  # R[i + 1] already contains the product of elements to the right of 'i + 1'
  # Simply multiplying it with nums[i + 1] would give the product of all elements to the right of index 'i'
  for i in range(len(nums) - 2, -1, -1): right[i] = right[i+1] * nums[i+1]

  output = [1] * len(nums)
  # for the output array, for each elem - multiple product of all elements to the left and to the right
  for i in range(len(output)): output[i] = left[i] * right[i]

  return output
'''

# approach 02
# O(N) time and O(1) space

def productExceptSelf(self, nums):
  # left[i] contains the product of all the elements to the left
  left = [1] * len(nums)
  for i in range(1, len(nums)): left[i] = left[i-1] * nums[i-1]

  # right tracks the product of all the elements to the right
  right = 1
  for i in range(len(nums) - 1, -1, -1):
    left[i] = left[i] * right
    right *= nums[i]

  return left
  
# all leetcode tests pass as of 11th Nov 2019
