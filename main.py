# Render table
def showTable(table, start=None):
    if start != None:
        print(start)

    for y in range(len(table)):
        for x in range(len(table[0])):
            print(f"{table[y][x]}", end=' ')
        print()
    print("\n", end='')

# Input table (you can also change this table)
input_table = [[2, 4, 1],
               [3, 8, 5],
               [6, 9, 7]]

# Multiplication table (you can change this table)
multiplication_table = [[4],
                        [2],
                        [5]]

# Output table. We write in this array all results with input_table and multiplication table
output_table = [ [],
                 [],
                 [] ]

for y in range(3):
    for x in range(3):
        output_table[y].append(input_table[y][x] * multiplication_table[x][0])

showTable(input_table, "Input table: ")
showTable(multiplication_table, "Multiplication table: ")
showTable(output_table, "Output table: ")