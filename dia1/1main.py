

calorias= open("dia1/recurso.txt").read()
calorias=calorias.split("\n")
mayor=0
duendes=0
for cal in calorias:
  if cal=="":
    if(duendes>mayor):
      mayor=duendes
    duendes=0
  else:
    duendes=duendes+int(cal)

print(mayor)
