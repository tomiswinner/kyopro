li = [list(map(int, input().split())) for _ in range(3)]

edge = li[0][0] + li[2][0] + li[0][2] + li[2][2]
side= li[0][1] + li[1][0] + li[1][2] + li[2][1]

if edge/2 == side - 2 * li[1][1]:
  print("Yes")
else:
  print("No")

# edge = 2(a1 + b1) + 2(a3 + b3)
# side = (a1 + b1) + 2(a2 + b2) + (a3 + b3)
# center = a2 + b2
# うん、ごまかしAC
