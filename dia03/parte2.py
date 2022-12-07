import string

mochilas= open("dia3/recurso.txt").read()
mochilas=mochilas.split("\n")

minusculas=list(string.ascii_lowercase)
mayusculas=list(string.ascii_uppercase)

puntos=dict()
for i in range(len(minusculas)):
  puntos[minusculas[i]]=i+1
for i in range(len(mayusculas)):
  puntos[mayusculas[i]]=i+27

intersectiones=[]
i=0
while i<len(mochilas):
  m1=set(mochilas[i])
  m2=set(mochilas[i+1])
  m3=set(mochilas[i+2])
  i+=3
  intersectiones.append(m1&m2&m3)

suma=0
for item in intersectiones:
  insignia=list(item)[0]
  suma+=puntos[insignia]
print(suma)