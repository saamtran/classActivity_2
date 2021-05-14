def palindrome(s):
    for x in range(0, int((len(s))/2)):
        if s[x] != s[len(s)-x-1]:
            return False
        return True

