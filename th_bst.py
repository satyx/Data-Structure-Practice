class node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
		self.lboolean=False
		self.rboolean=False

root=None
rthread=None
lthread=None
def insert(nd,data):
	print('caw')
	if nd==None:
		print('mew')
		return node(data)
	else:
		print('bhow')
		if root.data>data:
			print('rohit')
			temp=root.left
			root.left=insert(nd.left,data)
			root.lboolean=False
			if root.left.right==None:
				print('ashay')
				root.left.right=root
				root.left.rboolean=True
			if root.left.left==None:
				print('roy')
				root.left.left=temp
				root.left.lboolean=True
		elif root.data<data:
			print('saket')
			temp=root.right
			root.right=insert(nd.right,data)
			root.rboolean=False
			if root.right.left==None:
				print('venky')
				root.right.left=root
				root.right.lboolean=True
			if root.right.right==None:
				print('namdev')
				root.right.right=temp
				root.right.rboolean=True
		print('kant')
		return root
#def delete(nd,data):
#	if nd==None:
#		return
#	if nd.data>data:
#		nd.left=delete(nd.left,data)
#		if lthread!=None:
#			nd.left=lthread
#			lthread=None
#			nd.left.lboolean=True
#	if nd.data<data:
#		nd.right=delete(nd.right,data)
#		if rthread!=None:
#			nd.right=rthread
#			rthread=None
#			nd.right.rboolean=True
#	else:
#		if nd.lboolean==True:
#			lboolean=nd.left
#			temp=nd.right
#			if temp==None
#			nd=None
#			return temp
#

def display(nd):
	if nd==None:
		return
	if nd.lboolean==False:
		display(nd.left)
	print(nd.data)
	if nd.rboolean!=True:
		display(nd.right)

while True:
	ch=int(input())
	if ch==0:
		break
	else:
		x=int(input())
		root=insert(root,x)
display(root)
