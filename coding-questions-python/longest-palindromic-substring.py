'''
Given a string, find the longest substring which is palindrome. For example, if the given string is “forgeeksskeegfor”, the output should be “geeksskeeg”.

Suggested approach:
Dynamic programming -- maintain a 2D array that stores a boolean at each index
	- if inex i,j is true, that means that the substring from index i to j (inclusive) is a palindrome
This way, we can use pre-computed results of smaller lengths to find the current result for the (current) lengths
'''

def longestPalindromicSubstring(str):
	longest_palindromic_substring = "";
	length_of_longest = 0;
	
	cache = []
	
	#init 2D array with False at all indices
	for i in range(len(str)):
		cache.append([])
		for j in range(len(str)):
			cache[i].append(False)

	#set the values for substrings of length 1 and 2
	for i in range(len(cache)):
		cache[i][i] = True
		
		if (i != len(str)-1) and (str[i] == str[i+1]):
			cache[i][i+1] = True
			
	#set the values for substrings of length greater than 2

	#return cache

def getSubstring(string, i, j):
	return "";


#result = longestPalindromicSubstring("llolk")
#print(result)
	
'''	
"llolk"
True True False False False
False True False False False
False False True False False
False False False True False
False False False False True
'''