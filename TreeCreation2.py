inorder=[int(i) for i in input("Inorder:").split()]
post=[int(i) for i in input("Post Order:").split()]
tree=[None for i in range(pow(2,len(post))-1)]

key=len(post)-1

def tree_creation(a,b,curr):
	global key,tree
	if b-a==0:
		return
	pos=inorder.index(post[key])
	
	if b-pos>0:
		key-=1
		tree[2*curr]=post[key]
		tree_creation(pos+1,b,2*curr+1)
	if pos-a>0:
		key-=1
		tree[2*curr-1]=post[key]
		tree_creation(a,pos-1,2*curr)

tree[0]=post[-1]
tree_creation(0,len(post)-1,1)
while tree[-1]==None:
	del tree[-1]
print(tree)
