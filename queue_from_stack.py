class node:
	def __init__(self,data):
		self.data=data
		self.next=None
num=[int(i) for i in input("Enter the numbers:").split(" ")]

top=None
for i in num:
	nd=node(i)
	nd.next=top
	top=nd
temp=top
print("Output from stack")
while temp!=None:
	print(temp.data)
	temp=temp.next

temp=top
result=None
while temp!=None:
	nd=node(temp.data)
	nd.next=result
	result=nd
	temp=temp.next

temp=result
print("Output from queue")
while temp!=None:
	print(temp.data)
	temp=temp.next

