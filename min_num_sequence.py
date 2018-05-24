t=int(input())
while t>0:
	t-=1
	inp=input()
	i=0
	curr=1
	while i<len(inp):
		num_D=0
		ch=inp[i]
		if ch=='I':
			if i==0:
				print(1,end="")
			j=i+1
			while j<len(inp):
				if inp[j]=='D':
					num_D+=1
					j+=1
				else:
					break
			curr+=num_D+1
			print(curr,end="")
			temp=1
			while temp<=num_D:
				print(curr-temp,end="")
				temp+=1
			i+=num_D+1
		else:
			num_D=1
			j=i+1
			while j<len(inp):
				if inp[j]=='D':
					num_D+=1
					j+=1
				else:
					break
			curr+=num_D
			temp=0
			while temp<=num_D:
				print(curr-temp,end="")
				temp+=1
			i+=num_D
	print()
