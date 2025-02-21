from fastapi import FastAPI
import uvicorn
import file0
from random import randint
app = FastAPI()

@app.get("/")
def accueil():
    return {"Bonjour": "Bienvenue sur notre API"}

@app.get("/hasard")
def aleatoire():
    '''Retourne un nombre aléatoire entre 0 et 100'''
    return {"nombre aleatoire entre 0 et 100": randint(0, 100)}

@app.get("/hasard/{min}_{max}")
def aleatoire(min: int, max: int):
    '''Retourne un nombre aléatoire entre min et max'''
    return {
        f"nombre aleatoire entre {min} et {max}": randint(min, max)
        }

@app.get("/jour_semaine/{date}")
def weekday(date: str):
    '''Retourne le jour de la semaine correspondant à la date au format AAAA-MM-JJ'''
    return {"jour de la semaine": file0.jour_semaine(date)}

@app.get("/bissextile/{annee}")
def bissextile(annee: int):
    '''Retourne si l'année est bissextile ou non'''
    return {"bissextile": file0.bissextile(annee)}

@app.get("/pays/{nom_pays}")
def infos_pays(nom_pays: str):
    '''Retourne les infos sur un pays (indicatif et code ISO)
    Veuillez écrire le nom du pays en anglais avec la 1ere lettre en majuscule'''
    return {
        "indicatif": file0.pays_indicatif(nom_pays),
        "code ISO": file0.pays_iso(nom_pays)
    }

@app.get("/indicatif_pays/{indicatif}")
def infos_indicatif(indicatif: int):
    '''Entrer l'indicatif téléphonique pour obtenir le nom du pays correspond
    Veuillez entrer l'indicatif sans le "+" '''
    return {"pays": file0.indicatif_pays(indicatif)}

@app.get("/iso_pays/{iso}")
def infos_iso(iso: str):
    '''Entrer le code ISO (2 lettres majuscules) pour obtenir le nom du pays correspond '''
    return {"pays": file0.iso_pays(iso)}


