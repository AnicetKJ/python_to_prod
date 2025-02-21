import requests
import pandas as pd

# Lecture (GET) de l'API
response = requests.get("https://jsonplaceholder.typicode.com/posts")
# print(response.json())

# Création d'un DataFrame
df = pd.DataFrame(response.json())
# print(df.head())

# Créer (POST) un nouvel élement
new_post = {
    "userId": 1,
    "title": "Nouveau titre",
    "body": "Nouveau contenu"
}
response = requests.post("https://jsonplaceholder.typicode.com/posts", data=new_post)
print(response.json())

# Modifier (PUT) un élément
id_post = 2
update_post = {
    "title": "Titre modifié",
    "body": "Contenu modifié"
}
response = requests.put(f"https://jsonplaceholder.typicode.com/posts/{id_post}", data=update_post)
print(response.json())

# Supprimer (DELETE) un élément
id_post = 2
response = requests.delete(f"https://jsonplaceholder.typicode.com/posts/{id_post}")
print(response.status_code)