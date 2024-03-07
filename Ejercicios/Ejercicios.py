#1 ejercicio
mi_lista = []

while True:
    digito = input("ingerese un elemento o salir para terminar")
    if digito.lower() == "salir":
        break
    else:
        mi_lista.append(digito)
print(mi_lista)
#2 ejercicio
Lista = set([55, 12, 2, 1, 2, 26, 12, 55])
print(Lista)

#3 ejercicio
Digitos = [45, 2, 36]
suma_Lista = sum(Digitos)
print(suma_Lista)


#4 ejercicio
def elemento_comun(lista1, lista2):
    for elemento in lista1:
        if elemento in lista2:
            return True
    return False

lista1 = [1,2,3,4,5,6,7]
lista2 = [6,9,12,15,18]

print(elemento_comun(lista1, lista2))


#5 ejercicio
def multiplicacion_forma_circular(matriz):
    if not matriz:
        return 0

    m = len(matriz)
    n = len(matriz[0])
    multiplicacion = 1

    for i in range(m):
        for j in range(n):
            multiplicacion *= matriz[i % m][j % n]

    return multiplicacion

matriz_ejemplo = [
    [11, 12, 13],
    [14, 15, 16],
    [17, 18, 19]
]

resultado = multiplicacion_forma_circular(matriz_ejemplo)
print(resultado)
