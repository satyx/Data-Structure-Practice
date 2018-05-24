t=int(input())
while t>0:
	t-=1
	n=int(input())
	result=True
	num=[int(i) for i in input().split()]
	if n%2!=0:
		print("No")
		continue
	top=n-1
	while top>0:
		if abs(num[top]-num[top-1])!=1:
			result=False
			break
		top-=1
		top-=1
	if result==False:
		print("No")
	else:
		print("Yes")
	
