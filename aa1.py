J = 0.0000001
y = input("give me a member")
y = int(y)
x = 3
b = 0.1
while b>J:
	x = (y/x+x)/2
	b = abs(y-x*x)
print(x)


