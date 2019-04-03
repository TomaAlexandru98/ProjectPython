import b

print("Introduceti dimensiunile pentru Matrice_1 :")
nr_linii_matrice_1 = input("nr_linii_matrice_1 = ")
nr_coloane_matrice_1 = input("nr_coloane_matrice_1 = ")
matrice_1 = [[0 for i in range(int(nr_coloane_matrice_1))] for j in range(int(nr_linii_matrice_1))]
b.Creare_Matrice(matrice_1, nr_linii_matrice_1, nr_coloane_matrice_1)
print("Matricea_1 a fost creata!")
print("Matricea_1 este: ")
b.Afisare_Matrice(matrice_1, nr_linii_matrice_1, nr_coloane_matrice_1)

print("Introduceti dimensiunile pentru Matrice_2: ")
nr_linii_matrice_2 = input("nr_linii_matrice_2 =")
nr_coloane_matrice_2 = input("nr_coloane_matrice_2 =")
matrice_2 = [[0 for i in range(int(nr_coloane_matrice_2))] for j in range(int(nr_linii_matrice_2))]
b.Creare_Matrice(matrice_2, nr_linii_matrice_2, nr_coloane_matrice_2)
print("Matrice_2 a fost creata! ")
print("Matricea_2 este: ")
b.Afisare_Matrice(matrice_2, nr_linii_matrice_2, nr_coloane_matrice_2)

k = 1
while int(k) > 0 and int(k) < 9 :
     print("1.Determinarea dimensiunii matricei :")
     print("2.Citirea/Scriea unei valori :")
     print("3.Adunare doua matrici :")
     print("4.Scadere doua matrici :")
     print("5.Inmultire doua matrici :")
     print("6.Creare matrice nula :")
     print("7.Creare matrice unitate :")
     print("8.Transpunere matrice :")
     print("0.Inchidere program")
     print("Optiunea dumneavoastra :")
     k = input()
     if int(k) == 1 :
         print("Matricea_1 :")
         b.DimensiuneMatrice(matrice_1,nr_linii_matrice_1,nr_coloane_matrice_1)
         print("Matrice_2 :")
         b.DimensiuneMatrice(matrice_2,nr_linii_matrice_2,nr_coloane_matrice_2)
     elif int(k) == 2 :
         print("Doriti sa cititi/scrieti o valoare? 0/1")
         k1 = input()
         if int(k1) == 0 :
             i = input("i = ")
             j = input("j = ")
             print(matrice_1[int(i)][int(j)])
         if int(k1) == 1 :
             i = input("i = ")
             j = input("j = ")
             print("Introduceti noua valoare :")
             v = input()
             matrice_1[int(i)][int(j)] = v
             b.Afisare_Matrice(matrice_1,nr_linii_matrice_1,nr_coloane_matrice_1)
     elif int(k) == 3 :
         print("Suma matricelor Matrice_1 si Matrice_2 este :")
         b.Suma_Doua_Matrici(matrice_1, nr_linii_matrice_1, nr_coloane_matrice_1, matrice_2, nr_linii_matrice_2,nr_coloane_matrice_2)
     elif int(k) == 4 :
         print("Diferenta matricelor Matrice_1 si Matrice_2 este :")
         b.Scadere_Doua_Matrici(matrice_1, nr_linii_matrice_1, nr_coloane_matrice_1, matrice_2, nr_linii_matrice_2,nr_coloane_matrice_2)
     elif int(k) == 5 :
         print("Inmultirea matricelor Matrice_1 si Matrice_2 este :")
         b.Inmultire_Doua_Matrici(matrice_1, nr_linii_matrice_1, nr_coloane_matrice_1, matrice_2, nr_linii_matrice_2,nr_coloane_matrice_2)
     elif int(k) == 6 :
         b.Creare_Matrice_Nula()
     elif int(k) == 7 :
         b.Creare_Matrice_Unitate()
     elif int(k) == 8 :
         b.Afisare_Matrice(matrice_1,nr_linii_matrice_1,nr_coloane_matrice_1)
         b.Matrice_Transpusa(matrice_1,nr_linii_matrice_1,nr_coloane_matrice_1)
     elif int(k) == 0 :
         k = 9

