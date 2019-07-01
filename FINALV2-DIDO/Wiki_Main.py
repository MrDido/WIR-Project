import wikipediaapi
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

bad_words = ['user:', 'talk:', 'wikipedia:', 'template:', 'category:', 'file:', 'files:', 'portal:', 'draft:']
wiki=wikipediaapi.Wikipedia('en')

origin = input("Insert title of Wikipedia Page: ")
t = wiki.page(origin)
d = t.backlinks
stop_words = set(stopwords.words('english'))
stop_words = stop_words.union(set(stopwords.words('italian')))

def unique_list(l):
    ulist = []
    for x in l:
        x = x.lower()
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
    bad_chars = ["#", "@", "(", ")", "!", "&", "[", "]", "%", "£", "+", "÷", ":", "/", ",", ".", "*", "?", "|", "!",
                 "$", "^", "<", ">", "=", "{", "}", "~", ";", "_", "\\", "\"", "-", "\'", "–", "×", "¿", "’"]
    #questo è da implementare se nella radice ci sono caratteri strani
    origin1 = origin
    for char in origin1:
        if char in bad_chars:
            origin1 = origin1.replace(char, "_")

    if not os.path.exists(origin):
        os.mkdir(origin)

    if not os.path.exists(origin +'/'+'Full_Repr_'+ origin):
        #os.mkdir('Full_Repr_' + origin)
        os.mkdir(origin + '/' + 'Full_Repr_' + origin)


    '''questo toglie i bad chars dal titolo'''
    for char in title:
        if char in bad_chars:
            title = title.replace(char, "_")
            
    with open(os.path.join(origin + '/' + 'Full_Repr_' + origin, title + ".txt"), "w+", encoding="utf-8") as f:
        res_origin = []
        #scansione backlinks della pagina principale
        for i in links.keys():
            res = []
            t1 = wiki.page(i)
            links1 = t1.backlinks

            checkBad_Words(res, i, bad_words)

            for char in i:
                if char in bad_chars:
                    i = i.replace(char, "_")

            #print(res)
            if res != []:
                res = i
                res_origin.append(i)
                print("Processed " + i)
            i_title = ''.join(res)
                #scansione backlinks dei backlinks
            with open(os.path.join(origin + '/' + 'Full_Repr_' + title, i_title + ".txt"), "w+", encoding="utf-8" ) as f1:
                res1=[]
                for j in links1.keys():

                    checkBad_Words(res1, j, bad_words)
                    '''
                    la lista res1 contiene oggetti tipo ["telefono"], ["telefono di matteo"]. Per evitare che i due token siano trattati come parole diverse
                    attraverso queste 3 funzioni ottengo una lista pulita in cui ogni parola è un token, cioè ["telefono"], ["telefono"], ["di"], ["matteo"]
                    '''
                res1_clean_string = ' '.join(res1)
                # unwanted chars
                res1_clean_string = ''.join(i for i in res1_clean_string if not i in bad_chars).strip()
                word_tokens = word_tokenize(res1_clean_string)
                filtered_sentence = [w for w in word_tokens if not w in stop_words]
                #res1_clean_list = filtered_sentence.split()
                '''
                invoco la funzione definita sopra
                '''
                unique_res1 = unique_list(filtered_sentence)
                    
                for j in unique_res1:
                    f1.write(j + " ")

        res_clean_string = ' '.join(res_origin)

        res_clean_string = ''.join(i for i in res_clean_string if not i in bad_chars).strip()
        word_tokens = word_tokenize(res_clean_string)
        filtered_sentence = [w for w in word_tokens if not w in stop_words]

        unique_res = unique_list(filtered_sentence)
        #scrivo nel file origine
        for j in unique_res:
            f.write(j + " ")


create_and_write(origin, d)


