'''
LC: https://leetcode.com/problems/friends-of-appropriate-ages/

Approach:
  - instead of processing all 20000 people, we can process pairs of (age, count) representing how many people are that age
  - since there are only 120 possible ages, this is a much faster loop
  
  - for each pair (ageA, countA), (ageB, countB), if the conditions are satisfied with respect to age, 
    then countA * countB pairs of people made friend requests
  - be careful about overcounting when ageA == ageB
  
Time and space complexity:
  - time -- O(A^2 + N) where A = number of unique ages, and N = number of people
  - space -- O(A) space used to count each age
'''

def numFriendRequests(self, ages):
  # count how many time each unique age appears
  ages_count = Counter(ages)
  # count the number of possible friend requests
  friend_requests = 0
  
  # look at all possible (age, count) pairs
  for age_one in ages_count:
    for age_two in ages_count:
      # if the conditions don't meet, skip this pair
      if (age_two <= 0.5 * age_one + 7) or age_two > age_one: continue
      # take the cartesian product, as we are looking at groups (of ages) instead of individual ages
      friend_requests += ages_count[age_one] * ages_count[age_two]
      # overcounting! when age_one == age_two as a person cannot friend request themself
      if age_one == age_two: friend_requests -= ages_count[age_one]
      
  return friend_requests
