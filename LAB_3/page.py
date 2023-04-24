import random
import secrets
import lorem




data = {'Nom':'YMC','Race':'Humain','Origine':'Africain','Vaisseau':'Going Merry'}

for e in data:
    print(e,data[e],sep=":")


numb = [secrets.randbelow(100) for i in range(10)]

text = lorem.sentence()

print(numb)
print(text)





