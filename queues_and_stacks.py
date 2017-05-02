class SLNode():
	'''Node Object'''
	def __init__(self, value):
		self.val = value
		self.next = None


class SLQueue():
	def __init__(self):
		self.head = None
		self.tail = None

	def enqueue(self,value):
		new_node = SLNode(value)
		self.tail.next = new_node
		self.tail = new_node

	def dequeue(self):
		front_node = self.head
		self.head = self.head.next
		front_node.next = None
		return front_node.val
	def front(self):
		return self.head.val

		







