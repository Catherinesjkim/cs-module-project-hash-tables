class Node:
	def __init__(self, value):
	self.value = value
	self.next = None
	
	def __repr__(self):
	return f'Node({repr(self.value)})'
  
class LinkedList:
    def __init__(self):
        self.head = None
        
  