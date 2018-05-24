deque=[0 for  i in range(10)]
front=-1
rear=-1
print("1.Enqueue from front\n2.Enqueue from end\n3.Deque from front\n4.Dequeue from rear\n5.Print\n0.Exit")
while True:
	ch=int(input("Enter choice:"))
	if ch==0:
		break
	elif ch==1:
		if front==rear-1 or front==9 and rear==0:
			print("Overflow")
			continue
		data=int(input("Enter data:"))
		if front==-1:
			front=0
			rear=0
			deque[front]=data
		elif front<9:
			front+=1
			deque[front]=data
		else:
			front=0
			deque[front]=data
	elif ch==2:
		if front==rear-1 or front==9 and rear==0:
			print("Overflow")
			continue
		data=int(input("Enter data:"))
		if rear==-1:
			front=0
			rear=0
			deque[rear]=data
		elif rear>0:
			rear-=1
			deque[rear]=data
		else:
			rear=9
			deque[rear]=data
	elif ch==3:
		if front==-1:
			print("Underflow")
			continue
		if front==rear:
			front=-1
			rear=-1
		elif front>0:
			front-=1
		else:
			front=9
	elif ch==4:
		if rear==-1:
			print("Underflow")
			continue
		if front==rear:
			front=-1
			rear=-1
		elif rear<9:
			rear+=1
		else:
			rear=0
	elif ch==5:
		if front==-1:
			print("Underflow")
			continue
		else:
			i=rear
			while i!=front:
				print(deque[i],"->",end='')
				if i<9:
					i+=1
				else:
					i=0
			print(deque[i])
	else:
		break

			
		
	

