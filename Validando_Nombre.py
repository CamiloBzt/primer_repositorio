def main() -> None:
    print("Bienvenido".center(20, "-"))
    print("Ingrese el nombre a evaluar")
    nombre = input()
    nombre = nombre.split(" ")
    valido = True
    if len(nombre)<2:
        valido = False
    if len(nombre)>6:
        valido = False
    for name in nombre:
        if len(name)<3:
            valido = False
        if not name[0].isupper():
            valido = False
        if not name.isalpha():
            valido = False
    if valido:
        print("VALIDO.")
    else:
        print("INVALIDO.")
main()