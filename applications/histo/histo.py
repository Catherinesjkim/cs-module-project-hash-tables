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
# Open the file in read mode
text = open("robin.txt", "r")

# Create an empty dictionary
d = dict()

# Loop through each line of the file
for line in text:
	# Remove the leading spaces and newline character
	line = line.strip()

	# Convert the characters in line to lower case to avoid case mismatch
	line = line.lower()

	# split the line into words
	words = line.split(" ")

	# ignore special characters
	separators = '":;,.-+=/\|[]{}()*^&'

	# Compute the number of times each word occurs
	# Iterate over each word in line
	# Output a list of word count pairs sorted from highest to lowest count
	for word in words:
		# Check if the word is already in dictionary
		# Clean punctuation
		word = word.strip(separators)

		if word in d:
			# increment count of word by 1
			d[word] = d[word] + 1
		else:
			# Add the word to dictionary with count 1
			d[word] = 1

	# Reverse the key and values so they can be sorted using tuples.
	# word_freq = []
	# for key, value in d.items():
	# 	word_freq.append((value, key))

	# Sort from highest to lowest
	# word_freq.sort(reverse=True)
	# print(word_freq)

# Print the contents of dictionary
for key in list(d.keys()):
	print(key, ":", d[key])


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
