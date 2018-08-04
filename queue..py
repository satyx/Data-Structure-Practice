import time
import sys
import os
class node:
	def __init__(self,data):
		self.data=data
		self.next=None

front=None
rear=None
print("0.Exit\n1.Enqueue\n2.Dequeue\n3.Print List")
while True:
	ch=int(input("Enter your choice:"))
	if ch==0:
		print("Quiting",end='')
		for i in range(20):
			print(".",end='')
			sys.stdout.flush()
			time.sleep(0.1)
		print()
		temp=os.system('clear')
		break
	
	elif ch==1:
		data=int(input("Enter the data"))
		nd=node(data)
		if nd==None:
			print("Overflow")
			print("Aborting",end='')
			for i in range(20):
				print(".",end='')
				sys.stdout.flush()
				time.sleep(0.1)
			print()
			temp=os.system('clear')
			break
		if front==None:
			front=rear=nd
		else:
			front.next=nd
			front=nd

	elif ch==2:
		if front==None:
			print("Underflow")
			continue
		elif front==rear:
			front=rear=None
		else:
			rear=rear.next
	elif ch==3:
		temp=rear
		while temp!=None:
			print(temp.data,"->",end="")
			temp=temp.next
		print("NULL")

	else:
		print("Sorry wrong data entered")
		print("Aborting",end='')
		for i in range(20):
			print(".",end='')
			sys.stdout.flush()
			time.sleep(0.1)
		print()
		temp=os.system('clear')
		break

