class node:
	def __init__(self,data):
		self.data=data
		self.next=None

inp=[int(i) for i in input("Enter the number").split()]

def sort():
	global top
	if top!=None:
		data=top.data
		top=top.next
		sort()
		insert(data)

def insert(x):
	global top
	curr=top
	prev=None
	if top==None:
		nd=node(x)
		nd.next=None
		top=nd
		return
	while curr!=None:
		if curr.data>x:
			break
		prev=curr
		curr=curr.next

	nd=node(x)
	nd.next=curr
	if prev==None:
		top=nd
	else:
		prev.next=nd



top=None
for i in inp:
	nd=node(i)
	nd.next=top
	top=nd

sort()
temp=top
while temp!=None:
	print(temp.data,end="->")
	temp=temp.next
print("NULL")
