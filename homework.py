import random


def shift_columns_left(matrix, shift_amount):
    if not matrix or not matrix[0]:
        return matrix
    n = len(matrix)
    m = len(matrix[0])
    shifted = [row[:] for row in matrix]

    shift_amount = shift_amount % m
    if shift_amount == 0:
        return shifted

    for i in range(n):
         shifted[i] = shifted[i][shift_amount:] + shifted[i][:shift_amount]
    return shifted

def print_matrix(matrix, title=""):
     if title:
        print(f"\n{title}:")
     for row in matrix:
        for element in row:
            print(element, end='\t')
        print()

matrix = [[random.randint(1, 9) for i in range(8)] for j in range(9)]

print("\nИсходная матрица (9 строк, 8 столбцов):")
print_matrix(matrix)

while True:
   try:
       shift_amount = int(input("Введите количество позиций для сдвига столбцов влево:"))
       if shift_amount < 0:
           print("Пожалуйста введите положительное число.")
           continue
       shifted = shift_columns_left(matrix, shift_amount)

       print(f"\nРезультат сдвига на {shift_amount} позицию(и) влево:")
       print_matrix(shifted)


       print("\n" + "=" * 40)
       choice = input("Хотите выполнить еще один сдвиг? (да/нет): ").lower()
       if choice not in ['да', 'д', 'yes', 'y']:
           break

   except ValueError:
         print("Ошибка! Пожалуйста, введите целое число.")


def shift_columns_right(matrix, shift_amount):

    if not matrix or not matrix[0]:
        return matrix

    m = len(matrix[0])
    shift_amount = shift_amount % m

    if shift_amount == 0:
        return [row[:] for row in matrix]


    return [row[-shift_amount:] + row[:-shift_amount] for row in matrix]


def print_matrix(matrix, title=""):

    if title:
        print(f"\n{title}:")
    for row in matrix:
        for element in row:
            print(element, end='\t')
        print()



matrix = [[random.randint(1, 9) for i in range(8)] for j in range(9)]
print_matrix(matrix)


while True:
    try:
        print("\n" + "=" * 40)
        shift_amount = int(input("Введите количество позиций для сдвига столбцов вправо: "))

        if shift_amount < 0:
            print("Пожалуйста введите положительное число")
            continue


        shifted = shift_columns_right(matrix, shift_amount)


        print(f"\nРезультат сдвига на {shift_amount} позиции вправо:")
        print_matrix(shifted)


        print("\n" + "=" * 40)
        choice = input("Хотите выполнить еще один сдвиг? (да/нет): ").lower()
        if choice not in ['да', 'д', 'yes', 'y', '+']:
            break

    except ValueError:
        print("Пожалуйста введите целое число")