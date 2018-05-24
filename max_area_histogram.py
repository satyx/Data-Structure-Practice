t=int(input())
while t>0:
	waste=input()
	height=[]
	pos=[]

	size=[int(i) for i in input().split()]
	loop_var=0
	maxi=0
	while loop_var<len(size):
		i=size[loop_var]
		if len(height)==0:
			height.append(i)
			pos.append(loop_var)
		elif height[len(height)-1]<i:
			height.append(i)
			pos.append(loop_var)
		else:
			while True:
				if height[len(height)-1]==i:
					break
				elif height[len(height)-1]>i:
					h=height.pop()
					prev=pos.pop()
					if h*(loop_var-prev)>maxi:
						maxi=h*(loop_var-prev)
				if len(height)<=0:
					height.append(i)
					pos.append(prev)
					break
	
				if height[len(height)-1]<i:
					height.append(i)
					pos.append(prev)
					break
			
	
		loop_var+=1
	while len(height)>0:
		if height[len(height)-1]*(loop_var-pos[len(pos)-1])>maxi:
			maxi= height.pop()*(loop_var-pos.pop())
		else:
			height.pop()
			pos.pop()
	print(maxi)
	t-=1	

