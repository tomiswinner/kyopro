a, b, c = map(int, input().split())

li = sorted([a,b,c]) 

cnt = 0

while True:
  if li[0] == li[1] == li[2]:
    break
  elif li[0] == li[1]:
    li[0] += 1
    li[1] += 1
  else:
    li[0] += 2
  cnt += 1
  li = sorted(li)
  
print(cnt)   
