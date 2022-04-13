from Studente import Studente
from Persona import Persona
from Lavoratore import Lavoratore

class Main:
    def test_persona(self):
            nome = input('Inserisci il nome della persona\n')
            cognome = input('Inserisci il cognome della persona\n')
            eta = int(input("inserisci l'età della persona\n"))
            persona = Persona(nome,cognome,eta)
            print(persona)
    
    def test_studente(self):
            nome = input('Inserisci il nome dello studente\n')
            cognome = input('Inserisci il cognome dello studente\n')
            eta = int(input("inserisci l'età dello studente\n"))
            corso = input('Inserisci il cognome della persona\n')
            studente = Studente(nome,cognome,eta,corso)
            print(studente)
    
    def test_lavoratore(self):
            nome = input('Inserisci il nome del lavoratore\n')
            cognome = input('Inserisci il cognome del lavoratore\n')
            eta = int(input("inserisci l'età del lavoratore\n"))
            lavoro = input('Inserisci il lavoro del lavoratore\n')
            lavoratore = Lavoratore(nome,cognome,eta, lavoro)
            print(lavoratore)

main = Main()
main.test_lavoratore()
main.test_persona()
main.test_studente()

