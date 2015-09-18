

# a=-1000000
# b=9

x=raw_input()
ol = x.split(" ")

a=int(ol[0])
b=int(ol[1])
flag=0
c=a+b
if c<0:
	c=-c
	flag=1

l=[]
if c==0:
	l.append("0")
while c!=0:
	l.append(str(c%10))
	c=c/10
n=len(l)
s=""

for i in range(0,n):
	if (i%3==0 and i!=0):
		s=","+s
	s=l[i]+s
	
if flag==1:
	s="-"+s



print s



