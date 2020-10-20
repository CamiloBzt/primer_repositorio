def suma_divisores(numero:int) -> int:
    """
    Función la cual suma los divisores de un numero entero positivo.
    :param numero: numero entero.
    :return: suma de los divisores del numero entero.
    """
    sum = 0
    for i in range(1, numero + 1//2):
        if numero % i == 0:
            sum += i
    return sum


def main() -> None:
    print("Digite el numero de numeros: ")
    num_1 = int(input())
    for i in range(num_1):
        print("Digite un numero: ")
        num_2 = int(input())
        if suma_divisores(num_2) >= num_2//2:
            print("Encontrado!")
        else:
            print("no es...")

main()