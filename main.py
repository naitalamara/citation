import random
import json


def fonction(my_list):
    indice=random.randint(0, len(my_list) -1)
    item=my_list[indice]
    return (item)

def capital(mot):
    for item in mot :
        item.capitalize()

def message(auteur,phrase):
    capital(auteur)
    capital(phrase)
    return "{} a dit : {} ".format(auteur, phrase)


def lecture_fichier():
    valeur = []
    with open("caract.json") as f :
        data=json.load(f)
        for item in data:
            valeur.append(item['quote'])
    return valeur


def lecture_fichier2():
    valeur = []
    with open("auteur.json") as f :
        data=json.load(f)
        for item in data:
            valeur.append(item['character'])
    return valeur


def random_charact():
    data=lecture_fichier()
    return fonction(data)


def random_charact2():
    data=lecture_fichier2()
    return fonction(data)

user_answer=input("Tapez entrée pour connaitre une autre citation ou B pour quitter  ")
while user_answer != "B":
    print(message(random_charact(),random_charact2()))
    user_answer = input("Tapez entrée pour connaitre une autre citation ou B pour quitter")

print("Merci Aurevoirs")