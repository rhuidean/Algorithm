class ListNode():
	'''Node Object'''
	def __init__(self, value):
		self.val = value
		self.next = None

class LinkedList():
	def __init__(self):
		self.head = None

	def addFront(self,value):
		node = ListNode(value)
		node.next = self.head
		self.head = node

	def contains(self,value):
		pointer = self.head
		while pointer != None:
			if pointer.val == value:
				return True
			pointer = pointer.next
		return False


a = ListNode(3)
print "{} {}".format(a.val,a.next)

b = LinkedList()
b.addFront(a)
print "{} {} {}".format(b,b.head.val,b.head.next)

print b.contains(3)

