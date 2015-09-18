# n=5
# l=("1","3","2","4","5")
n=input()
a=raw_input()
l = a.split(" ")

l2=sorted(l)

print l2

l3=[]

for x in xrange(0,n):
	if l[x]==l2[x]:
		l3.append(l[x])
print len(l3)
for k in xrange(0,len(l3)):
	print l3[k],
