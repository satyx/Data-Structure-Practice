inorder=[int(i) for i in input().split()]

def postorder(num):
	print('mew')
	arr=[]
	i=0
	while i<len(num):
		ltree=postorder(num[:i])
		print('ltree',ltree)
		rtree=postorder(num[i+1:])
		print('rtree',rtree)
		temp=[[num[i]]]
		for j in ltree:
			if len(temp)==1:
				temp[0]=temp[0].append(j)
			else:
				temp.append(num[i]+j)
			for j in rtree:
				temp
		if len(ltree)==0:
			for k in rtree:
				if len(temp)==1 and len(temp[0])==1:
					temp[0]=temp[0].append(k)
				else:
					temp.append(num[i]+k)
		i+=1
	return arr

print(postorder(inorder))
