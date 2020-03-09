# Rad sa matricama

matrica = [[1,2,3], [4,5,6], [7,8,9]]
print(matrica)
for row in matrica:
    print(row)
print(matrica[1][1])

num_of_rows = len(matrica) # 3
num_of_columns = len(matrica[0]) # 3

for i in range(num_of_rows):
    for j in range(num_of_columns):
        if matrica[i][j] % 2 == 0:
            matrica[i][j] = matrica[i][j] ** 2
        else:
            matrica[i][j] *= (-1)
print(matrica)

zbir = 0
# Kreirati kvadratnu matricu i naci zbir elemenata sa glavne dijagonale
for i in range(num_of_rows):
    for j in range(num_of_columns):
        if i == j:
            zbir += matrica[i][j]

# Sabrati dvije matrice
matrica_1 = [[1,3], [2,4]]
matrica_2 = [[5,6], [7,2]]
matrica_3 = [[0,0], [0,0]]

num_of_rows = len(matrica_1)
num_of_columns = len(matrica_1[0])

for i in range(num_of_rows):
    for j in range(num_of_columns):
        matrica_3[i][j] = matrica_1[i][j] + matrica_2[i][j]
print(matrica_3)

matrix = [[0 for i in range(0, 3)] for j in range(0, 3)]

matrix2 = [[0]*3 for i in range(3)]


matrix3 = []
for i in range(3):
    matrix3.append([0] * 3)

matrix4 = []
broj_vrsta = int(input("Unesite broj vrsta:"))
broj_kolona = int(input("Unesite broj kolona:"))
for i in range(broj_vrsta):
    matrix4.append([0] * broj_kolona)

for i in range(broj_vrsta):
    for j in range(broj_kolona):
        element = int(input(f"Unesite element na poziciji [{i+1},{j+1}]:"))
        matrix4[i][j] = element

print(matrix4)