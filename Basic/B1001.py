#n= 3

n=input()
c=0
while n!=1:
	if n%2==0:
		n=n/2
	else :
		n=(3*n+1)/2
	c=c+1

print c
