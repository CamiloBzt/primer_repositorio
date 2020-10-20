def main() -> None:
    
    print("Please enter the names or nicknames separated by comma.")
    nicknames = input()
    print("Please enter the keywords.")
    keyw = input()
    nicknames_low = nicknames.lower()
    keyw = keyw.lower()
    names = nicknames.split(",")
    nicknames_low = nicknames_low.split(",")
    keyw = keyw.split(",")
    cont = 0
    for i in range(0, len(names)):
        name_valid = True
        for key in keyw:
            if key in nicknames_low[i]:
                name_valid = False
        if name_valid:
            print(names[i], 'receive a cordial greeting from the lord of thunder, know that he awaits your '
                            'presence tonight for a game.')
            cont += 1
    if cont == 0:
        print("Sorry lord of thunder, there is no one to invite.")

main()
