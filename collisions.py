"""
Collision Resolution via Chaining
- Operations of a hash table get slower if there are a lot of collisions
- To solve collisions, chain values together by using linked list
- If a value already exists at that index, add the new item to the linked list
- Inserting at the head is easier
"""

hash_table = [None] * 8  # 8 slots, all initialized to None

def my_hash(s):
    # take every character in the string, and convert character to number
    # Convert each character into UTF-8 numbers (it allows for more characters than ASCII & Unicode)
    sb = s.encode()  # Get the UTF-8 bytes

    total = 0
    # O(n): n is the length of the string ("key")
    for b in sb:
        total += b
        total &= 0xffffffff  # limit total/clamp to 32 bits - computer architecture - your table should always be within/related to the power of 2
    return total  # capacity

def hash_index(key):
    hash_num = my_hash(key)
    return hash_num % len(hash_table)

def put(key, value):
    # hash the key and get an index
    i = hash_index(key)
    # CHECK IF SOMETHING ALREADY EXISTS AT THAT INDEX
    if hash_table[i] != None:
        print(f"Collision! Overwriting {repr(hash_table[i])}!")
    # Store the value in the array at the hashed index
    hash_table[i] = value

def get(key):
    # hash the key and get an Index
    i = hash_index(key)
    # Return the value from the array at that index
    return hash_table[i]

#    Key      Value        Pair
put("Hello", "Hello Value")
put("World", "World Value")
put("foo", "foo value") # "foo" hashes to same index as "Hello"
                        # AKA "foo collides with Hello"
print(hash_table)
