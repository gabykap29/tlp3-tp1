# Ejercicio 1: “Weird Algorithm”
# Considera un algoritmo que toma como entrada un entero positivo n. Si n es par, el algoritmo
# lo divide por dos, y si n es impar, el algoritmo lo multiplica por tres y le suma uno. El
# algoritmo repite esto hasta que n sea uno. Por ejemplo, la secuencia para el valor 3 es la
# siguiente:
# 3 ➝ 10 ➝ 5 ➝ 16 ➝ 8 ➝ 4 ➝ 2 ➝ 1
# Tu tarea es simular la ejecución del algoritmo para un valor dado de n.


def weird_algorithm(n):
    array = [n]
    if n < 0:
        print("Numero ingresado es 0")
    else:
        while n != 1:
            if n % 2 == 0:
                n = n // 2
                array.append(n)
            elif n % 2 != 0:
                n = (n * 3) + 1
                array.append(n)
        return array


assert weird_algorithm(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"
print(weird_algorithm(3))