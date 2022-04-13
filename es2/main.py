from doctest import OutputChecker


def get_key(val,diz):
    for key, value in diz.items():
         if val == value:
             return key
 
    return "key doesn't exist"


file = input('inserisci nome del file: ')
if file == 'test.txt':
    with open(file, "r") as f:
        lista_nomi = []
        lista_voto1 = []
        lista_voto2 = []
        lista_medie = []
        dict_promossi = {}
        dict_bocciati = {}

        ris = f.readlines()
        for i in range(0, len(ris), 3):
            lista_nomi.append(ris[i].replace('\n',''))
            lista_voto1.append(ris[i+1].replace('\n',''))
            lista_voto2.append(ris[i+2].replace('\n',''))

        for i in range(len(lista_voto1)):
            lista_medie.append((int(lista_voto1[i])+int(lista_voto2[i]))/2)
        
        diz = dict(zip(lista_nomi, lista_medie))

        for k in diz:
            if diz[k] >= 18:
                dict_promossi[k] = diz[k]
                nomecognome = get_key(diz[k],dict_promossi)
                print (f'Nominativo dipendente: {nomecognome} Media voti: {diz[k]} esame superato')
            else:
                dict_bocciati[k] = diz[k]
                nomecognome = get_key(diz[k],dict_bocciati)
                print (f'Nominativo dipendente: {nomecognome} Media voti: {diz[k]} esame non superato')
    
else:   
    print('inserisci un file valido') 


# output
# Nominativo dipendente: Paolo Rossi Media voti: 27.5 esame superato
# Nominativo dipendente: Giorgia Bianchi Media voti: 16.0 esame non superato
# Nominativo dipendente: Marco Neri Media voti: 26.0 esame superato
# Nominativo dipendente: Giorgia Bianchi Media voti: 16.0 esame non superato

