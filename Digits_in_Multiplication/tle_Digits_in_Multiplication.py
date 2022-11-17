# https://drken1215.hatenablog.com/entry/2019/09/16/221500
# 賢すぎるっしょ、、、

n = int(input())

divisor = []

for i in range(1, n+1):
  if n % i == 0:
    divisor.append(i)

print(divisor)
center = 0

if len(divisor) % 2 == 0:
  x,y = divisor[int(len(divisor)/2) - 1], divisor[int(len(divisor)/2)1]
  print(max(len(str(x)),len(str(y))))
else:
  x = divisor[int(len(divisor)/2) + 1]
  print(len(str(x)))


