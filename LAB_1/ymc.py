import requests
import socket


# Une fonction pour connaitre l'adresse ip d'un site web
def web_ip_adresse() :
    # envoyer une requête GET à un service d'adresse IP pour récupérer l'adresse IP publique
    url = input("URL : ")
    response = requests.get(url)
    # extraire l'adresse IP à partir de la réponse
    ip_adresse = response.text.strip()
    print(f"Votre adresse IP est : {ip_adresse}")


# Une fonction qui affiche son propre adresse Ip
def ip_adresse() :
    # récupérer le nom d'hôte de l'ordinateur
    hostname = socket.gethostname()
    # récupérer l'adresse IP associée au nom d'hôte
    ip_adresse = socket.gethostbyname(hostname)
    print(f"Votre adresse IP est : {ip_adresse}")


# Une fonction qui liste tout le methode d'une librarie
def method_list(*args) :  # ce *args definit que on peux entre n'inort quel argument  a la fonction
    for method in dir(*args) :
        if '__' not in method :
            print(method)


ip_adresse()






# url = ['http://www.google.ch']
# hostename = socket.getaddrinfo(url,80)
# adresse = socket.gethostname(hostename)
