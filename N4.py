string = input("Введите строку: ")
dct = {a: 0 for a in string.split()}
lst = list(string.split())
print("\n")
for word in dct:
    print(word,":", lst.count(word))