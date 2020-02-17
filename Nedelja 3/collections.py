lista = [1, 2, 3, "abc", [1,2]]
for element in lista:
    print(element)

print(lista[::-1])

# Naci proizvod jednocifrenih brojeva unutar liste sastavljene od cijelih brojeva,
# Broj 0 preskociti.
lista = [1, 10, 2, 7, 23, -10]
proizvod = 1
for element in lista:
    if element < 10 and element > -10 and element != 0:
        proizvod *= element
print(proizvod)

# Naci proizvod kubova nepranih brojeva liste
lista = [2, 3, 7, 4]
proizvod = 1
for broj in lista:
    if broj % 2 != 0:
        proizvod = proizvod * broj ** 3

print(proizvod)

# Liste by val/by ref

list_a = [1,2,3,4]
# list_b = list_a
list_b = list_a.copy()
list_b[0] = 10
print(list_a)
print(list_b)