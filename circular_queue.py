class node:
	def __init__(self,data):
		self.data=data
		self.next=None

front=None
rear=None

print("1.Enqueue\n2.Dequeue\n3.Print\n0.Exit")
while True:
	ch=int(input("Enter choice:"))
	if ch==0:
		break
	elif ch==1:
		data=int(input("Enter data:"))
		nd=node(data)
		if nd==None:
			print("Overflow")
			continue
		if front==None:
			front=nd
			rear=nd
			rear.next=front
		else:
			rear.next=nd
			rear=nd
			rear.next=front
	elif ch==2:
		if front==None:
			print("Underflow")
		else:
			print(front.data)
			if front==rear:
				front=None
				rear=None
			else:
				front=front.next
				rear.next=front
	elif ch==3:
		if front==None:
			print("Empty")
			continue
		else:
			temp=front
			print(temp.data,"->",end="")
			temp=temp.next
			while temp!=front:
				print(temp.data,"->",end="")
				temp=temp.next
			print(temp.data)
	else:
		break	
