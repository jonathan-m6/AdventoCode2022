pares= open("dia4/recurso.txt").read()
pares=pares.split("\n")

contains=0


for item in pares:
  pares_elfos=item.split(",")

  start1=int(pares_elfos[0].split("-")[0])
  end1=int(pares_elfos[0].split("-")[1])
  start2=int(pares_elfos[1].split("-")[0])
  end2=int(pares_elfos[1].split("-")[1])
  array_pares1=list(range(start1,end1+1))
  array_pares2=list(range(start2,end2+1))
  if len(array_pares1)<len(array_pares2):
    if (start1>=start2 and start1<=end2) or (end1>=start2 and end1<=end2):
      contains+=1
  else:
    if (start2>=start1 and start2<=end1) or (end2>=start1 and end2<=end1):
      contains+=1
print(contains)

