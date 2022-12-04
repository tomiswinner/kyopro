n, c, k = map(int, input().split())
li = sorted([int(input()) for _ in range(n)])

cnt = 0

while True:
  first = li.pop(0)
  
# 最初に乗せる人は時間限界までまたせる
  leave_time = first + k
  capacity = c - 1
  
  # 定員に達する or leave_time までに来る人がいない場合終わる
  while capacity > 0:
    if len(li) == 0 or leave_time < li[0]:
      break
    else:
      li.pop(0)
      capacity -= 1

  cnt += 1

  if len(li) == 0:
    break

print(cnt)

  

  
