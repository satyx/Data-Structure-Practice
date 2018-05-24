a=[]
x_count=0
y_count=0

def push1(x):
	global a,x_count
	a.insert(x_count,x)
	x_count+=1

def push2(x):
	global a,y_count
	a.insert(len(a)-y_count,x)
	y_count+=1

def pop1():
	global a,x_count
	if x_count==0:
		print("Underflow")
		return
	print("Popped element =",a[x_count-1])
	del a[x_count-1]
	x_count-=1

def pop2():
	global a,y_count
	if y_count==0:
		print("Underflow")
	print("Popped Element =",a[len(a)-y_count])
	y_count-=1
	del a[len(a)-y_count]
def show1():
	global a
	temp=x_count-1
	while temp>=0:
		print(a[temp])
		temp-=1
def show2():
	global a
	temp=len(a)-y_count
	while temp<len(a):
		print(a[temp])
		temp+=1

print("1.Push in first\n2.Push in second\n3.Pop in first\n4.Pop in second\n5.Show first\n6.Show second\n0.Exit")

while True:
	ch=int(input("Enter your choice:"))
	if ch==0:
		break
	elif ch==1:
		x=int(input("Enter data:"))
		push1(x)
	elif ch==2:
		x=int(input("Enter data:"))
		push2(x)
	elif ch==3:
		pop1()
	elif ch==4:
		pop2()
	elif ch==5:
		show1()
	elif ch==6:
		show2()
