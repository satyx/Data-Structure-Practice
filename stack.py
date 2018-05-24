class node:
	def __init__(self,data):
		self.data=data
		self.next=None
top=None
aux_top=None
count=0
def show(temp):
	global count
	if count==0:
		print("empty")
		return
	while temp!=None:
		print(temp.data,end="->")
		temp=temp.next
	print("NULL")

def push(x):
	global count,top,aux_top
	nd=node(x)
	if nd==None:
		print("Overflow")
		return
	nd.next=top
	top=nd
	count+=1
	if aux_top!=None:
		if x<aux_top.data:
			nd=node(x)
			nd.next=aux_top
			aux_top=nd

		else:
			nd=node(aux_top.data)
			nd.next=aux_top
			aux_top=nd
	else:
		nd=node(x)
		nd.next=aux_top
		aux_top=nd


def pop():
	global top,aux_top,count
	if count==0:
		print("Underflow")
		return
	temp,aux_temp=top,aux_top
	top,aux_top=top.next,aux_top.next
	x=temp.data
	del temp,aux_temp
	count-=1
	print("Popped element :",x)

def get_min():
	return aux_top.data

print("1.Push\n2.Pop\n3.Minimum element\n4.Count elements\n5.Show\n0.Exit")
	
while True:
	ch=int(input("Enter your choice:"))
	if ch==0:
		break
	elif ch==1:
		x=input("Enter the data:")
		push(x)
		print("Successfully Pushed")
	elif ch==2:
		x=pop()
	elif ch==3:
		print("Minimum element in the stack",get_min())
	elif ch==4:
		print("Total element:",count)
	elif ch==5:
		show(top)
