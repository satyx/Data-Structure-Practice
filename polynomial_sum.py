class node:
	def __init__(self,coeff,exp):
		self.coef=coeff
		self.power=exp
		self.next=None

head_x,head_y=None,None

a=input()
a=a+"+"
coef=0
power=0
neg=False
exp=False
start=False
for i in a:
	if i==' ':
		continue
	if i=='-':
		neg=True
		if start==False:
			continue
		nd=node(coef,power)
		nd.next=head_x
		head_x=nd
		var=False
		exp=False
		coef=0
		power=0
		continue
	if i=='+':
		neg=False
		if start==False:
			continue
		nd=node(coef,power)
		nd.next=head_x
		head_x=nd
		var=False
		exp=False
		coef=0
		power=0
		continue

	if ord(i)>47 and ord(i)<58:
		start=True
		if exp==True:
			power=10*power+int(i)
		else:
			if neg==True:
				coef=coef*(-10)-int(i)
			else:
				coef=coef*10+int(i)
		continue
	if i=="x":
		continue
	if i=="^":
		exp=True
		continue

a=input()
a=a+"+"
coef=0
power=0
neg=False
exp=False
start=False
for i in a:
	if i==' ':
		continue
	if i=='-':
		neg=True
		if start==False:
			continue
		nd=node(coef,power)
		nd.next=head_y
		head_y=nd
		var=False
		exp=False
		coef=0
		power=0
		continue
	if i=='+':
		neg=False
		if start==False:
			continue
		nd=node(coef,power)
		nd.next=head_y
		head_y=nd
		var=False
		exp=False
		coef=0
		power=0
		continue

	if ord(i)>47 and ord(i)<58:
		start=True
		if exp==True:
			power=10*power+int(i)
		else:
			if neg==True:
				coef=coef*(-10)-int(i)
			else:
				coef=coef*10+int(i)
		continue
	if i=="x":
		continue
	if i=="^":
		exp=True
		continue

result=None

temp_x,temp_y=head_x,head_y

while temp_x!=None and temp_y!=None:
	nd=node(temp_x.coef+temp_y.coef,temp_x.power)
	nd.next=result
	result=nd
	temp_x=temp_x.next
	temp_y=temp_y.next

while temp_x!=None:
	nd=node(temp_x.coef,temp_x.power)
	nd.next=result
	result=nd
	temp_x=temp_x.next



print("result :",end=' ')
temp=result
print(temp.coef,"x^",temp.power,sep='',end=' ')
temp=temp.next

while temp!=None:
	if temp.coef>=0:
		print("+ ",temp.coef,"x^",temp.power,sep='',end=' ')
	else:
		print("- ",(-1)*temp.coef,"x^",temp.power,sep='',end=' ')
	temp=temp.next
print()
