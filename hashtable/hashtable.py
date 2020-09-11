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
    
    # for better representation of my output
    def __repr__(self):
        return f'{self.value} -> {self.next}'

# Hash table can't have fewer than this many buckets - to the power of 2 - number that works well with binary
MIN_CAPACITY = 8

# HashTable class using chaining
class HashTable:
# Constructor with optional initial capacity parameter
# Assigns all buckets with an empty list

    # A hash table with `capacity` buckets that accepts string keys. Implement this.
    def __init__(self, capacity):
        # Your code here
        # initialize the hash table with empty storage list entries
        # size of the array = min 8
        # will store our data in - set equal to None force python to get a list that has a fixed length
        self.capacity = MIN_CAPACITY
        self.bucket = [None] * self.capacity
        self.count = 0
        
    def __repr__(self):
        return str(self.capacity)

    # Return the length of the list you're using to hold the hash table data. (Not the number of items stored in the hash table, but the number of slots in the main list.) 
    # One of the tests relies on this. Implement this.
    def get_num_slots(self):
        return len(self.bucket)
    
    # Return the load factor for this hash table. Implement this.
    # If I'm runing out of space, let's keep track of the load factor.
    # I need to know when to increase the size of our table
    # Load Factor function - trigger the resize - is it time to do that?
    def get_load_factor(self):
        # num items (how many inserted) / num of buckets of array (length of the table)
        return self.count / len(self.bucket)
    
    # DJB2 hash, 32-bit. Implement this
    # returning my string into utf/unicode
    # hash function - gets the hash - take a string, mess it up, and output a number
    def djb2(self, key):
        hash = 5381
        # iterates characters in key,
        for character in key:
            # ord: numerical value of that character -->
            hash = ((hash << 5) + hash) + ord(character)
        return hash & 0xFFFFFFFF

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
        # store as LL node
        node = HashTableEntry(key, value)
        # print(node)
        key = self.bucket[index]
        
        self.count += 1
        
        # the key exist
        if key:
            # overwrite with the node
            self.bucket[index] = node
            self.bucket[index].next = key
        # if self.capacity[index] exist,
        # use LL to set next to the repeated key and value
        else:
            self.bucket[index] = node
        # print('adding node', node.next)
        print(self.bucket)
        return self.bucket[index]
        
            
    # Remove the value stored with the given key. Print a warning if the key is not found. Implement this.
    # Removes an item with matching key from the hash table
    def delete(self, key):
        # Search through the LL for the matching key
        # Delete from that node
        # Save the value and return the value of deleted node (or None)
        self.count -= 1
        self.put(key, None)
            
    # Retrieve the value stored with the given key. Returns None if the key is not found. Implement this.
    # searches for an item with matching key in the hash table
    # returns the item if found, or None if not found with LL
    def get(self, key):
        # get the storage list where this key would be
        # hash the key and get an index
        item = self.hash_index(key)
        # Get the LL AT the computed index
        storage = self.bucket[item]
        # Search through the LL for the key
        # Compare keys until you find the right one
        while storage:
            # locate the bucket, if that bucket is not None, then iteratate through the pairs that are in that bucket, find the value that matches that key and return that value
            # IF the key exists, return the value
            if storage.key == key:
                return storage.value
            storage = storage.next

    # Changes the capacity of the hash table and rehashes all key/value pairs. Implement this.
    # If load factor is too high > 0.7 --> RESIZE!
    # Expand the table/array if load factor > 0.7 (double the current array size: x 2)
    # If load factor is too small < 0.2 --> DOWNSIZE!
    # Shrink if < 0.2 (halve the array size: 1/2)
    # loadFactor = numElements/numSlots, numSlots (len(arr)), numElements (manually keeping track of it)
    # This will improve searching
    # Time Complexity: O(n) - number of total items - quite expensive - linear based on the number of items
    # Make a new array that's DOUBLE the current size - you don't want to double forever - start small, keep resizing in longer increments
        # Go through each LL in the array
        # Go through each item and re-hash it - the hash index is dependent on the length
        # Insert the items into their new locations - reuse put function here
    def resize(self, new_capacity):
        self.capacity = new_capacity
        # downsize
        if self.get_load_factor() < 0.2:
            # new_capacity = new_capacity // 2
            # // without a decimal part
            new_capacity //= 2
            self.capacity = new_capacity
            old_bucket = self.bucket
            self.bucket = [None] * self.capacity
            # Traverse the old bucket and pass each previous value into the put method of our empty bucket
            for node in old_bucket:
                while True:
                    if node != None:
                        self.put(node.key, node.value)
                        if node.next == None:
                            break
                        node = node.next
                    else: break
        if self.get_load_factor() > 0.7:
            # new_capacity *= 2
            self.capacity = new_capacity
            # get key to rehash and value to correspond to key
            old_bucket = self.bucket
            self.bucket = [None] * self.capacity
            for node in old_bucket:
                while True:
                    if node != None:
                        self.put(node.key, node.value)
                        if node.next == None:
                            break
                        node = node.next
                    else: break


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
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")



