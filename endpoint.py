from flask import Flask
import requests

app = Flask(__name__)

url='https://ott-details.p.rapidapi.com/advancedsearch?start_year=2015&end_year=2020'
headers = {
    'X-RapidAPI-Key': "18158db10dmshfd301d948367abbp19c882jsn15f2b8d7fbc6",
    'X-RapidAPI-Host': "ott-details.p.rapidapi.com"
    }

data=requests.get(url,headers=headers).json()


@app.route('/')
def hello():
    return data

lista_filme=[]
for film in data['results']:
    lista_filme.append(film)

@app.route('/films')
def films():
    return lista_filme
