n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(m)]
ans = dict.fromkeys(range(1,n+1), 0)

for road in li:
  ans[road[0]] += 1
  ans[road[1]] += 1


for city in list(ans.items()):
  print(city[1])
