# Ejercicio 4: “Palindrome Reorder”
# Dada una cadena de caracteres, tu tarea es reorganizar los caracteres de la cadena de manera
# que puedas formar un palíndromo. Si no es posible formar un palíndromo, debes indicarlo.
# Input:
# El único parámetro contiene una cadena de caracteres de longitud n ( 1 ≤ n ≤ 10^6 ). La
# cadena solo contiene letras minúsculas del alfabeto inglés.
# Output:
# Retorna una cadena que represente un palíndromo formado reorganizando los caracteres de la
# cadena de entrada. Si no es posible formar un palíndromo, retorna "NO SOLUTION".


def palindrome_reorder(value):
    # cuenta la cantidad de veces que aparece cada letra
    count = {}
    for i in value:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    # cuenta cuantas letras aparecen un número impar de veces
    odd_count = 0
    odd_char = ""
    for j in count:
        if count[j] % 2 == 1:
            odd_count += 1
            odd_char = j
    # Si hay más de una letra que aparece un número impar de veces, no se puede formar un palíndromo
    if odd_count > 1:
        return "NO SOLUTION"
    # contruye la mitad del palíndromo
    half = ""
    for k in count:
        half += k * (count[k] // 2)
    # si hay una letra que aparece un número impar de veces, la pone en el medio
    if odd_count == 1:
        return half + odd_char + half[::-1]
    else:
        return half + half[::-1]

assert palindrome_reorder("aabbc") == "abcba", "Error en el caso de prueba"
print(palindrome_reorder("aabbc"))