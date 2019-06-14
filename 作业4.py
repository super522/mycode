a=input()
a=int(a)
b=input()
b=int(b)
c=input()
c=int(c)
d=input()
d=int(d)


hhh=[a,b,c,d]

for i in range(0,len(hhh)-1):
	xxx = i
	for j in range(i+1,len(hhh)):
		if hhh[xxx]<hhh[j]:
			xxx=j
	hhh[i],hhh[xxx]=hhh[xxx],hhh[i]
print(hhh)