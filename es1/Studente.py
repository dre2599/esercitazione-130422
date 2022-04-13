from Persona import Persona

class Studente(Persona):
    def __init__(self,nome,cognome,eta,corso):
        super().__init__(nome,cognome,eta)
        self.corso=corso   

    def __str__(self):
        return super().__str__()+f' corso dello studente:{self.corso}'
