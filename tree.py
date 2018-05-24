class node:
	def __init__(self,data):
		self.data=data
		self.right=None
		self.left=None
		self.p=None
root=None

def find(key,temp):
	if temp!=None:
		if temp.data==key:
			return temp
		elif temp.data>key:
			return find(key,temp.left)
		else:
			return find(key,temp.right)
	return None

def display(temp):
	if temp==None:
		return
	display(temp.left)
	print(temp.data,end="->")
	display(temp.right)

def minimum(nd):
	if nd.left==None:
		return nd
	else:
		return minimum(nd.left)

def maximum(nd):
	if nd.right==None:
		return nd
	else:
		return maximum(nd.right)

def transplant(a,b):
	global root
	if a.p==None:
		root=b
	else:
		if a.p.left==a:
			a.p.left=b
		else:
			a.p.right=b
	if b!=None:
		b.p=a.p

def successor(nd):
	if nd.right!=None:
		return minimum(nd.right)
	else:
		y=nd.p
		while y!=None and nd==y.right:
			nd=y
			y=y.p
		return y

def predecessor(nd):
	if nd.left!=None:
		return maximum(nd.left)
	else:
		y=nd.p
		while y!=None and nd==y.left:
			nd=y
			y=y.p
		return y

while True:
	ch=int((input()))
	if ch==0:
		break
	elif ch==1:
		if root==None:
			root=node(int(input()))
		else:
			temp=root
			data=int(input())
			nd=None
			while temp!=None:
				nd=temp
				if temp.data>=data:
					temp=temp.left
				else:
					temp=temp.right
			if nd.data>=data:
				temp=node(data)
				temp.p=nd
				temp.p.left=temp
			else:
				temp=node(data)
				temp.p=nd
				temp.p.right=temp
	elif ch==2:
		if root==None:
			print("Empty")
		else:
			display(root)
			print("Null")
	elif ch==3:
		nd=find(int(input()),root)
		if nd!=None:
			print("Yes")
		else:
			print("no")
	elif  ch==4:
		data=int(input())
		nd=find(data,root)
		if nd==None:
			print("Not present")
		else:
			if nd.left==None:
				transplant(nd,nd.right)
			elif nd.right==None:
				transplant(nd,nd.left)
			else:
				y=minimum(nd.right)
				if y.p!=nd:
					transplant(y,y.right)
					y.right=nd.right
					y.right.p=y
				transplant(nd,y)
				y.left=nd.left
				y.left.p=y
	elif ch==5:
		if root==None:
			print("Empty")
		else:
			print(minimum(root).data)
	
	elif ch==6:
		x=int(input())
		nd=find(x,root)
		suc=successor(nd)
		if suc==None:
			print(x,'is has no successor')
		else:
			print(suc.data)
	elif ch==7:
		x=int(input())
		nd=find(x,root)
		pre=predecessor(nd)
		if pre==None:
			print(x,'has no predecassor')
		else:
			print(pre.data)
