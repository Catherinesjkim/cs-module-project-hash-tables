"""
# No Duplicates

Input: a string of words separated by spaces. Only the letters `a`-`z`
are utilized.

Output: the string in the same order, but with subsequent duplicate
words removed.

There must be no extra spaces at the end of your returned string.

The solution must be `O(n)`

"""
from collections import Counter

def no_dups(string):
    # split input string separated by space
    string = string.split(" ")

    # joins two adjacent elements in iterable way
    for i in range(0, len(string)):
        string[i] = "".join(string[i])

    # now create dictionary using counter method
    # which will have strings as key and their frequencies as value
    UniqW = Counter(string)

    # joins two adjacent elements in iterable way
    s = " ".join(UniqW.keys())
    print(s)


# Driver program
if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
