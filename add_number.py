class node:
	def __init__(self,data):
		self.data=data
		self.next=None

def create_list(num):
	head=None
	for i in num:
		nd=node(int(i))
		nd.next=head
		head=nd
	return head

def greater(num_1,num_2):
	 len(num_1)>len(num_2):
		return num_1,num_2
	elif len(num_2)>len(num_1):
		return num_2,num_1
	i=0
	while i<len(num_1):
		if int(num_1[i])>int(num_2[i]):
			return num_1,num_2
		elif int(num_1[i])<int(num_2[i]):
			return num_2,num_1
		i+=1
	return '-1','-1'




def difference(num_1,num_2):
	num_1,num_2=greater(num_1,num_2)
	if num_1[0]=='-' and num_1[1]=="1":
		return node(0)

	num_1=create_list(num_1)
	num_2=create_list(num_2)
	result=None
	borrow=0
	while num_2!=None:
		if num_1.data-borrow>=num_2.data:
			nd=node(num_1.data-borrow-num_2.data)
			borrow=0
		else:
			nd=node(10+num_1.data-borrow-num_2.data)
			borrow=1
		nd.next=result
		result=nd
		num_1=num_1.next
		num_2=num_2.next

	while num_1!=None:
		if num_1.data-borrow<0:
			nd=node(10+num_1.data-borrow)
			borrow=1
		else:
			nd=node(num_1.data-borrow)
			borrow=0
		nd.next=result
		result=nd
		num_1=num_1.next
	return result



a=input("Enter the first number:")
b=input("Enter the second number:")

diff=difference(a,b)
while diff.data==0 and diff.next!=None:
	rem=diff
	diff=diff.next
	del rem
temp=diff
print("Difference = ",end="")


while temp!=None:
	
	print(temp.data,end="")
	temp=temp.next
print()
