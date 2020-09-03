# 
class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

"""
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
"""
# HashTable class using chaining
class HashTable:
# Constructor with optional initial capacity parameter
# Assigns all buckets with an empty list
    def __init__(self, capacity):
        # Your code here
        # initialize the hash table with empty bucket list entries
        self.size = 11
        self.capacity = [None] * self.size
        self.value = [None] * self.size
        self.table = []
        for i in range(capacity):
            self.table.append([])

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.capacity)

# Once the hash values have been computed, we can insert each item into the hash table at the designated position. This is referred to as the load factor, and is commonly denoted by 𝜆 = 𝑛𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝑖𝑡𝑒𝑚𝑠 / 𝑡𝑎𝑏𝑙𝑒 𝑠𝑖𝑧𝑒
    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this
        """
        key = 5381
        for x in self:
            key = ((key << 5) + key) + ord(x)
        return key & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.djb2(key) % self.capacity

    """
    Store the value with the given key.

    Hash collisions should be handled with Linked List Chaining.

    Implement this.
    """
    # Inserts a new item into the hash table
    def put(self, key, value):
        # Your code here
        # get the bucket list where this item will go
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        
        # insert the item to the end of the bucket list
        bucket_list.append(key)
        


    """
    Remove the value stored with the given key.

    Print a warning if the key is not found.

    Implement this.
    """
    # Removes an item with matching key from the hash table
    def delete(self, key):
        # get the bucket list where this item will be removed from
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        
        # remove the item from the bucket list if it is present
        if key in bucket_list:
            bucket_list.remove(key)

    """
    Retrieve the value stored with the given key.

    Returns None if the key is not found.

    Implement this.
    """
    # searches for an item with matching key in the hash table
    # returns the item if found, or None if not found
    def get(self, key):
        # get the bucket list where this key would be
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        
        # search for the key in the bucket list
        if key in bucket_list:
            # find the item's index and return the item that is in the bucket list
            item_index = bucket_list.index(key)
            return bucket_list[item_index]
        else:
            # the key is not found
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



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

    # Test storing beyond capacity
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



