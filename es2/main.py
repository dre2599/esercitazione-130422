

def getPromossi():
    file = input('inserisci nome del file: ')
    dict= {}
    if file == 'test.txt':
        with open(file, "r") as f:
            lista_nomi = []
            lista_voto1 = []
            lista_voto2 = []
            lista_medie = []
            dict_promossi = {}

            ris = f.readlines()
            for i in range(0, len(ris), 3):
                lista_nomi.append(ris[i].replace('\n',''))

            for i in range(1, len(ris), 3):
                lista_voto1.append(ris[i].replace('\n',''))

            for i in range(2, len(ris), 3):
                lista_voto2.append(ris[i].replace('\n',''))

            for i in range(len(lista_voto1)):
                lista_medie.append((int(lista_voto1[i])+int(lista_voto2[i]))/2)
            
            dict = dict(zip(lista_nomi, lista_medie))

            for k in dict:
                if dict[k] >= 18:
                    dict_promossi[k] = dict[k]
            
            return dict_promossi
    else:
        return 'inserisci un file valido'
            
getPromossi()
# print(dict)
# print(lista_voto1)
# print(lista_voto2)
# print(lista_medie)



