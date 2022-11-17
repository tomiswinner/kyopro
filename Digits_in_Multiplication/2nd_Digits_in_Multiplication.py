n = int(input())

# a,b = n, then a <= b is valid
# 約数はルートで折り返すからルートまででいいのか(2乗)
mini = float('inf')
for a in range(1,int(n**0.5)+1):
  if n % a == 0:
    b = int(n/a)
    mini = min(mini, max(len(str(a)), len(str(b))))

print(mini)
