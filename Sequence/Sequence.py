n = int(input())

lis = list(map(int, input().split()))


def f(p):
  total = 0
  cnt = 0
  for i, a in enumerate(lis):
    total += a

    if i % 2 == p and total <= 0:
      cnt += 1 - total
      total = 1
    elif i % 2 != p and total >=0:
      cnt += 1 + total
      total = -1
    else:
      continue

  return cnt

print(min(f(0),f(1)))

      