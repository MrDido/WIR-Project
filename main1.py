import wikipediaapi
wiki=wikipediaapi.Wikipedia('en')

origin = input("Insert title of Wikipedia Page: ")
t = wiki.page(origin)
d = t.backlinks

def create_and_write(title, links):
    f = open(title+".txt", "w+")
    res = []
    for i in links.keys():
        if ("user" not in i.lower()) and ("talk" not in i.lower()) and ("wikipedia" not in i.lower()) and ("template" not in i.lower()) and ("category" not in i.lower()) and ("file" not in i.lower()) and ("portal" not in i.lower()):
            res.append(i)
            #if.write(i + "\n")
            if ("/" or ",") in i:
                i.replace("/", "_")

            f1 = open(i + ".txt", "w+")
            t1  = wiki.page(i)
            links1 = t1.backlinks
            res1=[]
            for j in links1.keys():
                if ("user" not in j.lower()) and ("talk" not in j.lower()) and ("wikipedia" not in j.lower()) and ("template" not in j.lower()) and ("category" not in j.lower()) and ("file" not in j.lower()) and ("portal" not in j.lower()):
                    res1.append(j)

            res1.sort()
            for j in res1:
                f1.write(j + "\n")

            f1.close()
        #print("Processed " + i)

    res.sort()
    for i in res:
        f.write(i + "\n")

    f.close()

create_and_write(origin, d)


