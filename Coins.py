a = int(input())
b = int(input())
c = int(input())
x = int(input())

cnt = 0

for num1 in range(a+1):
	for num2 in range(b+1):
		for num3 in range(c+1):
			if 500*num1 + 100*num2 + 50*+num3 == x:
				cnt += 1

print(cnt)
