inorder=[int(i) for i in input("inorder:").split()]
pre=[int(i) for i in input("preorder:").split()]

p=-1
def postorder(pre_ini,pre_end):
	global p
	p+=1
	root=inorder.index(pre[p])


	if root-pre_ini!=0:
		postorder(pre_ini,root-1)
	if pre_end-root!=0:
		postorder(root+1,pre_end)
	print(inorder[root],end=' ')

print("Postorder:",end=' ')
postorder(0,len(pre)-1)
print()
