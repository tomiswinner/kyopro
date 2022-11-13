a, b, ab, x, y = map(int, input().split())

# x for a, y for b

total = 0
  
while True:
  if x > 0 and y > 0:
    total += min(a+b, ab*2)
    x -= 1
    y -= 1
  elif x > 0:
    total += min(a, ab*2)
    x -= 1
  elif y > 0:
    total += min(b, ab*2)
    y -= 1
  if x == 0 and y == 0:
    break

print(total)








