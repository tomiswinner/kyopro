n = int(input())
di = {}

for i in range(n):
  a = int(input())
  if a in di:
    di[a] += 1
  else:
    di[a] = 1

cnt = 0
for i in di.values():
  if i % 2 == 0:
    cnt += 0
  else:
    cnt += 1

print(cnt)

