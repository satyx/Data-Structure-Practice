class tree:
	def __init__(self,data):
		self.data=data
		self.lchild=None
		self.rchild=None

root=tree(1)
n1=tree(2)
n2=tree(3)
n3=tree(4)
n4=tree(5)
n5=tree(6)
n6=tree(7)
n7=tree(8)
n8=tree(9)
n9=tree(10)


def height(tree):
	if tree==None:
		return 0
	lheight=height(tree.lchild)
	rheight=height(tree.rchild)
	if lheight>rheight:
		return lheight+1
	else:
		return rheight+1

max=0
def height2(tree,h):			#finds the height from top to bottom
	global max
	if tree==None:
		if h>max:
			max=h
		return

	height2(tree.lchild,h+1)
	height2(tree.rchild,h+1)

root.lchild=n1
root.rchild=n2

n1.lchild=n3
n1.rchild=n4

n2.lchild=None
n2.rchild=n5

n3.lchild=None
n3.rchild=n6

n4.lchild=n7
n4.rchild=None

n5.lchild=n8
n5.rchild=n9

print('height of tree using function1:',height(root))
height2(root,0)
print('height of tree using function2:'max)
