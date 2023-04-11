from flask import Flask
from flask import request
import requests
import json
import os.path

app = Flask(__name__)


class Film:
    def __init__(self, genre, imdbrating, released, synopsis, title, type):
        self.genre=genre #a list
        self.imageurl=["a link"] #a list
        self.imdbid='432kfh24' #TODO generate a random id
        self.imdbrating=imdbrating
        self.released=released
        self.synopsis=synopsis
        self.title=title
        self.type=type
    
    def toJson(self):
        return json.dumps(self,default=lambda o: o.__dict__)
    

if not os.path.isfile('./filme.json'):
    #data is fetched and the json file is created locally
    url='https://ott-details.p.rapidapi.com/advancedsearch?start_year=2015&end_year=2020'
    headers = {
        'X-RapidAPI-Key': "18158db10dmshfd301d948367abbp19c882jsn15f2b8d7fbc6",
        'X-RapidAPI-Host': "ott-details.p.rapidapi.com"
        }

    data=requests.get(url,headers=headers).json()
    lista_filme=[]
    for film in data['results']:
        lista_filme.append(film)
    
    with open('filme.json','w') as f:
        json.dump(lista_filme,f)

#not the smartest way to do this
lista_filme=[] 
with open('filme.json') as f:
    data=json.load(f)
    for i in data:
        lista_filme.append(i)

#--app routes--
@app.route('/')
def films():
    return "asta nu e toata aplicatia noastra, don t panic"

@app.route('/films', methods=["POST","GET","PUT","DELETE"]) 
def addFilm():
    if request.method=='GET':
        if len(request.get_data())!=0:
            i=0
            while i<len(lista_filme):
                if lista_filme[i]['imdbid']==request.get_json():
                    return lista_filme[i]
                i+=1
            return "the film with id {id} does not exist :(".format(id=request.get_json())
        return lista_filme
        
    elif request.method=='POST':
        newFilm=Film(request.get_json()["genre"],
                     request.get_json()["imdbrating"],
                     request.get_json()["released"],
                     request.get_json()["synopsis"],
                     request.get_json()["title"],
                     request.get_json()["type"])
        #encode into JSON format
        newFilmJSONData=json.dumps(newFilm.toJson(),indent=4)
        
        #decode
        newFilmJSON=json.loads(newFilmJSONData)
        newFilmJSON2=json.loads(newFilmJSON)
        lista_filme.append(newFilmJSON2)

        #update the json file
        with open('filme.json','w') as f:
            json.dump(lista_filme,f)
            
        return 'film added'
    
    elif request.method=="PUT":
        i=0
        while i<len(lista_filme):
            if lista_filme[i]['imdbid']==request.get_json()['imdbid']:
                lista_filme[i]=request.get_json()
                #update the json
                with open('filme.json','w') as f:
                    json.dump(lista_filme,f)
                return "film updated"
            i+=1 
        return "the film with id {id} does not exist :(".format(id=request.get_json()['imdbid'])

    elif request.method=='DELETE':
        for i in lista_filme:
            if request.get_json()==i['imdbid']:
                lista_filme.remove(i)  
                #update the json
                with open('filme.json','w') as f:
                    json.dump(lista_filme,f)
                return "film deleted"
        return "the film with id {id} does not exist :(".format(id=request.get_json())

         

