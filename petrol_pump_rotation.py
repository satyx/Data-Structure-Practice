t=int(input())
while t>0:
	t-=1
	n=2*int(input())
	inp=[int(i) for i in input().split()]
	curr=0
	total=0
	i=0
	index=0
	while i<n:
		total+=inp[i]-inp[i+1]
		curr+=inp[i]-inp[i+1]
		if curr<0:
			index=i//2+1
			curr=0
		i+=2
	if total<0:
		print(-1)
	else:
		print(index)

		
	
