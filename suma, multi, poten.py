def suma(sumando_1: int, sumando_2: int) -> int:
    """
    Función que retorna la suma de dos numeros enteros.
    :param sumando_1: numero entero uno.
    :param sumando_2: numero entero dos.
    :return: suma de dos numeros enteros.
    """
    sum = sumando_1 + sumando_2
    return sum


def multiplicacion(factor_1: int, factor_2: int) -> int:
    """
    Función que retorna la multiplicacion de dos numeros enteros
    con ayuda de la función suma.
    :param factor_1: numero entero uno.
    :param factor_2: numero entero dos.
    :return: retorna el productor de los factores.
    """
    mult = 0
    for i in range(0, factor_2):
        mult = suma(mult, factor_1)
    return mult


def potencia(base: int, expon: int) -> int:
    """
    Función que retorna la potencia de dos numeros enteros
    usando la función multiplicación.
    :param base: base de una potencia.
    :param expon: exponente de una potencia.
    :return: retorna la potencia de dos numeros enteros.
    """
    pot = 1
    for i in range(0, expon):
        pot = multiplicacion(pot, base)
    return pot


def main() -> None:
    """
    Función principal.
    """
    print("Bienvenido".center(20, "-"))
    print("Por favor, digite un numero: ")
    num_1 = int(input())
    print("Por favor, digite otro numero: ")
    num_2 = int(input())
    print(suma(num_1, num_2))
    print(multiplicacion(num_1, num_2))
    print(potencia(num_1, num_2))

main()
