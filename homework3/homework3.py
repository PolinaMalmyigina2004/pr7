def convert_to_base_3(a, d=""):
  if a == 0:
    return d
  if a > 0:
    x = a % 3
    a = a // 3
    d = str(x) + d
    return convert_to_base_3(a, d)
  else:
    return "-" + convert_to_base_3(-a, d) 

print("")
try:
  a = int(input("Введите число в десятичной системе счисления: "))
  result = convert_to_base_3(a)
  print("Число в троичной системе счисления: ", result)
except ValueError:
  print('Это не число. Выходим.')
