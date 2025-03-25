list_of_numbers = [a for a in input("Введите числа через пробел: ").split()]
power = input("Введите степень: ")
power_is_negative = False
if not power.isdigit() and not power.lstrip('-').isdigit():
    print("Ошибка: степень не является целым числом")
    quit()
elif not power.isdigit() and power.lstrip('-').isdigit():
    print("Предупреждение: степень отрицательная, строковые элементы не будут умножаться")
    power_is_negative = True
counter = 0
for number in list_of_numbers:
    if not number.isdigit() and not number.lstrip('-').isdigit() and not power_is_negative:
        number=number*int(power)
        list_of_numbers[counter] = number
        counter += 1
    elif (number.isdigit()) or (not number.isdigit() and number.lstrip('-').isdigit()):
        number = int(number)
        list_of_numbers[counter] = number**int(power)
        counter += 1
print("Вывод:", *list_of_numbers, sep = " ")