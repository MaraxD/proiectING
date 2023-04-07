from flask import Flask
from flask import request
import requests
import uuid
import json

app = Flask(__name__)

url='https://ott-details.p.rapidapi.com/advancedsearch?start_year=2015&end_year=2020'
headers = {
    'X-RapidAPI-Key': "18158db10dmshfd301d948367abbp19c882jsn15f2b8d7fbc6",
    'X-RapidAPI-Host': "ott-details.p.rapidapi.com"
    }

data=requests.get(url,headers=headers).json()

class Film:
    def __init__(self, genre, imdbrating, released, synopsis, title, type):
        self.genre=genre #a list
        self.imageurl=["a link"] #a list
        self.imdbid='432kfh24' #TODO generating a random id
        self.imdbrating=imdbrating
        self.released=released
        self.synopsis=synopsis
        self.title=title
        self.type=type
    
    def toJson(self):
        return json.dumps(self,default=lambda o: o.__dict__)


lista_filme=[]
for film in data['results']:
    lista_filme.append(film)

@app.route('/')
def films():
    return data

@app.route('/films', methods=["POST","GET","DELETE"]) # type: ignore
def addFilm():
    if request.method=='GET':
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

        return 'film added'
    
# @app.route('/films/{id}'.format(id=request.get_json()["imdbid"]), methods=["GET"]) #type: ignore
# def getFilmById():
#     return [x for x in lista_filme if x.imdbid==id]
         

