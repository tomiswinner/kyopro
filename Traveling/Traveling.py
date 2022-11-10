n = int(input())

t_old = 0
x_old = 0
y_old = 0
flag = True

for _ in range(n):
  t, x, y = map(int, input().split())
  move = t - t_old
  d = abs(x - x_old) + abs(y - y_old)

  if d <= move and move % 2 == d % 2:
    t_old = t
    x_old = x
    y_old = y
  else:
    flag = False
    break

if flag:
  print("Yes")
else:
  print("No")
