"""
Hash Table/Array: Time Complexities
Get: O(1) - Constant time
Store/Put: O(1) - Constant time
Delete: O(1) - Constant time

This is amortized/averaged over time. Worst case is actually O(n) Linear due to a lot of collisions and it has to go into every linked list node. 

Hash table uses hashing, array, linked list.

"""

def my_hash(s):
    sb = s.encode() # get utf/unicode representation for the string - convert the string into unicode(#)
    total = 0
    for b in sb:
        total += b
        total &= 0xffffffff
    return total

my_array = [None] * 8
print(f'my_array {my_array}')

# PUT - Storing a value
# O(1) - Constant Time
# Run key string through the hash function to get the hash value
# Mod the hash value with the table size to get the index
hash_index = my_hash("hello world") % 8 # 1116 <-- mod this to constraint the values between 0 and 7
print(f'hash_index {hash_index}')

# Store the value at the index
my_array[hash_index] = 'my value'
print(f'my_array {my_array}')


# GET a value
# O(1) - Constant Time
# Run key string through the hash function to get the hash value
hash_index = my_hash("hello world") % 8 # Mod the hash value with the table size to get the index
print(my_array[hash_index]) # Return the value at the index


# DELETE a value
# O(1) - Constant Time
hash_index = my_hash("hello world") % 8
my_array[hash_index] = None
print(my_array)
