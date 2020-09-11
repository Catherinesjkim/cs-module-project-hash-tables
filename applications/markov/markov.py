import random

def review_generator():
    # Read in all the words in one go
    with open("input.txt") as f:
        words = f.read()
    
    # TODO: analyze which words can follow other words
    # converting array to string with join operator
    reviews = ''.join([i for i in words if str(i)]
                      ).replace("\n", " ").split(' ')
    index = 1
    chain = {}
    count = input('Which word would you like to add?: ')
    
    for word in reviews[index:]:
        key = reviews[index-1]
        if key in chain:
            chain[key].append(word)
        else:
            chain[key] = [word]
        index += 1
    word1 = random.choice(list(chain.keys()))
    message = word1.capitalize()
    while len(message.split(' ')) < ord('a'):
        word2 = random.choice(chain[word1])
        word1 = word2
        message += ' ' + word2
    return message

print(review_generator())

# TODO: construct 5 random sentences
