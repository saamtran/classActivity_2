import pytest

def palindrome(s):
    for x in range(0, int((len(s))/2)):
        if s[x] != s[len(s)-x-1]:
            return False
        return True

def testOne():
    text = "racecar"
    status = palindrome(text)
    assert status == True

def testTwo():
    text = "chicken"
    status = palindrome(text)
    assert status == False
    

def testThree():
    text = " "
    status = palindrome(text)
    assert status == True

