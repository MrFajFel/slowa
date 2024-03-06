def slowa():
    plik = open("slowa.txt", "r")
    linijki = plik.readlines()

    ilosc = 0
    liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    ilosc = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for l in linijki:
        if len(l) < 14:
            ilosc[len(l)-2] += 1

    for i in range(len(liczby)):
        print(f"Wystąpienia liczby {liczby[i]}: {ilosc[i]}")


def nowe():
    plik = open("slowa.txt", "r")
    linijki = plik.readlines()

    plik2 = open("nowe.txt", "r")
    linijki_nowe = plik2.readlines()

    for i in linijki_nowe:
        wystapienia = 0
        wystapienia_lustrzane = 0

        for j in linijki:
            if i == j:
                wystapienia+=1

            if i.strip() == j[::-1].strip() and i != j:
                wystapienia_lustrzane+=1

        print(f"{i.strip()} {wystapienia} {wystapienia_lustrzane}")


nowe()

