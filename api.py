from fastapi import FastAPI, Request
from datetime import datetime

storage=FastAPI(title='MY FASTAPI')


# Flask way
@storage.get('/')
def index():
    return"My name is Bezalel, This is my first API"


if __name__== '__main__':
    storage.run()

@storage.get('/today')  # route with get method
def today():
    return str(datetime.now())

@storage.get('/mynames')
#def names(request:Request):
def names(First_name:bool=False, last_name:bool=False, full_name_:bool=False):
    full_names=""
    if First_name:
        full_names += "MUKIRANUTSI"
    if last_name:
        full_names += ' Bezalel'
    if full_name_:
       full_names += "My names is MUKIRANUTSI BEZALEL"
    return full_names
if __name__=="__main__":
    storage.run()
    