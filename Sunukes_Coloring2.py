w, h, n = map(int, input().split())

rectangle = [[0 for _ in range(w)] for _ in range(h)]

for _ in range(n):
  x, y, a = map(int, input().split())
  if a == 1:
    for i in range(h):
      for j in range(x):
        rectangle[i][j] = 1
  elif a == 2:
    for i in range(h):
      for j in range(x, w):
        rectangle[i][j] = 1
  elif a == 3:
    for i in range(y):
      for j in range(w):
        rectangle[i][j] = 1
  elif a == 4:
    for i in range(y, h):
      for j in range(w):
        rectangle[i][j] = 1

cnt = 0
for elem1 in rectangle:
  for tf in elem1:
    if tf == 0:
      cnt += 1

print(cnt)
        






