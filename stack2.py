class node:
	def __init__(self,data):
		self.data=data
		self.next=None

top=None
aux_top=None
count=0

def get_last_element():
	return top.data

def remove_last_element():
	global top,aux_top,count,least
	top=top.next
	least=2*least-aux_top.data
	aux_top=aux_top.next
	count-=1

def add_element(x):
	global top,aux_top,count,least
	nd=node(x)
	nd.next=top
	top=nd

	if count==0:
		nd=node(x)
		least=x
	else:
		if x<least:
			x,least=2*x-least,x
			nd=node(x)
		else:
			nd=node(least)	
	nd.next=aux_top
	aux_top=nd
	count+=1
		
def get_min():
	return least

print("1.Add data\n2.Remove Last Data\n3.Get Last Data\n4.Get min\n5.Exit")
while True:
	ch=int(input("Enter your choice:"))
	if ch==1:
		x=int(input("Enter data:"))
		add_element(x)
	elif ch==2:
		if count==0:
			print("Underflow")
			continue
		remove_last_element()
	elif ch==3:
		if count==0:
			print("Underflow")
			continue
		print("Last element :",get_last_element())
	elif ch==4:
		if count==0:
			print("Underflow")
			continue
		print("Minimum element :",get_min())
	elif ch==5:
		break
	else:
		print("Wrong data entered\nAborting.........")
		break
