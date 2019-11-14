'''
Find the Celebrity (Premium)

Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.
Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).
You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

Approach:
The first loop is to find the candidate. In detail, suppose the candidate after the first for loop is person k, 
it means 0 to k-1 cannot be the celebrity, because they know a previous or current candidate. Also, since k knows 
no one between k+1 and n-1, k+1 to n-1 can not be the celebrity either. Therefore, k is the only possible celebrity, 
if there exists one.

The remaining job is to check if k indeed does not know any other persons and all other persons know k.
We don't need to check if k knows k+1 to n-1 in the second loop, because the first loop has already done that.
'''

def findCelebrity(self, n):
  candidate = 0

  for i in range(n):
    if knows(candidate, i): candidate = i

  for i in range(n):
    if i < candidate and (knows(candidate, i) or not knows(i, candidate)): return -1
    if i > candidate and not knows(i, candidate): return -1

  return candidate
  
# all leetcode tests pass as of 13th Nov 2019
