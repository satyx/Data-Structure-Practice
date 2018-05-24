t=int(input())
def isEmpty(s):
	return len(s)==0
while t>0:
	stack=list()
	a=input()
	num=[int(i) for i in input().split()]
	final={}
	i=1
	ptr=0
	stack.append(num[0])
	while  i<len(num):
		x=num[i]
		while len(stack)>0:
			element=stack.pop()
			if element < x:
				final[element]=x
			else:
				stack.append(element)
				break
		stack.append(x)
		i+=1

	for i in stack:
		final[i]=-1

	for i in num:
		print(final[i],end=" ")
	print()
							
			


	t-=1
