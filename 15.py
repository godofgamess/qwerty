while True:
    count_numbers = int(input('Введите количество чисел: '))
    if 1 <= count_numbers <= 1000:
        break
    else:
        print('Число должно быть в диопозоне от 1 до 1000. Повторите ввод. \n ')
for num in range(1, count_numbers +1 ):
    while True:
        numbers = int(input('Введите число: '))
        if 1 <= numbers <= 30000:
            break
        else:
            print('Число должно быть в диопозоне от 1 до 30000. Повторите ввод. \n') #Похоже нужен список


print(min(numbers))