

calorias= open("dia1/recurso.txt").read()
calorias=calorias.split("\n")
mayor=0
segundo_mayor=0
tercer_mayor=0

duendes=0
for cal in calorias:
  if cal=="":
    if(duendes>mayor):
      tercer_mayor=segundo_mayor
      segundo_mayor=mayor
      mayor=duendes

    duendes=0
  else:
    duendes=duendes+int(cal)

print(mayor+segundo_mayor+tercer_mayor)
