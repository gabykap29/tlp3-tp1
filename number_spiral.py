# Ejercicio 3: “Number Spiral”
# Un espiral numérico es una cuadrícula infinita cuyo cuadrado superior izquierdo tiene el
# número 1. Aquí están las primeras cinco capas del espiral.

# Tu tarea es descubrir el número en la fila x y la columna y.
# Input:
# El primer parámetro contiene la posición de la fila de la matriz espiral
# El segundo parámetro contiene la posición de la columna de la matriz espiral
# Output:
# Retornar el valor de la matriz en la posición seleccionada.

def number_spiral(colum, row):
    if colum > row:
        ans = (colum - 1) * (colum - 1)
        if colum % 2 != 0:
            add = row
        else:
            add = 2 * colum - row
        print(ans + add)
        return ans + add
    else:
        ans = (row - 1) * (row - 1)
        if row % 2 == 0:
            add = colum
        else:
            add = 2 * row - colum
        print(ans + add)
        return ans + add

colum = 3
row = 3
number_spiral(colum, row)

assert number_spiral(2, 2) == 3, "Error en el caso de prueba"