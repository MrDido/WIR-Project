import wikipediaapi
import os
wiki=wikipediaapi.Wikipedia('en')

origin = input("Insert title of Wikipedia Page: ")
t = wiki.page(origin)
d = t.backlinks

'''
questa funzione prende in input una lista e restituisce una nuova lista, ordinata in ordine alfabetico, in cui non ci sono duplicati e in cui tutte le
lettere sono minuscole (questo per evitare che consideri "ciao" e "Ciao" come due parole diverse

la funzione rimuove inoltre l'evntuale virgola a fine parola " ciao, " diventa " ciao " (questo sempre per evitare che le consideri due parole diverse
'''
def unique_list(l):
    ulist = []  
    for x in l:
        x = x.lower()
        if x not in ulist:
            ulist.append(x.rstrip(','))
    ulist.sort()
    return ulist


def checkBad_Words(res, toCheck, bad_words):
    bool = True
    toCheck = toCheck.lower()
    for word in bad_words:
        if word in toCheck:
            bool = False
            break

    if bool:
        res.append(toCheck)



def create_and_write(title, links):
    bad_words = ['user:', 'talk:', 'wikipedia:', 'template:', 'category:', 'file:', 'files:', 'portal:', 'draft:']
    if not os.path.exists('files_'+ origin):
        os.mkdir('files_' + origin)

    if ('/' or ',') in title:
        title = title.replace('/', '_')
    with open(os.path.join('files_' + origin, title + ".txt"), "w+", encoding="utf-8") as f:
        res_origin = []
        #scansione backlinks della pagina principale
        for i in links.keys():
            res = []

            if ('/' or ',') in i:
                i = i.replace('/', '_')
                
            '''if ("user" not in i.lower()) and ("talk:" not in i.lower()) and ("wikipedia" not in i.lower()) and ("template" not in i.lower()) and ("category" not in i.lower()) and ("file" not in i.lower()) and ("portal" not in i.lower()):
                res.append(i)'''

            checkBad_Words(res, i, bad_words)
            #print(res)
            if res != []:
                res = i
                res_origin.append(i)
                print("Processed " + i)
            i_title = ''.join(res)
                #scansione backlinks dei backlinks
            with open(os.path.join('files_' + title, i_title + ".txt"), "w+", encoding="utf-8" ) as f1:
                t1  = wiki.page(i)
                links1 = t1.backlinks
                res1=[]
                for j in links1.keys():

                    if ('/' or ',') in i:
                        j = j.replace('/', '_')
            
                            
                        '''if ("user" not in j.lower()) and ("talk:" not in j.lower()) and ("wikipedia" not in j.lower()) and ("template" not in j.lower()) and ("category" not in j.lower()) and ("file" not in j.lower()) and ("portal" not in j.lower()):
                            res1.append(j)'''
                    checkBad_Words(res1, j, bad_words)
                    '''
                    la lista res1 contiene oggetti tipo ["telefono"], ["telefono di matteo"]. Per evitare che i due token siano trattati come parole diverse
                    attraverso queste 3 funzioni ottengo una lista pulita in cui ogni parola è un token, cioè ["telefono"], ["telefono"], ["di"], ["matteo"]
                    '''
                res1_clean_string = ' '.join(res1)
                # unwanted chars
                bad_chars = ['#', '@', '(', ")", "!", "&", "[", "]", "%"]
                res1_clean_string = ''.join(i for i in res1_clean_string if not i in bad_chars).strip()
                res1_clean_list = res1_clean_string.split()
                '''
                invoco la funzione definita sopra
                '''
                unique_res1 = unique_list(res1_clean_list)
                    
                for j in unique_res1:
                    f1.write(j + " ")

        res_clean_string = ' '.join(res_origin)
        # unwanted chars
        bad_chars = ['#', '@', '(', ")", "!", "&", "[", "]", "%"]
        res_clean_string = ''.join(i for i in res_clean_string if not i in bad_chars).strip()
        res_clean_list = res_clean_string.split()
        unique_res = unique_list(res_clean_list)
        #scrivo nel file origine
        for j in unique_res:
            f.write(j + " ")


create_and_write(origin, d)


