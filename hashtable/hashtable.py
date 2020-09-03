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


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
# I use two lists to create a HashTable class that implements the Map abstract data type. One list, called capacity, will hold the key items and a parallel list. Second list, called value, will hold the data values. When we look up a key, the corresponding position in the data list will hold the associated data value. We will treat the key list as a hash table. The initial size for the hash table is 11. Although this is arbitrary, it is important that the size be a prime number so that the collision resolution algorithm can be as efficient as possible. 
    def __init__(self, capacity):
        self.size = 11
        self.capacity = [None] * self.size
        self.value = [None] * self.size

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

# hashfunction implements the simple remainder method. The collision resolution technique is linear probing with a “plus 1” rehash function. The put function assumes that there will eventually be an empty slot unless the key is already present in the self.capacity. It computes the original hash value and if that slot is not empty, iterates the rehash function until an empty slot occurs. If a nonempty slot already contains the key, the old value is replaced with the new value. Dealing with the situation where there are no empty capcity left
    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        hashvalue = self.hashfunction(key, len(self.capacity))
        
        if self.capacity[hashvalue] == None:
            self.capacity[hashvalue] = key
            self.value[hashvalue] = value
        else:
            if self.capacity[hashvalue] == key:
                self.value[hashvalue] = value # replace 
            else:
                nextcapacity = self.rehash(hashvalue, len(self.capacity))
                while self.capacity[nextcapacity] != None and \
                    self.capacity[nextcapacity] != key:
                        nextcapacity = self.rehash(nextcapacity, len(self.capacity))
                
                if self.capacity[nextcapacity] == None:
                    self.capacity[nextcapacity] = key
                    self.value[nextcapacity] = value
                else:
                    self.value[nextcapacity] = value # replace

    def hashfunction(self, key, size):
        return key % size
    
    def rehash(self, oldhash, size):
        return (oldhash + 1) % size


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here

# The final methods of the HashTable class provide additional dictionary functionality. Overload the __getitem__ and __setitem__ methods to allow access using``[]``. This means that once a HashTable has been created, the familiar index operator will be available.
    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        startcapacity = self.hashfunction(key, len(self.capacity))
        
        value = None
        stop = False
        found = False
        position = startcapacity
        while self.capacity[position] != None and \
                                not found and not stop:
            if self.capacity[position] == key:
                found = True
                value = self.value[position]
            else:
                position = self.resize(position, len(self.capacity))
                if position == startcapacity:
                    stop = True
        return value

    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, value):
        self.put(key, value)


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

# hex(hash_djb2(u'hello world, 世界'))  # '0xa6bd702fL'
