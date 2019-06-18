import wikipediaapi
wiki=wikipediaapi.Wikipedia('en')

t = wiki.page("Pokemon Go")
d = t.backlinks

def removeUser(d):
    res=[]
    for i in d.keys():
        if ("user" not in i.lower()) and ("talk" not in i.lower()):
            res.append(i)
    return res

new=removeUser(d)


f= open("output_after_remove.txt","w+")

for i in new:
    f.write(i +"\n")
    print(i)
f.close()
