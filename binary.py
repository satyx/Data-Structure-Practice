n=int(input())
q=['1']
while n>0:
	n-=1
	x=q.pop()
	print(x)
	q.insert(0,x+'0')
	q.insert(0,x+'1')
	
