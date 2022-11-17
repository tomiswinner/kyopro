n = int(input())
height_dat = [list(map(int, input().split())) for _ in range(n)]

# found the coordinate where h is not negative
for x, y, h in height_dat:
  if h == 0:
    continue
  px, py, ph = x, y, h
  break

for cx in range(100+1):
  for cy in range(100+1):
    ch = ph + abs(px - cx) + abs(py - cy)

    for x, y, h in height_dat:
      predict = max(0, ch - abs(x - cx) - abs(y - cy))
      if h != predict:
        break
    else:
      # if this assumption is correct
      print(cx, cy, ch) 

