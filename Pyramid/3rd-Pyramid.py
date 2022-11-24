n = int(input())

li = [list(map(int, input().split())) for _ in range(n)]

for x, y, h in li:
  if h <= 0:
    continue
  cx, cy,ch = x, y, h

for x in range(100+1):
  for y in range(100+1):
    # 仮の値から仮の高さHを算出
    predict_height = ch + abs(x - cx) + abs(y - cy)
    for px, py, ph in li:
      # 仮の高さHに対して,全ての入力が正しければOK、ダメならbreakして次
      if ph != max(predict_height - abs(x - px) - abs(y - py),0):
        break
    else:
      print(x, y, predict_height)


      
      

    
