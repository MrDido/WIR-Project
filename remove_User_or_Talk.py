import wikipediaapi
import io
wiki=wikipediaapi.Wikipedia('en')

t = wiki.page("Tea")
d = t.backlinks

def removeUser(d):
    res=[]
    for i in d.keys():
        if ("user" not in i.lower()) and ("talk" not in i.lower()):
            res.append(i)
    return res

new=removeUser(d)


with open("output_Tea.txt", "w", encoding="utf-8") as f:
    for i in new:
        f.write(i +"\n")
        print(i)

