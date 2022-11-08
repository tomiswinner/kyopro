def check():
  n, y = map(int, input().split())

  # 10000円
  for i in range(n+1):
    # 5000円
    for j in range(n+1-i):
      if 10000 * i + 5000 * j + 1000 * (n-i-j) == y:
        print("{} {} {}".format(i,j,n-i-j))
        return False
  
  return True

if check():
  print("-1 -1 -1")
    
