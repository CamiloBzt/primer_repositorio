def contador_divisores(numero:int) -> int:
    """
    Funcion que cuenta el numero de divisores de un numero.
    :param numero:numero entero.
    :return:retorna la cantidad de divisores que tiene un numero entero.
    """
    cont = 0
    for i in range(1, numero+1):
        if numero % i == 0:
            cont += 1
    return cont

def main() -> None:
    print("Bienvenido".center(20, "-"))
    print("Digite un numero: ")
    num_1 = int(input())
    if contador_divisores(num_1) == 2:
        print("PRIMO!")
    else:
        print("NO PRIMO!")
main()