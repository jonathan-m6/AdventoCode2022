pares= open("dia4/recurso.txt").read()
pares=pares.split("\n")

contains=0
for item in pares:
  pares_elfos=item.split(",")

  array_pares1=list(range(int(pares_elfos[0].split("-")[0]),int(pares_elfos[0].split("-")[1])+1))
  array_pares2=list(range(int(pares_elfos[1].split("-")[0]),int(pares_elfos[1].split("-")[1])+1))
  str_pares_elfos1=",".join(map(str,array_pares1))
  str_pares_elfos2=",".join(map(str,array_pares2))
  if len(array_pares1)>len(array_pares2):
    if array_pares2[0]>=array_pares1[0]:
      if str_pares_elfos1.find(str_pares_elfos2)!=-1:
        contains+=1
  else:
    if array_pares1[0]>=array_pares2[0]:
      if str_pares_elfos2.find(str_pares_elfos1)!=-1:
        contains+=1



print(contains)

