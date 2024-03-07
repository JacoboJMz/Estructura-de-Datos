# Ejerrcicio 1
def sumar_arreglo(arreglo):
    suma = 0
    for numero in arreglo:
        suma += numero
    return suma


numeros = [11, 2, 3, 6, 5, 7]
resultado = sumar_arreglo(numeros)
print(resultado)


# Ejercico 2
def ordenamiento_burbuja(arreglo):
    n = len(arreglo)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arreglo[j] > arreglo[j + 1]:
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]


numeros = [64, 34, 27, 12, 22, 86, 90]
ordenamiento_burbuja(numeros)
print(numeros)


# Ejercicio 3
def encontrar_maximo(arreglo):
    maximo = arreglo[0]
    for numero in arreglo:
        if numero > maximo:
            maximo = numero
    return maximo


numeros = [39, 7, 22, 10, 5]
maximo = encontrar_maximo(numeros)
print(maximo)


# Ejercicio 4
def fibonacci(n):
    if n <= 0:
        return "El término de la secuencia de Fibonacci debe ser un entero positivo."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b


resultado = fibonacci(9)
print(resultado)


# Ejercicio 5
def ordenamiento_seleccion(arreglo):
    n = len(arreglo)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arreglo[j] < arreglo[min_idx]:
                min_idx = j
        if min_idx != i:
            arreglo[i], arreglo[min_idx] = arreglo[min_idx], arreglo[i]


numeros = [74, 25, 32, 22, 11]
ordenamiento_seleccion(numeros)
print(numeros)


# Ejercicio 6
def buscar_numero(arreglo, objetivo):
    return objetivo in arreglo


numeros = [1, 2, 3, 4, 5]
resultado = buscar_numero(numeros, 7)
print(resultado)

# Ejercicio 7
Lista = set([57, 12, 2, 1, 2, 24, 12, 57])
print(Lista)


# Ejercicio 8
def multiplicar_matrices(matriz1, matriz2):
    filas_matriz1 = len(matriz1)
    columnas_matriz1 = len(matriz1[0])
    filas_matriz2 = len(matriz2)
    columnas_matriz2 = len(matriz2[0])

    if columnas_matriz1 != filas_matriz2:
        return None  # Las dimensiones no son adecuadas para la multiplicación

    resultado = [[0 for _ in range(columnas_matriz2)] for _ in range(filas_matriz1)]

    for i in range(filas_matriz1):
        for j in range(columnas_matriz2):
            for k in range(filas_matriz2):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado


matriz1 = [[1, 2, 3], [4, 5, 6]]
matriz2 = [[7, 8], [9, 10], [11, 12]]
resultado = multiplicar_matrices(matriz1, matriz2)
print(resultado)


# Ejercicio  9
class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def obtener_nombre(self):
        return self.nombre

    def obtener_edad(self):
        return self.edad

    def obtener_genero(self):
        return self.genero

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def establecer_edad(self, edad):
        self.edad = edad

    def establecer_genero(self, genero):
        self.genero = genero


persona1 = Persona("Juan", 25, "Masculino")
print(persona1.obtener_nombre())
print(persona1.obtener_edad())
print(persona1.obtener_genero())

persona1.establecer_edad(30)
print(persona1.obtener_edad())


# Ejercicio 10
class Rectangulo:
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

    def calcular_area(self):
        return self.longitud * self.ancho

    def calcular_perimetro(self):
        return 2 * (self.longitud + self.ancho)


mi_rectangulo = Rectangulo(5, 3)
print(mi_rectangulo.calcular_area())
print(mi_rectangulo.calcular_perimetro())

