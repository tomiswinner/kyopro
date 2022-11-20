n = int(input())
li = list(map(int, input().split()))

old = li[0]
state = "checking"
cnt = 0

for new in range(1, len(li)):
  if state == "checking":
    if old <= li[new]:
      state = "increasing"
    else:
      state = "decreasing"
  elif state == "increasing":
    if not (old <= li[new]):
      cnt += 1
      state = "checking"
  else:
    if not (old >= li[new]):
      cnt += 1
      state = "checking"
  old = li[new]

print(cnt)


      




  







