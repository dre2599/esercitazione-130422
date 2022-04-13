from Persona import Persona

class Lavoratore(Persona):
    
    def __init__(self,nome,cognome,eta,lavoro):
        super().__init__(nome,cognome,eta)
        self.lavoro = lavoro

    def __str__(self):
     return super().__str__() + f' mestiere: {self.lavoro}'    