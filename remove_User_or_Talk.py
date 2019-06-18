import wikipediaapi
wiki=wikipediaapi.Wikipedia('en')

t = wiki.page("Pokemon Go")
d = t.backlinks

for i in d:
    print(i)
def removeUser(d):
    res=[]
    for i in d.keys():
        if ("user" not in i.lower()) and ("talk" not in i.lower()):
            res.append(i)
    return res

new=removeUser(d)
print()
print("/")
for i in new:
    print(i)
