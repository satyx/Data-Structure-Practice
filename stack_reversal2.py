class node:
	def __init__(self,data):
		self.data=data
		self.next=None

top=None
for i in input("Enter the numbers:").split():
	nd=node(int(i))
	nd.next=top
	top=nd
temp=top
while temp!=None:
	print(temp.data,end="->")
	temp=temp.next
print("NULL")
prev=None
curr=top
after=top.next

while curr!=None:
	curr.next=prev
	prev=curr
	curr=after
	top=prev
	if curr!=None:
		after=after.next

temp=top
while temp!=None:
	print(temp.data,end="->")
	temp=temp.next
print("NULL")	
