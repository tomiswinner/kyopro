n = int(input())
li = list(map(int, input().split()))

ans = []

for remainder in [0,1]:
  cnt = 0
  total = 0
  for num, ele in enumerate(li):
    total += ele
    if num % 2 == remainder and total >= 0:
      cnt += abs(-1 - total)
      total = -1
    elif num % 2 != remainder and total <= 0:
      cnt += abs(1 - total)
      total = 1
    else:
      continue
  ans.append(cnt)

print(min(ans))






    

    
