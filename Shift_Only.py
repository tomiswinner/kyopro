n = input()

lis = list(map(int, input().split()))
cnt = 0


while all(e % 2 == 0 for e in lis):
	cnt += 1
	for i, e in enumerate(lis):
		lis[i] = e / 2

print(cnt)
	

		

