#1
#matrix = [[1, 2, 3], [5, 7, 8], [9, 11, 13]]  
#for j in range(len(matrix[0])):  
#    all_odd = True
#    for i in range(len(matrix)):  
#        if matrix[i][j] % 2 == 0:  
#            all_odd = False
#            break
#    if all_odd:
#        print("Номер столбца:", j)
#        break
#else:
#    print("0")  
#2
#matrix = [[1, 5, 3], [9, 2, 8], [4, 7, 6]]
#for row in matrix:
#    min_val = min(row)
#    max_val = max(row)
#    min_idx = row.index(min_val)
#    max_idx = row.index(max_val)
#    row[min_idx], row[max_idx] = row[max_idx], row[min_idx]
#print(matrix)    
#3
#matrix = [[1, 5, 3], [9, 2, 8], [4, 7, 6]]
#min_val = min(min(row) for row in matrix)
#max_val = max(max(row) for row in matrix)
#min_row = [i for i, row in enumerate(matrix) if min_val in row][0]
#max_row = [i for i, row in enumerate(matrix) if max_val in row][0]
#matrix[min_row], matrix[max_row] = matrix[max_row], matrix[min_row]
#print(matrix)
#4
#matrix = [[1, 2], [3, 4], [5, 6]]
#matrix.reverse()  
#print(matrix)
#5
#matrix = [[1, 5, 3], [9, 2, 8], [4, 7, 6]]
#min_val = min(min(row) for row in matrix)
#for i, row in enumerate(matrix):
#    if min_val in row:
#        del matrix[i]
#        break
#print(matrix)
#6
#matrix = [[1, 5, 3], [9, 2, 8], [4, 7, 6]]
#max_val = max(max(row) for row in matrix)
#for j in range(len(matrix[0])):
#    for i in range(len(matrix)):
#        if matrix[i][j] == max_val:
#            # удаляем столбец j
#            for row in matrix:
#                del row[j]
#            break
#    break
#print(matrix)
#7
#matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#for row in matrix:
#    row.reverse()  
#print(matrix)
#8
#matrix = [[1, 5, 3], [9, 2, 8], [4, 7, 6]]
#max_val = max(max(row) for row in matrix)
#for i, row in enumerate(matrix):
#    if max_val in row:
#        matrix.insert(i, row)  
#        break
#print(matrix)
#9
#matrix = [[1, 5, 3], [9, 2, 8], [4, 7, 6]]
#for j in range(len(matrix[0])):
#    col = [matrix[i][j] for i in range(len(matrix))]  
#    avg = sum(col) / len(col)
#    count = sum(1 for x in col if x > avg)
#    print(f"Столбец {j}: {count} элементов > среднего")
#10
#matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
#m, n = len(matrix), len(matrix[0])
#top_left = [row[:n//2] for row in matrix[:m//2]]
#bottom_right = [row[n//2:] for row in matrix[m//2:]]
#for i in range(m//2):
#    matrix[i][:n//2] = bottom_right[i]
#    matrix[i+m//2][n//2:] = top_left[i]
#print(matrix)
#11
#matrix = [[1, 5, 3], [9, 2, 8], [4, 7, 6], [10, 11, 12]]
#for i in range(1, len(matrix), 2):  
#    avg = sum(matrix[i]) / len(matrix[i])
#    print(f"Строка {i}: среднее = {avg}")
#12
#matrix = [[1, 5, 3], [9, 2, 8], [4, 7, 6]]
#max_sum = max(sum(row) for row in matrix)
#max_row_idx = [i for i, row in enumerate(matrix) if sum(row) == max_sum][0]
#print(f"Номер строки: {max_row_idx}, сумма: {max_sum}")
#13
#matrix = [[1, 5, 3], [9, 2, 8], [4, 7, 6]]
#min_val = min(min(row) for row in matrix)
#zero_row = [0] * len(matrix[0])  # строка из нулей
#for i, row in enumerate(matrix):
#    if min_val in row:
#        matrix.insert(i, zero_row)
#        break
#print(matrix)
#14
#matrix = [[2, 4, 6], [1, 8, 10], [12, 14, 16]]
#last_even_row = 0
#for i in range(len(matrix)):
#    if all(x % 2 == 0 for x in matrix[i]):
#        last_even_row = i
#print(last_even_row)
#15
#matrix = [[1, -2, 3], [4, 5, -6], [7, 8, 9]]
#pos_cols = [j for j in range(len(matrix[0])) if all(matrix[i][j] > 0 for i in range(len(matrix)))]
#if pos_cols:
#    last_pos_col = pos_cols[-1]
#    # меняем 1-й и last_pos_col столбцы
#    for i in range(len(matrix)):
#        matrix[i][0], matrix[i][last_pos_col] = matrix[i][last_pos_col], matrix[i][0]
#print(matrix)
