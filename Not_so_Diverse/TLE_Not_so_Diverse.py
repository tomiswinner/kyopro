# TLE

n, k = map(int, input().split())
li = list(map(int, input().split()))

no_dup_li = list(set(li))

how_many = len(no_dup_li) - k

li_count = []

for ele in no_dup_li:
  li_count.append(li.count(ele))
# N^2になる、countが全体を走査するので。
# なので、1回の走査になるように、
# 先に配列を準備して、そこに割り振っていくのが正解
# 新しいものに出くわしたらdictに突っ込む、既知のものならdictに加算していくのが正解なのか
# ほんで、それをcollections.Counterは勝手にやってくれるんだなるほど

cnt = 0

for i in range(how_many):
  cnt += li_count.pop(li_count.index(min(li_count)))
# これもsum(sum(li_count.sort()[:how_many]))の方が良い

print(cnt)


