#! -*- coding:utf-8 -*-


for i in range(1,10):
	#print("       "*(i-1),end=" ")
	for j in range(1,i+1):
		x=i*j
		print("%d*%d=%2d" %(i,j,x),end=" ")
	print("	")


