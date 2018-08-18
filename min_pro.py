num=[int(i) for i in input().split()]

pos_pro=1
neg_pro=0
zero=1
pminimum=num[0]
nmax=num[0]
for i in num:
	if i<0:
		if neg_pro==0:
			neg_pro=i
		else:
			neg_pro*=i
		if i>nmax or nmax>0:
			nmax=i
	elif i>0:
		pos_pro*=i
		if i<pminimum or pminimum<0:
			pminimum=i
		
	else:
		zero=0

if neg_pro<0:
	print(neg_pro*pos_pro)
else:
	if nmax<0:
		print(neg_pro//nmax*pos_pro)
	else:
		print(zero*pminimum)
