import sqlite3

conn = sqlite3.connect('immobili.db')
curs = conn.cursor()

try:
    curs.execute("DROP table immobile")
    curs.execute("DROP table catalogo")
except:
    pass

curs.execute("CREATE table immobile (riferimento char(30), proprietario char(30), indirizzo char(30), citta char(30), prezzo int, catalogo char(30))")


class Immobile():
    def __init__(self, riferimento, prezzo, proprietario, indirizzo, citta):
        self.riferimento = riferimento
        self.prezzo = prezzo
        self.proprietario = proprietario
        self.indirizzo = indirizzo
        self.citta = citta

    def modifica_prezzo(self, prezzo_nuovo):        
        self.prezzo = prezzo_nuovo
        print("\nPrezzo modificato")

    def stampa_immobile(self):
        print("citta: %s\nindirizzo: %s\nprezzo: %d\nproprietario: %s" %(self.citta, self.indirizzo, self.prezzo, self.proprietario))



class Catalogo():
    def __init__(self,nome, cursore):
        self.nome = nome
        self.immobili = []
        self.cursore = cursore
        
    def aggiungi(self, immobile):
        self.immobili.append(immobile)

        row = (immobile.riferimento, immobile.proprietario, immobile.indirizzo,
            immobile.citta, immobile.prezzo, self.nome)
        self.cursore.execute("insert into immobile values(?, ?, ?, ?, ?, ?)", row)
        print("immobile aggiunto")


    def elimina(self, immobile):
        if immobile in self.immobili:
            self.immobili.remove(immobile)
            self.cursore.execute("delete from immobile where riferimento = ?", (immobile.riferimento,))
            print("Immobile eliminato")
        else:
            print("Immobile non esistente")

    def cerca(self, proprietario):
        for immobile in self.immobili:
            if immobile.proprietario == proprietario:
                print("\nIl proprietario possiede i seguenti immobili:\n")
                immobile.stampa_immobile()
            else:
                print("Proprietario non trovato")
        print("dal database:")
        self.cursore.execute("SELECT * FROM immobile WHERE indirizzo = ?",(immobile.proprietario,))
        for row in self.cursore.fetchall():
            print(row)

    def stampa_cat(self):
            for immobile in self.immobili:
                immobile.stampa_immobile()
            print("dal database:")
            self.cursore.execute("SELECT * FROM immobile")
            for row in self.cursore.fetchall():
                print(row)

generale = Catalogo("generale", curs)

casa1 = Immobile("1a", 50000, "nicola losito", "via roma 2", "grosseto")
casa2 = Immobile("2a", 100000, "mario rossi", "via canada 5", "pisa")

generale.aggiungi(casa1)
generale.aggiungi(casa2)
generale.stampa_cat()
generale.cerca("nicola losito")

conn.commit()
conn.close()