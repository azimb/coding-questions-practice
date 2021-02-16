'''
Unique Binary Search Trees
LC: https://leetcode.com/problems/unique-binary-search-trees/

Also known as the nth Catalan number.

g(n) = f(i,n) where i = 1..n (inclusive)
and f(i,n) = g(i-1) * g(n-i)

We take the cartesian product because we want to look at all n possibilities for i (or the root).

# TODO: time and space complexity analysis
'''

def numTrees(self, n):
  return self.g(n, {})

def g(self, n, cache):
  # is this a base case or is this subprob already looked at?
  if n == 0 or n == 1: return 1
  elif n in cache: return cache[n]
  
  # make each n possibility as the root and get f(i,n)
  sum = 0
  for i in range(1, n+1): sum += self.f(i, n, cache)
  cache[n] = sum
  return sum

def f(self, i, n, cache):
  '''
  i is fixed as the root
  left subtree can be anything up to but including i
  right subtree can be anything after i, upto n
  we take a cartesian product as for each left subtree, we can have multiple right subtrees
  and vice versa
  '''
  return self.g(i-1, cache)*self.g(n-i, cache)
  
  # all leetcode tests pass as of 12th Oct 2019
