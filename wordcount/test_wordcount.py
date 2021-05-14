import pytest

def wordCount(s):
    newList = s.split()
    
    numWords = len(newList)
    return numWords


def testOne():
    text = "i am homeless"
    num = wordCount(text)
    assert num == 3


def testTwo():
    text = "hello, my name is sam"
    num = wordCount(text)
    assert num == 5


def testThree():
    text = "?? !!     5"
    num = wordCount(text)
    assert num == 3