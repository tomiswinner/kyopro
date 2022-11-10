def loop():
  li = ["dream","dreamer","erase","eraser"]
  s = input()[::-1]

  for i, el in enumerate(li):
    li[i] = el[::-1]

  while len(s) != 0:
    flag = False
    for el in li:
      if s[:len(el)] == el:
        s = s[len(el):]
        flag = True
    if flag:
      continue
    else:
      return "NO"

  return "YES"

print(loop())

