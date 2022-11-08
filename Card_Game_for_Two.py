n = int(input())

lis = list(map(int, input().split()))
lis = sorted(lis)

alice = 0
bob = 0

for num in range(n):
	if num % 2 == 0:
		alice += lis.pop()
	else:
		bob += lis.pop()

print(alice -  bob)




