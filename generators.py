#Генераторы списков
qwerty1 = [i for i in range(0, 5)]
qwerty2 = [i for i in range(0, 5) if i % 2 == 0]
qwerty3 = [i if i % 2 == 0 else 'Нечетное' for i in range(0, 5)]


#Генераторы словарей
qwerty_dic = {i: 'Hello' for i in range(5)}
print(qwerty_dic)