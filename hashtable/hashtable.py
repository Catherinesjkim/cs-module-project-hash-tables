# Average Time/Space Complexity - Assuming good hash fn and resizing strategy:
# GET: O(1) - Constant
# PUT/Store: O(1) - Constant
# DELETE: O(1) - Constant

# Worst Time/Space Complexity:
# GET: O(number of elements) - Linear
# PUT/Store: O(n)
# DELETE: O(n) 

class HashTableEntry:
    # Linked List hash table key/value pair
    def __init__(self, key, value):
        self.key = key # a string
        self.value = value
        # next to search
        self.next = None

# Hash table can't have fewer than this many buckets - to the power of 2 - number that works well with binary
MIN_CAPACITY = 8

# Day 1
# HashTable class using chaining
class HashTable:
# Constructor with optional initial capacity parameter
# Assigns all buckets with an empty list

    # A hash table with `capacity` buckets that accepts string keys. Implement this.
    def __init__(self, capacity):
        # Your code here
        # initialize the hash table with empty storage list entries
        # size of the array = min 8
        self.capacity = MIN_CAPACITY
        self.count = 0
        # will store our data in - set equal to None force python to get a list that has a fixed length
        self.bucket = [None] * capacity

    # Return the length of the list you're using to hold the hash table data. (Not the number of items stored in the hash table, but the number of slots in the main list.) 
    # One of the tests relies on this. Implement this.
    def get_num_slots(self):
        # Your code here
        return self.capacity

    # DJB2 hash, 32-bit. Implement this
    # returning my string into utf/unicode 
    # hash function - gets the hash - take a string, mess it up, and output a number
    def djb2(self, key):
        # Your code here
        hash = 5381
        # iterates characters in key,
        for character in key:
            hash = (hash * 33) + ord(character) # ord: numerical value of that character -->
        return hash

    # hash index function - gets the index
    # Take an arbitrary key and return a valid integer index within the storage capacity of the hash table
    # private get hash function that takes a key - uses the djb2 code above to calculate the index for that key and return that index
    def hash_index(self, key):
        # when you get that total, mod to the capacity value
        return self.djb2(key) % self.capacity

    # Store the value with the given key. Hash collisions should be handled with Linked List Chaining. Implement this. 
    # put function: put takes in a key and value - we are building a hash table - dictionary in Python
    def put(self, key, value):
        # hash the key and get an index
        # index is index value that I'm going to place it in the bucket
        index = self.hash_index(key) 
        # find the start of the linked list using the index
        # insert into the head of this LL a new HashTableEntry
        # entry is what I want to enter in the cell, constructing a list from the key and value passed in
        entry = HashTableEntry(key, value)
        # set the index into my bucket in the array
        bucket = self.bucket[index]
        # keeping track of the count and increasing by one
        self.count += 1
        # Search through the whole list
        # IF the key already exists in the LL 
        if bucket:
            self.bucket[index] = entry
            # Replace the value
            self.bucket[index].next = bucket
        # Else
        else: 
            # Add new HashTable Entry to the head of LL
            self.bucket[index] = entry
            
    # Retrieve the value stored with the given key. Returns None if the key is not found. Implement this.
    # searches for an item with matching key in the hash table
    # returns the item if found, or None if not found with LL
    def get(self, key):
        # get the storage list where this key would be
        # hash the key and get an index
        index = self.hash_index(key)
        # Get the LL AT the computed index
        bucket = self.bucket[index]
        # Search through the LL for the key
        # Compare keys until you find the right one
        while bucket:
            # locate the bucket, if that bucket is not None, then iteratate through the pairs that are in that bucket, find the value that matches that key and return that value
            # IF the key exists, return the value
            if bucket.key == key:
                return bucket.value
            bucket = bucket.next
            
            # if we don't find that key, we return None
            return None
        
    # Remove the value stored with the given key. Print a warning if the key is not found. Implement this.
    # Removes an item with matching key from the hash table
    def delete(self, key):
        # Search through the LL for the matching key
        # Delete from that node
        # Save the value and return the value of deleted node (or None)
        self.put(key, None)
        self.count -= 1

        
    # Day 2
    # Return the load factor for this hash table. Implement this.
    # If I'm runing out of space, let's keep track of the load factor.
    # I need to know when to increase the size of our table
    # Load Factor function - trigger the resize - is it time to do that?
    def get_load_factor(self):
        # num items (how many inserted) / num of buckets of array (length of the table)
        return self.count / self.capacity

    # Changes the capacity of the hash table and rehashes all key/value pairs. Implement this.
    # If load factor is too high (over 0.7) --> RESIZE!
    # If load factor is too small (under 0.2) --> DOWNSIZE! (you don't want to take too much of what you don't need)
    # Expand the table/array if load factor > 0.7 (double the current array size: x 2)
    # Shrink if < 0.2 (halve the array size: 1/2)
    # loadFactor = numElements/numSlots, numSlots (len(arr)), numElements (manually keeping track of it)
    # If it exists, del -1
    # If it doesn't exist, I don't have to del anything
    # will improve searching
    # Time Complexity: O(n) - number of total items - quite expensive - linear based on the number of items
    def resize(self, new_capacity):
        # Make a new array that's DOUBLE the current size - you don't want to double forever - start small, keep resizing in longer increments
        # Go through each LL in the array 
            # Go through each item and re-hash it - the hash index is dependent on the length
            # Insert the items into their new locations - reuse put function here
        pass
    
    def shrink(self, new_capacity):
        # Same as resize, but reduce array by HALF
        pass
    
    

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity - passed
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # print("")



