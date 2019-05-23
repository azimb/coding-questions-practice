'''
Given a string, find the longest substring which is palindrome. For example, if the given string is “forgeeksskeegfor”, the output should be “geeksskeeg”.

Suggested approach:
Dynamic programming -- maintain a 2D array that stores a boolean at each index
	- if inex i,j is true, that means that the substring from index i to j (inclusive) is a palindrome
This way, we can use pre-computed results of smaller lengths to find the current result for the (current) lengths
'''

longestLength = -1
longestSubstring = ""

def init():
	print(dummy)

def longestPalindromicSubstring(str):
	
	cache = []
	
	#init 2D array with False at all indices
	for i in range(len(str)):
		cache.append([])
		for j in range(len(str)):
			cache[i].append(False)

	#set the values for substrings of length 1 and 2
	for i in range(len(cache)):
		cache[i][i] = True
		setSubstring(str, i, i)
		
		if (i != len(str)-1) and (str[i] == str[i+1]):
			cache[i][i+1] = True
			setSubstring(str, i, i+1)
			
	#set the values for substrings of length greater than 2
	k = 0
	for i in range(2, len(str)):
		for j in range(len(str) - i):
			k = i+j
			if str[j] == str[k] and cache[j+1][k-1] == True:
				cache[j][k] = True
				setSubstring(str, j, k)
	return longestSubstring

def getSubstring(str, i, j):
	return str[i:j+1]
		

def setSubstring(str, i, j):
	global longestLength
	global longestSubstring
	substring = getSubstring(str, i, j)
	if len(substring) > longestLength:
		longestLength = len(substring)
		longestSubstring = substring

result = longestPalindromicSubstring("jkahhakkkracecarxoxo")
print(result)


#TODO: check why global keyword is needed on ln 51, 52
#TODO: estimate big O runtime complexity