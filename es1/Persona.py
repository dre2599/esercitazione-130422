class Persona():

    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def __str__(self):
        return str(self.nome) +' '+ str(self.cognome) + ' ha '+ str(self.eta) + ' anni '
