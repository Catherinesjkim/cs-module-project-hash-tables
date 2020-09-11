"""
## Input

This function takes a single filename string as an argument, e.g.

```
robin.txt
```

It should open the file, and work through it to produce the output.

(`robin.txt` is in this directory.)

## Output

1. Output will be first ordered by the number of words, then by the word
(alphabetically).

2. Print a histogram showing the word count for each word, one hash mark
for every occurrence of the word.

3. The hash marks should be left justified two spaces after the longest
word.

4. Case should be ignored, and all output forced to lowercase.

5. Split the strings into words on any whitespace.

6. Ignore each of the following characters:

```
" : ; , . - + = / \ | [ ] { } ( ) * ^ &
```

7. If the input contains no ignored characters, print nothing.

"""
import collections

d = collections.OrderedDict()
with open("robin.txt") as f:
    words = f.read()

words = words.split()

# Print a histogram showing the word count for each word, one hash mark for every occurrence of the word.
for word in words:
    # Ignore each of the following characters:
    # " : ; , . - + = / \ | [ ] { } ( ) * ^ &
    word = word.strip('":;,.-+=/\\|[]{}()*^&!?''')
    # Case should be ignored, and all output forced to lowercase.
    word = word.lower()
    if word in d:
        d[word] = d[word] + '#'
    else:
        d[word] = '#'

# The hash marks should be left justified two spaces after the longest word.
# find longest word
longest_word = ''
for key in d.keys():
    if len(key) > len(longest_word):
        longest_word = key
# Output will be first ordered by the number of words, then by the word (alphabetically).
# get dictionary sorted by values
for w in sorted(d, key=d.get, reverse=False):
    # How do I do this based on the longest word
    print(f'{w:<20} {d[w]}')



"""
Printing: you can print a variable field width in an f-string with nested braces, like so `{x:{y}}` 

d1 = 'a'
d2 = 'ab'
d3 = 'abc'
d4 = 'abcd'

print(f'{d1:>10}')
print(f'{d2:>10}')
print(f'{d3:>10}')
print(f'{d4:>10}')

chr(number): This function converts number to its corresponding ASCII character (# == 35) '{0!a}'.format(35)

def asciiSums(sentence): 
  
    # split words separated by space 
    words = sentence.split(' ') 
  
    # create empty dictionary 
    result = {} 
  
    # calculate sum of ascii values of each word 
    for word in words: 
         currentSum = sum(map(ord,word)) 
  
         # map sum and word into resultant dictionary 
         result[word] = currentSum 
  
    totalSum = 0

"""
