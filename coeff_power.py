a=input()
a=a+"+"
coef=0
power=0
neg=False
exp=False
for i in a:
	if i==' ':
		continue
	if i=='-':
		neg=True
		print("num=",coef,"pow=",power)
		var=False
		exp=False
		coef=0
		power=0
		continue
	if i=='+':
		neg=False
		print("num=",coef,"pow=",power)
		var=False
		exp=False
		coef=0
		power=0
		continue

	if ord(i)>47 and ord(i)<58:
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

