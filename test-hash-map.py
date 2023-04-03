from hashmap import hash_map

# Создание хэш-карты
map = hash_map()

# Добавление элементов в хэш-карту
map['Russian'] = 'RUBLE'
map['Germany'] = 'EURO'
map['Turkey'] = 'LYRA'
print(len(map)) #выводит 3

# Получение элементов из хэш-карты
print(map['Russian']) # выводит 'RUBLE'
print(map['Turkey']) # выводит 'LYRA'

# Удаление элемента из хэш-карты
del map['Turkey']

# Получение количества элементов в хэш-карте
print(len(map)) # выводит 2

# Получение текущего коэффициента загрузки хэш-карты
print(map.current_load()) # выводит 0.2

# Очистка хэш-карты
map.clear()

# Проверка, что количество элементов в хэш-карте равно 0
print(len(map)) # выводит 0