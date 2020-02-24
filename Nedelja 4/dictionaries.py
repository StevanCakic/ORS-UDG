'''
    Napisati funkciju koja omogucava korisniku da unese
    n studenata (n parametar funkcije).
    Svaki student se predstavlja sa kao dictionary oblika:
    {ime, prezime, godina_studija, prosjek}.
    Funkcija treba da vrati listu studenata

    Napisati funkciju koja izdvaja one studenti ciji je prosjek veci od zadatog.
    Prosjek se zadaje kao parametar funkcije. Funkcija treba da vrati studente 
    koji zadovoljavaju zadati uslov

    Funkcije testirati
'''

def unos_studenata(broj_studenata):
    studenti = []
    for i in range(0, broj_studenata):
        ime = input("Unesite ime studenta:")
        prezime = input("Unesite prezime studenta:")
        godina_studija = int(input("Unesite godinu studija:"))
        prosjek = float(input("Unesite prosjek studenta:"))
        studenti.append({"ime": ime, "prezime": prezime, 
                        "godina_studija": godina_studija, "prosjek": prosjek})
    return studenti

def izdvoji_studente(studenti, min_prosjek):
    studenti_koji_zadovoljavaju_prosjek = []
    for student in studenti:
        print(student)
        if min_prosjek < student["prosjek"]:
            studenti_koji_zadovoljavaju_prosjek.append(student)
    return studenti_koji_zadovoljavaju_prosjek
        

broj_studenata = int(input("Unesite broj studenata:"))
studenti = unos_studenata(broj_studenata).copy()

min_prosjek = float(input("Unesite minimalni prosjek studenta:"))
studenti_sa_zadovoljavajucim_prosjekom = izdvoji_studente(studenti, min_prosjek)
print(studenti_sa_zadovoljavajucim_prosjekom)
