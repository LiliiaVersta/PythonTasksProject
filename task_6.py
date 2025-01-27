# Изменение значений в вложенном списке

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row_index, row in enumerate(grid): # Внешний цикл for row in grid перебирает строки матрицы
    for col_index, value in enumerate(row): # Внутренний цикл for value in row обрабатывает элементы в каждой строке
        if value % 2 == 0:  # Если значение чётное
            grid[row_index][col_index] = value * 2
        else:  # Если значение нечётное
            grid[row_index][col_index] = 0

for row in grid:
    print(row)