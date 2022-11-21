# https://find-best-practice.com/2021/07/24/%E3%80%90python%E3%80%91atcoder-beginner-contest-093-%E8%A7%A3%E7%AD%94/
# すげー

a, b, c = map(int, input().split())

cnt = 0
li = sorted([a,b,c])

while True:
  if li[0] == li[1] == li[2]:
    break
  li = sorted(li)
  if li[0] < li[1]:
    li[0] += 2
  else:
    li[0] += 1
    li[1] += 1
  cnt += 1

print(cnt)

  

