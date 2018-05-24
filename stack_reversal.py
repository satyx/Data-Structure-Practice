#Reversal of a stack using recursion

class node:
	def __init__(self,data):
		self.data=data
		self=None

def reverse(curr,prev):
	global top
	if curr.next==None:
		top=curr
		curr.next=prev
		return
	else:
		reverse(curr.next,curr)
	curr.next=prev

top=None
for i in input("Enter the numbers:").split(" "):
	nd=node(int(i))
	nd.next=top
	top=nd
temp=top
while temp!=None:
	print(temp.data,end='->')
	temp=temp.next
print()

reverse(top,None)

		
temp=top
while temp!=None:
	print(temp.data,end='->')
	temp=temp.next
print()
