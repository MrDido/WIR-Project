from whoosh.index import create_in
from whoosh.fields import *
import os
import sys
 
  
 
'''
Schema definition: title(name of file), path(as ID), content(indexed
but not stored),textdata (stored text content)
'''
schema = Schema(title=TEXT(stored=True),path=ID(stored=True), content=TEXT,textdata=TEXT(stored=True))


#create folder if doesn't exist
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")
 
# Creating a index writer to add document as per schema
ix = create_in("indexdir",schema)
writer = ix.writer()


#take the file and add line by line
path = 'source/output_Tea.txt'
titolo = "Tea_search"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for i in lines:
    writer.add_document(title=i, path=path, content=i,textdata=i)
    print(i)
writer.commit()
 


#query section
from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from whoosh import scoring

ix = open_dir("indexdir")

with ix.searcher(weighting=scoring.Frequency) as searcher:
     parser = QueryParser("content", ix.schema) #this is where to search
     myquery = parser.parse("english") #this is the word to search
     results = searcher.search(myquery)
     print(results)
     for i in results:
         print(i)

