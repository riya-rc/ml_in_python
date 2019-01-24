n=(int)(input())


for i in range(n):
	for j in range(n):
		print(n-min(i, j, n-i-1,n-j-1),end=" ")
	print("\n")
