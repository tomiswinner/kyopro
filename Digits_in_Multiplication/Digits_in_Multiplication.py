# https://drken1215.hatenablog.com/entry/2019/09/16/221500
# 賢すぎるっしょ、、、

n = int(input())

divisor = []

minimum = float('inf')

for a in range(1, int(n**0.5)+1):
  if n % a == 0:
    b = int(n / a)
    la = len(str(a))
    lb = len(str(b))
    minimum = min(minimum, max(la, lb))

print(minimum)

