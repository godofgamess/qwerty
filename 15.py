numbers_list = []


while True:
    count_numbers = int(input('Введите количество чисел: '))
    if 1 <= count_numbers <= 1000:
        break
    else:
        print('Число должно быть в диопозоне от 1 до 1000. Повторите ввод. \n ')

for num in range(1, count_numbers + 1):
    while True:
        number = int(input('Введите число: '))
        if 1 <= number <= 30000:
            if (number % 10 == 4):
                numbers_list.append(number)
            break
        else:
            print('Число должно быть в диопозоне от 1 до 30000. Повторите ввод. \n')



print(min(numbers_list))

