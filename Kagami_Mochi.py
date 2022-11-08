n = int(input())
lis = []
for num in range(n):
  lis.append(int(input()))

sorted_lis = sorted(lis)
set_lis = set(lis)

print(len(set_lis))

