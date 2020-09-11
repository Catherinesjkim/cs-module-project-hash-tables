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


"""
Day 2: Combining 3 things: Arrays, Hashing, & Linked List

"""

hash_table = [None] * 8  # 8 slots, all initialized to None


def my_hash(s):
    # take every character in the string, and convert character to number
    # Convert each character into UTF-8 numbers (it allows for more characters than ASCII & Unicode)
    sb = s.encode() # Get the UTF-8 bytes

    total = 0
    # O(n): n is the length of the string ("key")
    for b in sb:
        total += b
        total &= 0xffffffff  # limit total to 32 bits
    return total  # capacity


def hash_index(key):
    hash_num = my_hash(key)
    return hash_num % len(hash_table)


def put(key, value):
    # hash the key and get an index
    i - hash_index(key)
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


# Implement a LL Class
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def __repr__(self):
        currStr = ""
        curr = self.head
        while curr is not None:
            currStr += f'{str(curr.value)} -> '
            curr = curr.next
        return currStr

	# Runtime: O(1)
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node
    
    # Runtime: O(number of nodes)
    def insert_at_head_or_overwrite(self, node):
        existingNode = self.find(node.value)
        if existingNode is not None:
            existingNode.value = node.value
        else:
            self.insert_at_head(node)

	# Runtime: O(number of nodes)
	# Space: O(1) Constant - don't change depending on the input - Worst case.
    def delete(self, value):
        curr = self.head
        
        if curr.value == value:
            self.head = curr.next
            return curr
        
        prev = curr
        curr = curr.next
        
        while curr is not None:
            if curr.value == value:
                prev.next = curr.next
                curr.next = None
                return curr
            else:
                prev = curr 
                curr = curr.next
                
        return None # if we pass the while loop, there's none.

    # Runtime: O(number of nodes) - we need to traverse the entirety of this node
    def find(self, value):
		curr = self.head
		while curr is not None:
			if curr.value == vallue:
				return curr
			curr = curr.next
		return None

a = Node(1)
b = Node(2)
c = Node(3)
ll = LinkedList()
ll.insert_at_head(a)
ll.insert_at_head(b)
ll.insert_at_head(c)

print(ll)

"""
UPER for White Boarding Problems: 
1. Understand: Come up with test cases.
2. Plan: What patterns - think about the algo.
3. Execute: Easiest and fastest. Watch out for bugs.
4. Review: 
	Give your code a pass through and correct any bugs.
	Make sure you don't cause regressions when fixing your bugs. 
 	Test your code with the test cases you made in the Understand step. 
  	State your runtime and space complexity. 
"""
