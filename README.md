# How this work?
First we create function:
``` python
# Render table
def showTable(table, start=None):
    if start != None:
        print(start)

    for y in range(len(table)):
        for x in range(len(table[0])):
            print(f"{table[y][x]}", end=' ')
        print()
    print("\n", end='')
```
We'll explain why we created the function <br>

Then we create a input array (but actually i call multidimensional array):
``` python
# Input table (you can also change this table)
input_table = [[2, 4, 1],
               [3, 8, 5],
               [6, 9, 7]]
```
And multiplication table:
``` python
# Multiplication table (you can change this table)
multiplication_table = [[4],
                        [2],
                        [5]]
```
And finally output table:
``` python
# Output table. We write in this array all results with input_table and multiplication table
output_table = [ [],
                 [],
                 [] ]
```
Now we take each number from the input table and multiply it by each number from the multiplication table and writting in output table. It all looks in code like this:
``` python
for y in range(3):
    for x in range(3):
        output_table[y].append(input_table[y][x] * multiplication_table[x][0])
```
In picture looks like this:
![icon](https://github.com/We4not/Multiplication-table/blob/main/prototype.png)

After we've done everything, all that remains is to display the information to the user like this:
``` python
showTable(input_table, "Input table: ")
showTable(multiplication_table, "Multiplication table: ")
showTable(output_table, "Output table: ")
```

And result is:
```
Input table: 
2 4 1 
3 8 5 
6 9 7 

Multiplication table: 
4 
2 
5

Output table:
8 8 5
12 16 25
24 18 35

```

Oh yes, about the `showTable()` function. How does it even work? Let's go back to the very beginning

## Function `showTable()`
What does the ***start=None*** variable do inside a function? Before displaying the table, we first write what is written inside the ***start*** variable, and then we display the table.
``` python
def showTable(table, start=None):
    if start != None:
        print(start)
```
If nothing is written to the ***start*** variable, then we skip this check <br>

How do we display the table on the screen? We go through x and y on the table which is specified in the ***table*** variable and print it to the screen.
``` python
for y in range(len(table)):
        for x in range(len(table[0])):
            print(f"{table[y][x]}", end=' ')
        print() # After completing the first cycle, we go to the next cycle y
    print("\n", end='') # End function
```