n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

stack = [[0,0]]
while True:
  tmp_coor = stack.pop()
  for x in [-1,1]:
    for y in [-1,1]:
      if 0 <= tmp_coor[0] + x and 0 <= tmp_coor[0] + y and tmp_coor[0] + x < n and tmp_coor[0] + y < n:
        stack.append([tmp_coor[0] + x, tmp_coor[1] + y])

# give up
