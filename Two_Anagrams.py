s = input()
t = input()

s = sorted(s)
t = sorted(t)[::-1]

if s < t :
  print("Yes")
else:
  print("No")
