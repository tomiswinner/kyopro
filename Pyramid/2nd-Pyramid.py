
n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

for x, y, h in li:
  if h > 0:
    px, py, ph = x, y, h
    break
  
for cx in range(100+1):
  for cy in range(100+1):
    ch = ph + abs(cx - px) + abs(cy - py)
    for x, y, h in li:
      predict = max(0, ch - abs(cx - x) - abs(cy - y))
      if predict != h:
        break
    else:
      print(cx, cy, ch)


  
