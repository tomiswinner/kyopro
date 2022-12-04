import string

# https://stackoverflow.com/questions/453576/is-there-a-fast-way-to-generate-a-dict-of-the-alphabet-in-python
# fromkeys : dict.fromkeys({辞書のキー},{辞書のバリュー})
# string.ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'

s = input()
di = dict.fromkeys(string.ascii_lowercase, 1)

for char in s:
  di[char] -= 1

if 1 not in di.values():
  print("None")
else:
  for key, val in di.items():
    if val == 1:
      print(key)
      break


  
