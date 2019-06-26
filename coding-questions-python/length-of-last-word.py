def lengthOfLastWord(self, s):
    # approach 1
    # arr = s.split()
    # return 0 if len(arr) is 0 else len(arr[len(arr)-1])

    # approach 2
    s = s.strip()
    for i in range(len(s) - 1, -1, -1):
        if s[i] == " ":
            return len(s) - 1 - i
    return len(s) if (len(s) is not 0) else 0