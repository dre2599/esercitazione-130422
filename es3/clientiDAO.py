from Singleton_DB import DBConnection

class clientiDAO(object):
    __db = None

    def __init__(self):
        self.__db = DBConnection()

    def getnumClientiForAgente(self):
        num = self.__db.query(f'select c.agente, count(c.nome) from clienti c group by c.agente').fetchall()
        for n in range (len(num)):
            print (f"per l'agente numero {num[n][0]} vi sono {num[n][1]} clienti" )
    
    def getClienti_byAgente(self):
        agente = int(input('inserisci numero agente: '))
        nomi = self.__db.query(f'select c.nome from clienti c where c.agente = {agente}').fetchall()
        print(f"i clienti dell'agente {agente} sono:\n")
        for nome in range (len(nomi)):
            print (f'{nomi[nome][0]}\n', end='')

    