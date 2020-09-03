"""
Instructor: Mari Batilando

To Put:
- Run key string through the hash fn to get the hash value
- Mod the hash value with the table size 

To Delete:

Time Complexities:
- Get: O(1) - Constant time
- Store: O(1) 
- Delete: O(1)
- This is amortized/averaged over time. Worst case is actually O(n) and we'll talk about why in the next lecture!

Project: blockchain
- Implement a hash table class that can get/store

Hash Functions:
- Used widely in cryptography
- SHA-256 encryption algo
	- Used for the most popular authentication and encryption protocols (SSL, TLDS, etc.)
	- Also used in cryptocurrencies such as Bitcoin
		- Used to verify transactions, create addresses, etc.
  
Collisions: How hash tables are used in an interview. 
- What happens if you try to store values that have the same index?
- Based on our last example you would overwrite the values!
- How can we solve this?
- To solve collisions, chain values together by using linked lists
- If a value already exists at that index, add the new item to end of the ll
- Operations of a hash table get slower if there are a lot of collisions

LL Review
- Comprised of nodes
- Nodes contain: value, next pointer, previous (if DLL)
- To fully implement a hash table, we're come

Load Factor and Resizing:
- The performance of a hash table worsens as there are more Collisions
	- Can you think of any?

How chaining works:
Hash Function
1. Create a node
2. Store key and value (why do we store a key? We might have multiple values in a given index, so we need to save the key)
3. Downside: Why would it take linear O(n) in the worst case? Need to go to every node in the LL due to collisions
5. 

Hash Tables: Things to know 
- There's many use-cases for hash tables

Jewels and stones
- Return how many stones are Jewels
- Leetcode

DJB2: why 33?

"""

def my_hash(s):
	sb = s.encode()
	total = 0
	for b in sb:
		total += b
	return total

my_array = [None] * 8
print(f'my_array {my_array}')

# Storing a value
hash_index = my_hash("hello world") % 8 # to constrain the value between 0 and 7
another_hash_index = my_hash("world hello") % 8

print(f'hash_index {hash_index}')

my_array[hash_index] = 'my value'
print(f'my_array {my_array}')

# Get a value 
hash_index = my_hash("hello world") % 8
print(my_array[hash_index])

# Deleting a value
hash_index = my_hash("hello world") % 8
my_array[hash_index] = None
print(my_array)
