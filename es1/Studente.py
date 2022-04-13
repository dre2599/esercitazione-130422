from Persona import Persona

class Studente(Persona):
    
    def addCorso(self, corso):
        self.corso = corso
        return self.corso
    
    def __str__(self):    
        return str(self.nome) +' '+ str(self.cognome) + ' ha '+ str(self.eta) + ' anni e frequenta'

instance = Studente('mario','ciao',22).addCorso('mate')
print (instance)
