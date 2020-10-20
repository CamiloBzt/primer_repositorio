def main() ->None:
    numeros = "123456789"
    numeros = list(numeros)
    for num in numeros:
        if int(num) % 2 == 1:
            print(num)

main()