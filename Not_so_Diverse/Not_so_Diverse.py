# TLE

n, k = map(int, input().split())
li = list(map(int, input().split()))

no_dup_li = list(set(li))

how_many = len(no_dup_li) - k

li_count = []

for ele in no_dup_li:
  li_count.append(li.count(ele))
# N^2になる、countが全体を走査するので。
# なので、

cnt = 0

li_count = sorted(li_count)
cnt = sum(li_count[:how_many])

print(cnt)


