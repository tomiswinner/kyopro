n, a, b = map(int, input().split())

ans = 0

for num in range(n+1):
	lis = [int(s) for s in str(num)]
	if a <= sum(lis) and sum(lis) <= b:
		ans += num

print(ans)

	
