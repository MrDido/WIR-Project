import wikipediaapi
wiki = wikipediaapi.Wikipedia('en')
main = input("Insert title of Wikipedia Main Page: ")
mainpage = wiki.page(main)
pAllLinks_main = []

similar = input("Insert title of Wikipedia Related Page: ")
relatedpage = wiki.page(similar)
pAllLinks_similar = []

bad_words = ['user:', 'talk:', 'wikipedia:', 'template:', 'category:', 'file:', 'files:', 'portal:', 'draft:']


def find_links(page, listAll):
    links = page.links
    for title in sorted(links.keys()):
        listAll.append(title)

def checkBad_Words(res, toCheck, bad_words):
    bool = True
    toCheck_lowered = toCheck.lower()
    for word in bad_words:
        if word in toCheck_lowered:
            bool = False
            break

    if bool:
        res.append(toCheck)

def remove_bad_links(result, links):
    for link in links:
        checkBad_Words(result, link, bad_words)



res_main = []
find_links(mainpage, pAllLinks_main)
#print(pAllLinks_main)
remove_bad_links(res_main, pAllLinks_main)
print(res_main)
print("\n\n")

res_similar= []
find_links(relatedpage, pAllLinks_similar)
#print(pAllLinks_similar)
remove_bad_links(res_similar, pAllLinks_similar)
print(res_similar)
print("\n")
print("DIFFERENCE = ")
print(list(set(pAllLinks_similar) - set(pAllLinks_main)))