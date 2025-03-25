list1 = [a for a in input("Введите элементы первого списка через пробел: ").split()]
list2 = [b for b in input("Введите элементы второго списка через пробел: ").split()]
set1 = set(list1)
set2 = set(list2)
print("Общие элементы, полученные оператором '&':", *sorted(set1 & set2), sep = " ")
print("Общие элементы, полученные методом '.intersection()':", *sorted(set1.intersection(set2)), sep = " ")