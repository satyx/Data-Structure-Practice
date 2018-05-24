class node:
	def __init__(self,data):
		self.data=data
		self.next=None

t=int(input())
while t>0:
	n=int(input())
	num=input().split()
	head=None
	for i in num[-1::-1]:
		nd = node(int(i))
		nd.next=head
		head=nd

	while head.next!=None:
		if head.next.data>head.data:
			rem=head
			head=head.next
			del rem
		else:
			break
	prev=head
	temp=head.next
	if temp!=None:
		while temp.next!=None:
			if temp.data<temp.next.data:
				rem=temp
				prev.next=temp.next
				temp=temp.next
				del rem
			else:
				prev=prev.next
				temp=temp.next
	while head!=None:
		print(head.data,end=" ")
		head=head.next
	print()

	t-=1
