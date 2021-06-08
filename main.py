import pickle

class Immobile():
    def __init__(self, id, prezzo, proprietario, indirizzo, citta):
        self.id = id
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
    def __init__(self,nome):
        self.nome = nome
        self.immobili = []
        #aggiungo pickle
        self.file = self.nome + ".p"

    def aggiungi(self, immobile):
        self.immobili.append(immobile)
        print("Immobile aggiunto")

    def elimina(self, immobile):
        if immobile in self.immobili:
            self.immobili.remove(immobile)
            print("Immobile eliminato")
        else:
            print("Immobile non esistente")

    def stampa_cat(self):
        for immobile in self.immobili:
            immobile.stampa_immobile()

    def cerca(self, proprietario):
        for immobile in self.immobili:
            if immobile.proprietario == proprietario:
                print("Il proprietario possiede i seguenti immobili:\n")
                immobile.stampa_immobile()
            else:
                print("Proprietario non trovato")

###############  creo funzioni Pickle   ################

    def salva(self):     ### aggiunge i valori al file sopra creato
        with open(self.file, "wb") as file:
            pickle.dump(self.immobili, file)
        print("Salvataggio effettuato")

    def leggi(self):     ### legge i valori del file sopra creato
        with open(self.file, "rb") as file:
            self.immobili = pickle.load(file)
        



casa1 = Immobile(1, 500, "nicola", "via roma", "grosseto")
casa2 = Immobile(2, 1000, "nicola", "via canada", "pisa")

casa1.stampa_immobile()

casa1.modifica_prezzo(600)

casa1.stampa_immobile()

catalogo1 = Catalogo("vacanza")

catalogo1.aggiungi(casa1)
catalogo1.aggiungi(casa2)
catalogo1.stampa_cat()
#catalogo1.elimina(casa1)

catalogo1.cerca("nicola")

catalogo1.salva()    ### eseguo il codice e con Salva aggiungo a file 

### eseguo solo funzione Leggi per leggere il file sopra riempito

'''
print("\nqqqq")
catalogo1.leggi()
catalogo1.stampa_cat()
'''
