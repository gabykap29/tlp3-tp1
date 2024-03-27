# Ejercicio 2: “Missing Number”
# Se te dan todos los números entre 1 a “n” excepto uno. Tu tarea es encontrar el número que
# falta.

# Input:
# El primer parámetro contiene la cantidad de elementos del array.
# El segundo parámetro contiene “n” números. Cada número es único y está entre 1 y n
# (inclusive).
# Output:
# Retornar el número que falta.

def missing_number(len,array):
    array_len = len
    accum = array[0]
    array_c = [accum]
    number = 0
    for i in range(0,array_len-1):
        accum += 1
        array_c.append(accum)
    print(array_c)
    for j in array_c:
        if j not in array:
            number = j
    print(f"el numero faltante es {number}")  
    return number
    


assert missing_number(5, [1, 2, 4, 5]) == 3, "Error en el caso deprueba"

# missing_number([1,2,4,5,6])