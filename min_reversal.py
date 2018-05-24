test=int(input())
while test>0:
	count=0
	stack=[]
	inp=input()
	if len(inp)%2==1:
		print(-1)
		test-=1
		continue
	for i in inp:			#Removing the balanced part
		if i=='{':
			stack.append(i)
		elif i=='}':
			if len(stack)>0:
				if stack[-1]=='{':
					stack.pop()
					continue
				else:
					stack.append(i)
			else:
				stack.append(i)
	i=len(stack)-1
	while len(stack)>0:		#Better approach is if m=number of { and
					#n =number of } then required answer is 
					# smallest integer function(m/2) +
					# smallest integer function(n/2)
		if stack[i]=='{':
			if stack[i-1]=='}':
				count+=2
				stack.pop()
				stack.pop()
			else:
				count+=1
				stack.pop()
				stack.pop()
		else:
			count+=1
			stack.pop()
			stack.pop()
		i-=2
	print(count)
	test-=1
