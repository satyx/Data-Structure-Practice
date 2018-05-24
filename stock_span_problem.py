class node:
	def __init__(self,index):
		self.index=index
		self.next=None

test=int(input())
while test>0:
	num=input()
	x=[int(i) for i in input().split()]
	span=[0 for i in x]
	maximum=None

	count=0
	for i in x:
		if count==0:
			span[count]+=1
			count+=1
			continue
		else:
			if i<x[count-1]:
				span[count]+=1
				nd=node(count-1)
				nd.next=maximum
				maximum=nd
				count+=1
			else:
				span[count]+=span[count-1]
				while maximum!=None:
					if i<x[maximum.index]:
						break
					else:
						span[count]+=span[maximum.index]
						maximum=maximum.next
				span[count]+=1
				count+=1
			 
	for i in span:
		print(i,end=" ")
	test-=1
	print()
