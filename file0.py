# Dans ce fichier on va créer des fonctions à utiliser dans nos prochains api

# 1- Fonction qui prend en entrée une date et renvoie le jour de la semaine

def jour_semaine(date: str) -> str:
    '''Fonction qui prend en entrée une date 
    au format AAAA-MM-JJ 
    et renvoie le jour de la semaine'''
    from datetime import datetime
    jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
    return jours[datetime.strptime(date, "%Y-%m-%d").weekday()]

# 2- Fonction qui prend en entrée une année et dis si oui ou nom c'est une année bissextile

def bissextile(annee: int) -> bool:
    '''Fonction qui prend en entrée 
    une année 
    et renvoie "True"
    si c'est une année bissextile 
    et "False" sinon'''
    return annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0)

# 3- Fonction qui prend en entrée le nom d'un pays et renvoie son/ses indicatifs téléphoniques

import phonenumbers
from phonenumbers.phonenumberutil import region_code_for_country_code, country_code_for_region

def pays_indicatif(pays: str)-> int:
    '''Fonction qui prend en entrée 
    le nom d'un pays (écris en anglais, la 1ere lettre en majuscule
    et renvoie son indicatif téléphonique'''
    def iso_to_ind(iso: str):
        '''Fonction qui prend en entrée un code ISO et renvoie l'indicatif téléphonique'''
        return f"+{country_code_for_region(iso)}"
    from pycountry import countries
    for country in countries:
        if country.name == pays:
            return iso_to_ind(country.alpha_2)
    return "Indicatif non trouvé, vérifiez le nom du pays"
    
# 4- Fonction qui prend en entrée l'indicatif téléphonique et renvoie le nom du pays

def indicatif_pays(indicatif: int) -> str:
    '''Fonction qui prend en entrée l'indicatif téléphonique (sans le "+")
    et renvoie le nom du pays'''
    def ind_to_iso(ind: int):
        '''Fonction qui prend en entrée un indicatif téléphonique et renvoie le code ISO'''
        return region_code_for_country_code(ind)
    from pycountry import countries
    for country in countries:
        if country.alpha_2 == ind_to_iso(indicatif):
            return country.name
    return "Pays non trouvé, vérifiez l'indicatif"

# 5- Fonction qui prend en entrée le nom d'un pays et renvoie son code ISO

def pays_iso(pays: str) -> str:
    '''Fonction qui prend en entrée le nom d'un pays et renvoie son code ISO'''
    from pycountry import countries
    for country in countries:
        if country.name == pays:
            return country.alpha_2
    return "Code ISO non trouvé, vérifiez que le nom du pays est correct"

# 6- Fonction qui prend en entrée le code ISO et renvoie le nom du pays

def iso_pays(iso: str) -> str:
    '''Fonction qui prend en entrée 
    le code ISO (2 lettres majuscules)
    et renvoie le nom du pays'''
    from pycountry import countries
    for country in countries:
        if country.alpha_2 == iso:
            return country.name
    return "Pays non trouvé, vérifiez le code ISO"

# testons les fonctions
# date = "2000-08-26"
# année = 2025
# ind1 = 237
# ind2 = 33
# pays1 = "Cameroon"
# pays2 = "France"
# iso1 = "CM"
# iso2 = "FR"
# print(f"jour de {date} =",jour_semaine(date))
# print(f"{année} bissextile?",bissextile(année))
# print(f'+{ind1} pour ',indicatif_pays(ind1))
# print(f"{pays1} = ",pays_indicatif(pays1))
# print(f"{pays1} abrégé = ",pays_iso(pays1))
# print(f"{iso1} est l'iso de ",iso_pays(iso1))
# print(f'+{ind2} pour ',indicatif_pays(ind2))
# print(f"{pays2} = ",pays_indicatif(pays2))
# print(f"{pays2} abrégé = ",pays_iso(pays2))
# print(f"{iso2} est l'iso de ",iso_pays(iso2))
