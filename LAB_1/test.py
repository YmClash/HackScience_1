import random
from ymc import ip_adresse as ip

# fonctionpour genere de nombre  en indiquant  le min,max et ele nombre de chiffre aleatoire a genere dans
# le parametre de la fonction
def Gen_numb(min, max, numbre) :
    num = [random.randint(min, max) for i in range(numbre)]
    print(f"les {numbre} nombres genere entre {min} et {max} sont les suivant : {num}")



def gen_numb():
    min = input("Minimum: ")
    max = input("maxximum : ")
    numbre = input("Range: ")
    num = [random.randint(int(min),int(max)) for i in range(int(numbre))]
    print(f"Les {numbre} nombre genere entre {min} et {max} sont les suivant : {num})")

Gen_numb(0, 1000, 10)


ip = ip()
print(ip)
