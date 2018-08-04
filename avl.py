class node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
		self.height=0
		self.bf=0

root=None

def update(nd):
	if nd.left==None:
		if nd.right==None:
			nd.height=0
			nd.bf=0
		else:
			nd.height=1+nd.right.height
			nd.bf=(nd.right.height+1)*(-1)
	elif nd.right==None:
		nd.height=1+nd.left.height
		nd.bf=nd.left.height+1
	else:
		nd.height=1+max(nd.left.height,nd.right.height)
		nd.bf=nd.left.height-nd.right.height


def rearrange(nd):
	if nd.bf>1:
		if nd.left.bf==1 or nd.left.bf==0:
			return rr(nd)
		else:
			lr(nd.left)
			return rr(nd)
		
	if nd.bf<-1:
		if nd.right.bf==-1 or nd.right.bf==0:
			return lr(nd)
		else:
			rr(nd.right)
			return lr(nd)
	return nd

def rr(nd):
	temp=nd.left
	nd.left=temp.right
	temp.right=nd
	if nd!=None:
		update(nd)
	if temp!=None:
		update(temp)
	return temp


def lr(nd):
	temp=nd.right
	nd.right=temp.left
	temp.left=nd
	if nd!=None:
		update(nd)
	if temp!=None:
		update(temp)
	return temp


def smallest(nd):
	if nd==None:
		return None
	if nd.left==None:
		return nd
	else:
		return smallest(nd.left)

def insert(nd,data):
	if nd==None:
		return node(data)
	if  nd.data>data:
		nd.left=insert(nd.left,data)
		update(nd)
		nd=rearrange(nd)
	elif nd.data<data:
		nd.right=insert(nd.right,data)
		update(nd)
		nd=rearrange(nd)
	return nd

def delete(nd,data):
	if nd==None:
		return
	if nd.data>data:
		nd.left=delete(nd.left,data)
		update(nd)
		nd=rearrange(nd)

	elif nd.data<data:
		nd.right=delete(nd.right,data)
		update(nd)
		nd=rearrange(nd)


	else:
		if nd.left==None:
			temp=nd.right
			nd=None
			return temp
		elif nd.right==None:
			temp=nd.left
			nd=None
			return temp
		else:
			temp=smallest(nd.right)
			nd.data=temp.data
			nd.right=delete(nd.right,temp.data)
			update(nd)
			nd=rearrange(nd)
	return nd


def display(nd):
	if nd==None:
		return
	display(nd.left)
	print(nd.data,end='')
	print('('+str(nd.bf)+')',end='')
	display(nd.right)

def Display(nd):
	if nd==None:
		return
	print(nd.data,end='')
	Display(nd.left)
	Display(nd.right)

while True:
	ch=input()
	if ch=='e':
		break
	elif int(ch)>0:
		root=insert(root,int(ch))
	elif int(ch)<0:
		root=delete(root,int(ch)*(-1))

	elif int(ch)==0:
		display(root)
		print()
		Display(root)
		print()
	if root!=None:
		print('root:',root.data)
