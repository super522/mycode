ls=[11,12,13,14,15,16]
def hyh(ls,x):
	l=0
	h=5
	while l<=h:
		i=(l+h)//2
		print(l,h,i)
		if ls[i]>x:
			h=i+1
		elif ls[i]<x:
			l=i-1
		elif ls[i]==x:
			i=l
			return i
print(hyh(ls,14))