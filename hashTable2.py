# Implement a Linked List Class - Chaining
# What are the main objects when creating a LL? 2 main objects.
# 1. Node class - implement a node class
class Node:
  # This class needs a initializer - pass itself, a node will have a value
	def __init__(self, value):
		self.value = value # assign value to the instance variable self.value
		self.next = None # we need next to move on to the next node for LL
  
	def __repr__(self):
		# cast it to a string self.value
		return str(self.value)
     

# 2. a Hash class or LL class
class LinkedList:
    # initializer, don't need to pass anything besides itself
    def __init__(self):
        self.head = None # LL is empty in the beginning

    # Representation: __repr__ double under method to easily print itself out, to get a good representation of what it looks like v. __str__? Debugging method
    def __repr__(self):
        # build a string,
        currStr = ""
        # will start from the head
        curr = self.head
        # go through the entire LL
        while curr is not None:
            # keep appending to the string the value of the current node we are at so that we can see exactly what the LL looks like when we are printing
            currStr += f'{str(curr.value)} -> '
            curr = curr.next
        return currStr

	# Runtime: O(1) - Constant time
    # Add to the LL
    # Insert a new node at the head of the LL
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    # Runtime: O(number of nodes)
    def insert_at_head_or_overwrite(self, node):
        # use find fn to see if the node exists in the list, 
        existingNode = self.find(node.value)
        # if it does, simply overwrite the value
        if existingNode is not None:
            existingNode.value = node.value
        # if it doesn't exist yet, simply insert at head
        else:
            self.insert_at_head(node)

    # Runtime: O(n) Linear - n == number of nodes
    # Space: O(1) Constant - don't change depending on the input - Worst case.
    # Delete a certain value from the LL
    # implement the delete fn
    def delete(self, value):
        # current node, will start at the head
        curr = self.head

		# handle edge case first
		# make sure to move to the next
		# if curr.value at the head is the value we want to delete,
		# we want to make sure we move the head to the next value of the current head
        if curr.value == value:
            self.head = curr.next
            # return the node that we just deleted
            return curr

		# We need 2 pointers
		# prev pointer == slower pointer, which is curr
        prev = curr
        # current one will be one ahead of it, so it's curr.next
        curr = curr.next

		# iterate through entirety of the list, 
  		# front pointer is curr, make sure curr is not None
		# if it is, the node that we want is not in the list
        while curr is not None:
            # if the node that we are currently on, the fast pointer is the value that we want to delete, 
            # then we found it
            if curr.value == value:
                # all we need to do, is below
                prev.next = curr.next
                # also delete the next pointer since it will not be part of the list anymore
                curr.next = None
                # since we want to return the node that we already deleted, simple return curr
                return curr
            # if we haven't found the node that we wanted to delete,
            else:
                prev = curr
                # move the pointer forward by one
                curr = curr.next
		
		# if we passed the while loop, we return none since we haven't found the node we wanted to delete
        return None  

    # Runtime: O(n) - number of nodes is n - we need to traverse the entirety of this node
    # Find a certain value in the LL
    def find(self, value):
        # curr will be starting at the head
        curr = self.head
        
        # while loop
        while curr is not None:
            # if curr value is value, 
            if curr.value == value:
                # then we found the node that we were looking for so return curr
                return curr
            # if not the curr value, we haven't found the node, so we go to the next node
            curr = curr.next
        
        # if we passed the while loop, we traversed the entirety of the LL, that node does not existe, we simple return None
        return None
            
# Make a few nodes           
a = Node(1)
b = Node(2)
c = Node(3)

# initialize an empty LL
ll = LinkedList()

# Insert a, b, c
ll.insert_at_head(a)
ll.insert_at_head(b)
ll.insert_at_head(c)
ll.insert_at_head_or_overwrite(a)

# What would be the order? 3 -> 2 -> 1
print(ll)
