class Node(object):
	"""docstring for Node"""
	def __init__(self, value=None,lchild=None,rchild=None):
		self.value = value
		self.lchild = lchild
		self.rchild = rchild

class Tree(object):
	"""docstring for Tree"""
	def __init__(self):
		self.root = None
		self.q = []

	def add(self,v):
		new = Node(value=v)
		self.q.append(new)
		if self.root == None:
			self.root = new
		else:
			node = self.q[0]
			if node.lchild == None:
				node.lchild = new
			else:
				node.rchild = new
				self.q.pop(0)

	def front_order(self,node):
		if node == None:
			return
		print(node.value,end=" ")
		self.front_order(node.lchild)
		self.front_order(node.rchild)

	def middle_order2(self,node):
		if node == None:
			return
		self.middle_order2(node.lchild)
		print(node.value,end=" ")
		self.middle_order2(node.rchild)

	def front_print(self,node):
		s=[]
		n=node
		while s or n:
			while n:
				print(n.value,end=" ")
				s.append(n)
				n=n.lchild
			n=s.pop()
			n=n.rchild
t=Tree()
for i in range(1,10):
	t.add(i)
t.front_print(t.root)
print("")
t.front_order(t.root)
print("")
t.middle_order2(t.root)
