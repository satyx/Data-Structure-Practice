def modular(a,b,c):
	if b==1:	
		return a%c
	if b==0:
		return 1

	x=modular(a,b//2,c);
	if(b%2==0):
		return (x*x)%c
	else:
		return (x*x*a)%c


print("Modular Exponential ALgorithm")
print("a^b%c=d");

a=int(input("a="));

b=int(input("b="));

c=int(input("c="));

d=modular(a,b,c);
print("d=",d)

