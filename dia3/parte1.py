import string


mochilas= open("dia3/recurso.txt").read()
mochilas=mochilas.split("\n")

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
minusculas=list(string.ascii_lowercase)
mayusculas=list(string.ascii_uppercase)

puntos=dict()
for i in range(len(minusculas)):
  puntos[minusculas[i]]=i+1
for i in range(len(mayusculas)):
  puntos[mayusculas[i]]=i+27

intersectiones=[]
for item in mochilas:
  mitad=int(len(item)/2)
  intersectiones.append(intersection(item[0:mitad],item[mitad:])[0])

suma=0
for item in intersectiones:
  suma+=puntos[item]
print(suma)