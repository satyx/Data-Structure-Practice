class node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
		self.parent=None

root=None

def fill():
	global root
	ch=1
	print('Enter x to exit')
	if root==None:
		ch=input('Enter data:')
		if ch=='x':
			return
		root=node(ch)
	queue=[root]
	while ch!='x':
		print(root.data,'fffff')
		ch=input('Enter Data:')
		if ch=='x':
			break
		while True:
			if queue[-1].left==None:
				queue[-1].left= node(ch)
				break

			else:
				queue.insert(0,queue[-1].left)
				if  queue[-1].right==None:
					queue[-1].right= node(ch)
					break
			
			queue.insert(0,queue[-1].right)
			queue.pop()

def display(ch):
	if ch==None:
		return
	display(ch.left)
	print(ch.data,'->',end='')
	display(ch.right)

fill()
display(root)
print('NULL')
fill()
display(root)
print('NULL')
