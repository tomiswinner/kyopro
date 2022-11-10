
def yes_no():
  lis = ["dream","dreamer","erase","eraser"]
  s = input()
  ans = [""]
  while True:
    word = ans.pop()
    for num in range(4):
      added_word = word + lis[num]
      if len(added_word) > len(s):
        next
      if s[0:len(added_word)] == added_word:
        if len(s) == len(added_word):
          return "YES"
        ans.append(added_word)
    if len(ans) == 0:
      return "NO"
    
print(yes_no())

