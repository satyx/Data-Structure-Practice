class node:
	def __init__(self,data):
		self.data=data
		self.next=None
count=0
def push(x):
	global top,rear,count
	nd=node(x)
	if top==None:
		top=rear=nd
	else:
		rear.next=nd
		rear=nd
	rearrange()
	count+=1

def pop():
	global top,count
	print("Popped data:",top.data)
	top=top.next
	count-=1
	
def rearrange():
	ch=count
	while ch>0:
		x=dequeue()
		enqueue(x)
		ch-=1

def enqueue(x):
	global top,rear
	nd=node(x)
	if top==None:
		top=rear=nd
	else:
		rear.next=nd
		rear=nd
def dequeue():
	global top,rear
	x=top.data

	if top==rear:
		top=rear=None
	else:
		top=top.next
	return x

top=rear=None
print("1.Push\n2.Pop\n3.Show\n4.Exit")
while True:
	ch=int(input("Enter choice:"))
	if ch==1:
		x=int(input("Data:"))
		push(x)
	elif ch==2:
		if count==0:
			print("Underflow")
			continue
		pop()
	elif ch==3:
		if count==0:
			print("Empty")	
			continue
		temp=top
		while temp!=None:
			print(temp.data,end="->")
			temp=temp.next
		print("NULL")
	elif ch==4:
		break
