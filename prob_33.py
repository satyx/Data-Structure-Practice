#Removal of loop using Flyod's cycle

class node:
	def __init__(self,data):
		self.data=data
		self.next=None

num=input("Enter the numbers:").split()

head=None
for i in num[-1::-1]:
	nd=node(int(i))
	nd.next=head
	head=nd

mutual=int(input("Which node you want to connect with"))

target,temp,end=None,head,None
while temp!=None:
	if mutual==1:
		target=temp
	end=temp
	temp=temp.next
	mutual-=1
end.next=target
fast,slow=head,head

try:
	while True:
		fast=fast.next.next
		slow=slow.next
		
		if fast==slow:
			print("loop")
			print("fast=",fast.data)
			break
except:
	print("Linear")

temp=slow.next
count=1
while temp!=slow:
	count+=1
	temp=temp.next
temp=head

a,b=head,head
while True:
	print(a.data,b.data)
	if count>1:
		b=b.next
		count-=1
		continue
	elif b.next==a:
		b.next=None
		break
	else:
		a=a.next
		b=b.next

print("Done")
