# Faktoriális kiszámítása:

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Tesztelés
n = 5
print(f"A(z) {n} faktoriálisa: {factorial(n)}")

# Euklideszi algoritmus:

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Tesztelés
x, y = 54, 24
print(f"A(z) {x} és {y} legnagyobb közös osztója: {gcd(x, y)}")

# Átlagszámítás tömb nélkül:

sum_of_grades = 0
count_of_grades = 0
while True:
    grade = int(input("Adjon meg egy érdemjegyet (0 befejezi): "))
    if grade == 0:
        break
    sum_of_grades += grade
    count_of_grades += 1
    print(f"Átlag: {sum_of_grades / count_of_grades}")

print(f"Végleges átlag: {sum_of_grades / count_of_grades}")

#Ritka mátrix:

import random

def create_matrix(rows, columns, density):
    total_elements = rows * columns
    non_zero_elements = int(total_elements * density)
    matrix = [[0] * columns for _ in range(rows)]
    non_zero_indices = random.sample(range(total_elements), non_zero_elements)
    for index in non_zero_indices:
        row = index // columns
        column = index % columns
        matrix[row][column] = random.randint(1, 100)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

def is_sparse(matrix, threshold=0.2):
    total_elements = sum(len(row) for row in matrix)
    non_zero_elements = sum(1 for row in matrix for elem in row if elem != 0)
    density = non_zero_elements / total_elements
    return density < threshold

rows = int(input("Adja meg a sorok számát: "))
columns = int(input("Adja meg az oszlopok számát: "))
density = float(input("Adja meg a sűrűséget (0 és 1 között): "))

matrix = create_matrix(rows, columns, density)
print("A mátrix:")
print_matrix(matrix)

if is_sparse(matrix):
    print("A mátrix ritka.")
else:
    print("A mátrix nem ritka.")

#Alsóháromszög mátrix implementációja:

def create_lower_triangular_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            matrix[i][j] = random.randint(1, 100)
    return matrix

# Tesztelés
n = int(input("Adja meg a mátrix méretét: "))
lower_triangular_matrix = create_lower_triangular_matrix(n)
print("Az alsóháromszög mátrix:")
print_matrix(lower_triangular_matrix)
