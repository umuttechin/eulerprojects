if __name__ == "__main__":
    with open("matrix") as e:
        numbers = e.read().split()
    matrix = [numbers[x:x+100] for x in range(0, len(numbers), 20)]
    cross_product = []
    
    for row_index in range(0,len(matrix)):
        for column_index in range(0, len(matrix) - 3):
            cross = int(matrix[row_index][column_index]) * int(matrix[row_index][column_index + 1]) * int(matrix[row_index][column_index + 2]) * int(matrix[row_index][column_index + 2])
            cross_product.append(cross)

    for row_index in range(0,len(matrix) - 3):
        for column_index in range(0, len(matrix)):
            cross = int(matrix[row_index][column_index]) * int(matrix[row_index + 1][column_index]) * int(matrix[row_index + 2][column_index]) * int(matrix[row_index + 3][column_index])
            cross_product.append(cross)

    for row_index in range(0,len(matrix) - 3):
        for column_index in range(0, len(matrix) - 3):
            cross = int(matrix[row_index][column_index]) * int(matrix[row_index + 1][column_index + 1]) * int(matrix[row_index + 2][column_index + 2]) * int(matrix[row_index + 3][column_index + 3])
            cross_product.append(cross)

    for row_index in range(0, len(matrix) - 3):
        for column_index in range(len(matrix), 2 ,-1):
            cross = int(matrix[row_index][column_index]) * int(matrix[row_index + 1][column_index - 1]) * int(matrix[row_index + 2][column_index - 2]) * int(matrix[row_index + 3][column_index - 3])
            cross_product.append(cross)
print(max(cross_product))
