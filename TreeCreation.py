inorder=[int(i) for i in input("Enter Inorder:").split()]
pre=[int(i) for i in input("Enter Preorder:").split()]

tree=[None for i in range(pow(2,len(inorder))-1)]

key=0
def tree_create(a,b,curr):
	global key
	if b-a==0:
		return
	pos=inorder.index(pre[key])
	if pos-a>0:
		key+=1
		tree[2*curr-1]=pre[key]
		tree_create(a,pos-1,2*curr)
	if b-pos>0:
		tree[2*curr]=pre[key+1]
		key+=1
		tree_create(pos+1,b,2*curr+1)

tree[0]=pre[0]
tree_create(0,len(pre)-1,1)


while tree[-1]==None:
	del tree[-1]
print(tree)
