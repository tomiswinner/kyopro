
n, k = map(int, input().split())

li = list(map(int, input().split()))

diff = len(set(li)) - k

dic = {}

for ele in li:
  if ele in dic:
    dic[ele] = dic[ele] + 1
  else:
    dic[ele] = 1


dic_sort = sorted(dic.values())
print(sum(dic_sort[:diff]))

