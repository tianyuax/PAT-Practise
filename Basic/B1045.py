n=input()
a=raw_input()
ol = a.split(" ")
# n=10
# ol=[1,6,7,3,2,5,4,8,9,10]
a=[]
l=[]
for h in xrange(0,n):
	l.append(int(ol[h]))
for i in xrange(0,n):
	flag=0
	if flag==0:
		for x in xrange(1,i):
			if l[x]>l[i]:
				# print l[x]+">"+l[i]
				flag=1
				break
	if flag==0:
		for y in xrange(i+1,n):
			if l[y]<l[i]:
				# print l[y]+"<"+l[i]
				flag=1
				break
	if flag==0:
		a.append(l[i])


# print i
print len(a)
for k in xrange(0,len(a)):
	print a[k],
