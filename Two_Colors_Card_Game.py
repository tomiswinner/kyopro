n = int(input())

dic = {}

for _ in range(n):
  s = input()
  if s in dic:
    dic[s] += 1
  else:
    dic[s] = 1
  
m = int(input())

for _ in range(m):
  t = input()
  if t in dic:
    dic[t] -= 1
  else:
    dic[t] = -1

print(max(0,max(list(dic.values()))))



