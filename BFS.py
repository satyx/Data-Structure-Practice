tree=[]
stack=[]
def add_node(data):
	global tree
	tree.append(data)

def dfs_inorder(key):
	global tree
	if 2*key<=len(tree):
		inorder(2*key)
	print(tree[key-1])
	if 2*key+1<=len(tree):
		inorder(2*key+1)
def dfs_preorder(key):
	global tree
	print(tree[key-1])
	if 2*key<=len(tree):
		preorder(2*key)
	if 2*key+1<=len(tree):
		preorder(2*key+1)
def dfs_postorder(key):
	global tree
	if 2*key<=len(tree):
		postorder(2*key)
	if 2*key+1<=len(tree):
		postorder(2*key+1)
	print(tree[key-1])

while True:
	ch=int(input("0.Exit\n1.Input\n2.BFS\n3.DFS\nChoice:"))
	if ch==0:
		break
	if ch==1:
		add_node(int(input("Enter data:")))
	if ch==2:
		q=[1]
		key=1
		while len(q)!=0:
			print(tree[q[0]-1])
			del(q[0])
			if 2*key+1<=len(tree):
				q.append(2*key)
				q.append(2*key+1)
			elif 2*key<=len(tree):
				q.append(2*key)
			key+=1
	if ch==3:
		ch1=int(input("1.Inorder\n2.Preorder\n3.Post order\nChoice:"))
		if ch1==1:
			dfs_inorder(1)
		elif ch1==2:
			dfs_preorder(1)
		elif ch1==3:
			dfs_postorder(1)

