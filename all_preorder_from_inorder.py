inorder=[int(i) for i in input("Inorder:").split()]


def postorder(num,arr):
	print(num,'	',arr)
	i=0
	while(i<len(num)):
		arr.append(num[i])
		postorder(num[:i],arr)
		postorder(num[i+1:],arr)
		if len(arr)==len(inorder):
			print("mew",arr)
		i+=1
		print('len of num:',len(num))
#		if len(num)==len(inorder):
#			print('holaaa')
#			arr=[]
		if i>0 and i<len(inorder)-1:
			del(arr[-1])
			del(arr[-1])
		else:
			del(arr[-1])
		print('cawcaw		',arr)

postorder(inorder,[])
