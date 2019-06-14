hhh=[4,9,2,8,1]
i=len(hhh)
j=0
while i!=1:
	while j!=i-1:
		if hhh[j]<hhh[j+1]:
			hhh[j],hhh[j+1]=hhh[j+1],hhh[j]
		j=j+1
	print(hhh)
	if j==i-1:
		i=i-1
print(hhh)