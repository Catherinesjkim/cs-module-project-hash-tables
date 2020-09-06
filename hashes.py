"""
Artem

The requirements for a Hash Function:

1. A hash function must be consistent(deterministic). Every time it receives the sam input (like "aqua"), it must return the same output (like 4). If it's not deterministic, it's no a hash function. Same input will always return the same output. 

2. Different input data should return different numbers to minimize collisions. 

3. A hash function must return numbers that are within a specific range. 

Hashing: blockchain, saving passwords in the BE, SHA-256 (256 bits limit), SHA-512 (used in class), etc. 
SHA: Secure Hashing Algo

"""
# Magic Function: 
# takes a word --> returns the index fo where that word is located in some array of
# book --> 1
# egypt --> 4
# fake_word --> None
# this fn is O(1)

# HASH FUNCTIONS
# Any string input ---> A specific number (within some range)
# MOST IMPORTANT!
# This fn must be deterministic
# Same input will alwasy return the same output
# Non-reversible
# Avoid collisions

# Similar to node class in LL - I can have 8 LL potentially
class HashTabelEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        # will linked the nodes together
        self.next = None
        
hash_table = [None] * 8 # 8 slots, all initialized to None

# O(n) for length of key
def my_hash(self):
    # take every character in the string, and convert character to number
    # Convert each character into UTF-8 numbers (it allows for more characters than ASCII & Unicode)
    string_utf = self.encode()
    
    total = 0
    # O(n): n is the length of the string ("key")
    for char in string_utf:
        total += char
        total &= 0xffffffff # limit total to 32 bits 
    return total # capacity

def hash_index(key):
    hash_num = my_hash(key)
    return hash_num % len(hash_table)

def put(key, value):
    # hash the key and get an index
    i = hash_index(key)
    
    # find the start of the linked list using the index
    
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

put("Hello", "Hello Value")
put("World", "World Value")
    
print(hash_table)


# No DS can exist without having a specific initial size limit --> resize later
hash_table = [None] * 8 # 8 none values - of size of power of 2 - for our hash function to return 32 bits
#  1,   2,   4,   8,  16,  32,  64,  128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536
# 2^0, 2^1, 2^2, 2^3, 2^4, 2^5, 2^6, 2^7, 2^8, 2^9, 2^10, 2^11, 2^12, 2^13,  2^14, 2^15,  2^16

# ADD items to hash_table using my_hash function
# Hash the key (Hello and World) to get an index 
# Store the value at the generated Index
index = my_hash('card', len(hash_table))  # O(key)
hash_table[index] = 'Value for card' # O(1)
# Speed in context of length of the hash table: O(1)
# Because O(1) + O(key) <-- usually very small

index = my_hash('apple', len(hash_table))
hash_table[index] = 'Value for apple'

# Retrieve some items from hash_table
# Let's retrieve the value for "Hello"
index = my_hash('card', len(hash_table))
print(hash_table[index])
print(hash_table)


"""
TK
"""
def my_hashing_func(str, list_size):
    bytes_representation = str.encode()

    sum = 0
    for byte in bytes_representation:
        sum += byte

    return sum % list_size

my_list = [None] * 5

my_list[my_hashing_func("aqua", len(my_list))] = "#00FFFF" # put the value in list
# print(my_list[my_hashing_func("aqua", len(my_list))]) # get value from list

# put the value in list
my_list[my_hashing_func("beige", len(my_list))] = "#F5F5DC"
# print(my_list[my_hashing_func("beige", len(my_list))])  # get value from list

# put the value in list
my_list[my_hashing_func("chartreuse", len(my_list))] = "#7FFF00"
# print(my_list[my_hashing_func("chartreuse", len(my_list))])  # get value from list

# put the value in list
my_list[my_hashing_func("deepskyblue", len(my_list))] = "#00BFFF"
# get value from list
# print(my_list[my_hashing_func("deepskyblue", len(my_list))])

# put the value in list
my_list[my_hashing_func("forestgreen", len(my_list))] = "#228B22"
# get value from list
# print(my_list[my_hashing_func("forestgreen", len(my_list))])


"""
Day 2: Pseudocode of collisions management and resizing functions
"""

