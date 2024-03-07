from models import Author, Quote
import json
from mongoengine.errors import NotUniqueError


el_dict= []
quotes = []
authors = []

if __name__=='__main__':
    with open('authors.json',encoding='utf-8') as fd:
        data = json.load(fd)
        for  el in data:
            try:
                author = Author(fullname=el_dict.get('fullname'),
                born_date=el_dict.get('born_date'),
                born_location=el_dict.get('born_location'),
                description=el_dict.get('description'))
                author.save()
            except NotUniqueError:
                print(f"Автор вже існує {el.get('fullname')}")


    with open('qoutes.json',encoding='utf-8') as fd:
        data = json.load(fd)
        for  el in data:
            author,*_ = Author.objects(fullname=el.get('author'))
            quote = Quote(quote=el.get('quote'),tags=el.get('tags'),author=el.get('author'))