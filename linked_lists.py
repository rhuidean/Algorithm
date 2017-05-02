class ListNode():
	'''Node Object'''
	def __init__(self, value):
		self.val = value
		self.next = None

b = ListNode(4)

print "{} {} {}".format(b,b.val,b.next)


class LinkedList():
	def __init__(self):
		self.head = None

	def addFront(self,value):
		new_node = ListNode(value)
		if self.head == None:
			self.head = node

		else:
			node.next = self.head
			self.head = node

	def contains(self,value):
		pointer = self.head
		while pointer != None:
			if pointer.val == value:
				return True
			pointer = pointer.next
		return False

	def removeFront(self):
		if self.head == None:
			return None
		else:
			self.head = self.head.next 

	def front(self):
		if self.head == None:
			return None
		else:
			return self.head.val

a = ListNode(3)
print "{} {}".format(a.val,a.next)

b = LinkedList()
b.addFront(3)
print "{} {} {}".format(b,b.head.val,b.head.next)

print b.contains(3)



b.removeFront()
print b.head


