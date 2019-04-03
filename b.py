def Matrice_Rara(matrice, nr_linii, nr_coloane):
    i = 0
    numar_elemente_nenule = 0
    numar_elemente_nule = 0
    while int(i) < int(nr_linii):
        j = 0
        while int(j) < int(nr_coloane):
            if matrice[i][j] != 0:
                numar_elemente_nenule += 1
            else:
                numar_elemente_nule += 1
            j += 1
        i += 1
    if numar_elemente_nenule > numar_elemente_nule:
        return 1
    else:
        return 0


def Creare_Matrice(matrice, nr_linii, nr_coloane) :
    ok = 1
    print("Introduceti un element dupa indicii i,j(pentru pozitia in matrice) si valoare nenula v :")
    while int(ok) == 1:
        i = input("i =")
        j = input("j =")
        v = input("v =")
        matrice[int(i)][int(j)] = v
        if Matrice_Rara(matrice,nr_linii,nr_coloane) == 0 :
            print("Adaugati element: ")
        else :
            print("Matricea este rara acum. Doriti sa mai adaugati elemente?1/0")
            ok = input()


def Afisare_Matrice(matrice, nr_linii, nr_coloane) :
    i = 0
    while int(i) < int(nr_linii) :
        print(matrice[i][0 :])
        i += 1


def Suma_Doua_Matrici(matrice_1, nr_linii_matrice_1, nr_coloane_matrice_1, matrice_2, nr_linii_matrice_2, nr_coloane_matrice_2) :
    if int(nr_linii_matrice_1) != int(nr_linii_matrice_2) :
        print("Nu se poate realiza suma celor 2 matrici")
        return 0
    elif int(nr_coloane_matrice_1) != int(nr_coloane_matrice_2) :
        print("Nu se poate realiza suma celor 2 matrici")
        return 0
    else :
        matrice_suma = [[0 for x in range(int(nr_linii_matrice_1))]for y in range(int(nr_coloane_matrice_1))]
        i = 0
        while int(i) < int(nr_linii_matrice_1) :
            j = 0
            while int(j) < int(nr_coloane_matrice_1) :
                matrice_suma[i][j] = int(matrice_1[i][j]) + int(matrice_2[i][j])
                j += 1
            i += 1
    Afisare_Matrice(matrice_suma,nr_linii_matrice_1,nr_coloane_matrice_1)


def Scadere_Doua_Matrici(matrice_1, nr_linii_matrice_1, nr_coloane_matrice_1, matrice_2, nr_linii_matrice_2, nr_coloane_matrice_2) :
    if int(nr_linii_matrice_1) != int(nr_linii_matrice_2) :
        print("Nu se poate realiza diferenta celor 2 matrici")
        return 0
    elif int(nr_coloane_matrice_1) != int(nr_coloane_matrice_2) :
        print("Nu se poate realiza diferenta celor 2 matrici")
        return 0
    else :
        matrice_scadere = [[0 for x in range(int(nr_linii_matrice_1))]for y in range(int(nr_coloane_matrice_1))]
        i = 0
        while int(i) < int(nr_linii_matrice_1) :
            j = 0
            while int(j) < int(nr_coloane_matrice_1) :
                matrice_scadere[i][j] = int(matrice_1[i][j]) - int(matrice_2[i][j])
                j += 1
            i += 1
    Afisare_Matrice(matrice_scadere,nr_linii_matrice_1,nr_coloane_matrice_1)


def Inmultire_Doua_Matrici(matrice_1, nr_linii_matrice_1, nr_coloane_matrice_1, matrice_2, nr_linii_matrice_2, nr_coloane_matrice_2) :
    if int(nr_coloane_matrice_1) != int(nr_linii_matrice_2) :
        print("Nu se poate realiza inmultirea celor doua matrice")
        return 0
    else :
        matrice_inmultire = [[0 for x in range(int(nr_coloane_matrice_1))] for y in range(int(nr_linii_matrice_2))]
        i = 0
        while int(i) < int(nr_linii_matrice_1) :
            j = 0
            while int(j) < int(nr_coloane_matrice_1) :
                k = 0
                while int(k) < int(nr_coloane_matrice_2) :
                    matrice_inmultire[i][j] = int(matrice_inmultire[i][j]) + int(matrice_1[i][k]) * int(matrice_2[k][j])
                    k += 1
                j += 1
            i += 1
    Afisare_Matrice(matrice_inmultire, nr_linii_matrice_1, nr_coloane_matrice_2)


def Matrice_Transpusa(matrice, nr_linii, nr_coloane) :
    matrice_transpusa = [[0 for i in range(int(nr_linii))]for j in range(int(nr_coloane))]
    i = 0
    while int(i) < int(nr_linii) :
        j = 0
        while int(j) < int(nr_coloane) :
            matrice_transpusa[j][i] = int(matrice[i][j])
            j += 1
        i += 1
    Afisare_Matrice(matrice_transpusa, nr_linii, nr_coloane)


def Creare_Matrice_Nula() :
    nr_linii_matrice = input("nr_linii_matrice = ")
    nr_coloane_matrice = input("nr_coloane_matrice = ")
    matrice = [[0 for i in range(int(nr_coloane_matrice))] for j in range(int(nr_linii_matrice))]
    Afisare_Matrice(matrice, nr_linii_matrice, nr_coloane_matrice)

def Creare_Matrice_Unitate() :
    nr_linii_matrice = input("nr_linii_matrice = ")
    nr_coloane_matrice = input("nr_coloane_matrice = ")
    matrice = [[0 for i in range(int(nr_coloane_matrice))] for j in range(int(nr_linii_matrice))]
    i = 0
    while int(i) < int(nr_linii_matrice) and int(i) < int(nr_coloane_matrice) :
        matrice[i][i] = 1
        i += 1
    Afisare_Matrice(matrice, nr_linii_matrice, nr_coloane_matrice)


def DimensiuneMatrice(matrice, nr_linii, nr_coloane) :
    numarElemente = 0
    i = 0
    while int(i) < int(nr_linii) :
        j = 0
        while int(j) < int(nr_coloane) :
            if matrice[i][j] != 0 :
                numarElemente += 1
            j += 1
        i += 1
    print(numarElemente)




