import sys
import time
class node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

root=None

def insert(x,nd):
	if nd==None:
		return node(x)
	elif x<nd.data:
		nd.left=insert(x,nd.left)
	elif x>nd.data:
		nd.right=insert(x,nd.right)
	return nd

def delete(root,x):
	if root==None:
		return None
	if root.data<x:
		root.right=delete(root.right,x)
	elif root.data>x:
		root.left=delete(root.left,x)
	else:
		if root.left==None:
			temp=root.right
			root=None
			return temp
		elif root.right==None:
			temp=root.left
			root=None
			return temp
	
		else:
			temp=smallest(root.right)
			root.data=temp.data
			root.right=delete(root.right,temp.data)
	return root	
def daddy(x,nd):
	if nd.data==x or nd.left==None and nd.right==None:
		return None
	elif nd.data>x:
		if nd.left.data==x:
			return nd
		else:
			return daddy(x,nd.left)
	elif nd.data<x:
		if nd.right.data==x:
			return nd
		else:
			return daddy(x,nd.right)

def inorder_s(nd):
	if nd.right==None:
		return inorder_s(daddy(nd.data,root))
	else:
		return smallest(nd.right)
	




def display(nd):
	if nd==None:
		return
	display(nd.left)
	print(nd.data,'->',end='')
	display(nd.right)

def smallest(nd):
	if nd==None:
		return None
	if nd.left==None:
		return nd
	else:
		return smallest(nd.left)

def find(x,nd):
	if nd==None:
		return None
	if nd.data==x:
		return nd
	if nd.data>x:
		return find(x,nd.left)
	if nd.data<x:
		return find(x,nd.right)

print('0.Exit\n1.Insert\n2.Delete\n3.Display\n4.Find Parent')
while True:
	ch=int(input('Enter your choice:'))
	if ch==0:
		break
	elif ch==1:
		root=insert(int(input('Enter data to be inserted:')),root)
	elif ch==3:
		print('Inorder:')
		display(root)
		print('NULL')
	elif ch==2:
		root=delete(root,int(input('Data:')))
	elif ch==4:
		data=int(input('Enter the child:'))
		dad=daddy(data,root)

		if dad==None:
			if data==root.data:
				print('It is root')
			else:
				print('Data absent')
		else:
			print(dad.data)
	elif ch==5:
		nd=find(int(input()),root)
		if nd==None:
			print('Absent')
		else:
			print(inorder_s(nd).data)
	else:
		print('Wrong Choice entered\nTerminating',end='')
		for i in range(8):
			time.sleep(0.2)
			print('.',end='')
			sys.stdout.flush()
		break

