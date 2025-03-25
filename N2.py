dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}
keys=set(dct.keys())
values=set(dct.values())
combined_set=keys.union(values)
print("Множество ключей: ", keys)
print("Множество значений: ", values)
print("Объединение множеств: ", combined_set)