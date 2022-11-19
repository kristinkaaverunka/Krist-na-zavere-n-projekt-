"""Main stranka je prepojena s ostatnymi zlozkami suboru. Volaju sa tu vsetky funkcie programu. """
from poistenec import Pojistenec
from uvod_texty import Texty
evidencia = []
t = Texty
t.vypis_hl_ponuky()

"""cyklus spusta vyber moznosti z programu a provadi v nom vyberane operace"""
cyklus = True
while cyklus == True:
    vyber_moznosti = t.vyber_moznosti()
    if vyber_moznosti == "1":
        jmeno = (input(str("Jmeno: ")))
        prijmeni = (input(str("Prijmeni: ")))
        vek = (input(str("Vek: ")))
        tel_cislo = (input(str("Tel: ")))
        p = Pojistenec(jmeno, prijmeni, vek, tel_cislo)
        evidencia.append(p)
        print("Nový pojistenec bol uložený. Údaje o pojistencovi: \n {0}".format(p))
    elif vyber_moznosti == "2":
        for i in evidencia:
            print(i)
    elif vyber_moznosti == "3":
        hladane_meno = input("Hladane jmeno: ")
        hladane_priezvisko = input("Hladane prijmeni: ")       
        for poistenec in evidencia:
            if poistenec.jmeno == hladane_meno and poistenec.prijmeni == hladane_priezvisko:
                print(poistenec) 
            else:
                print ("Osoba {0} {1} nie je v evidencii".format(hladane_meno, hladane_priezvisko))
    elif vyber_moznosti == "4": 
        print("Koniec programu")
        cyklus = False
    else:
        print("Volba nerozoznána.")
        cyklus = True
