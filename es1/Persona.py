class Persona():

    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def __str__(self):
        return f'Nome: {str(self.nome)} Cognome: {str(self.cognome)} Età: {str(self.eta)} anni'
