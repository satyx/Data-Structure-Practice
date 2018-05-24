class node:
	def __init__(self,data):
		self.data=data
		self.next=None
	
least=None
count=0
top=None

def push(x):
	global count, least,top
	if count==0:
		least=x
	elif x<least:
		x,least=2*x-least,x
	nd=node(x)
	nd.next=top
	top=nd
	count+=1

def pop():
	global count,least,top
	if count==0:
		print("Under flow")
		return
	if top.data<least:
		least=2*least-top.data
	rm=top
	top=top.next
	del rm
	count-=1
def get_min():
	global least,count
	if count==0:
		print("Underflow")
		return
	print("Min :",least)		

print("1.Push\n2.Pop\n3.Get Minimum\n4.Exit")
while True:
	ch=int(input("Choice:"))
	if ch==0:
		break
	if ch==1:
		x=int(input("Enter data:"))
		push(x)
	if ch==2:
		pop()
	if ch==3:
		get_min()
