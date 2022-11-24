n = int(input())
li = list(map(int, input().split()))

cnt = 0

for i in li:
  if i % 2 != 0:
    cnt += 1

if cnt % 2 == 0:
  print("YES")
else:
  print("NO")

# even 同士は何個あろうが消せる
# odd は　偶数じゃないと消せない
