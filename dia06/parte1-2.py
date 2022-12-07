
flujo= open("dia6/recurso.txt").read()

def tiene_repetidos(cadena):
  i=0
  while i<len(cadena):
    letra=cadena[i]
    y=0
    while y <len(cadena):
      if i!=y:
        if letra==cadena[y]:
          return True
      y+=1
    i+=1
  return False

indice=3
while indice<len(flujo):
  stop=indice-4
  i=indice
  cuatro_recientes=""
  while i>stop:
    cuatro_recientes+=flujo[i]
    i-=1
  if not tiene_repetidos(cuatro_recientes[::-1]):
    print(indice+1)
    break
  indice+=1
""" for letra in flujo:
  print(letra) """
