"""
# Count the words in an input string

## Input

1. This function takes a single string as an argument: Done
```
Hello, my cat. And my cat doesn't say "hello" back.
```

## Output

2. It returns a dictionary of words and their counts: Done
```
{'hello': 2, 'my': 2, 'cat': 2, 'and': 1, "doesn't": 1, 'say': 1, 'back': 1}
```

3. Case should be ignored. Output keys must be lowercase: Done

4. Key order in the dictionary doesn't matter: Done

5. Split the strings into words on any whitespace: Done

6. Ignore each of the following characters: Done
```
" : ; , . - + = / \ | [ ] { } ( ) * ^ &
```

7. If the input contains no ignored characters, return an empty dictionary: Done

"""

def word_count(string):
    separators = '":;,.-+=/\|[]{}()*^&'
    
    words = string.lower().split()
    counts = {}
    
    for word in words:
        word = word.strip(separators)
        if not word:
            break
        if word in counts:
            counts[word] += 1
        else: 
            counts[word] = 1
            
    return counts


# Driver program
if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
