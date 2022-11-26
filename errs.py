try:
  a = int(input('Введи число: '))
  b = 6 / 0
except (ZeroDivisionError, ValueError) as err:
  print(err)
else:
  print(a + 4)
finally:
  print('Программа завершилась')