while True:
 print("введите номер четверти от 1 до 4")
 num = input()
 try:
  dnum = int(num)
 except Exception:
  print("этот символ не цифра")
 else:
  if(dnum in range(1,4)):
   break
  else: print("цифра выходит за диапазон четвертей")

if dnum == 1: print("все возможные значения X и Y больше нуля")
if dnum == 2: print("все возможные значения X меньше нуля и Y больше нуля")
if dnum == 3: print("все возможные значения X и Y меньше нуля")
if dnum == 4: print("все возможные значения Y меньше нуля и X больше нуля")