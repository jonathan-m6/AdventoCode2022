datos= open("dia5/recurso.txt").read()

cajas=datos.split("--")[0]
cajas=cajas.split("\n")

movimientos=datos.split("--")[1]
movimientos=movimientos.split("\n")
cajas_dict=dict()

def mover_cajas(start,origen,destino):
  cajas_mover=cajas_dict[origen][start:]
  cajas_dict[destino]=cajas_dict[destino]+cajas_mover
  indice=len(cajas_dict[origen])
  while indice>start:
    cajas_dict[origen].pop()
    indice-=1

for i in range(len(cajas)):
  cajas_dict[str(i+1)]=cajas[i].split(",")
movimientos_list=[]
for item in movimientos:
  instrucciones=dict()
  instrucciones["mover"]=item.split(" ")[1]
  instrucciones["origen"]=item.split(" ")[3]
  instrucciones["destino"]=item.split(" ")[5]
  movimientos_list.append(instrucciones)
for item in movimientos_list:
  length=len(cajas_dict[item["origen"]])
  start=length-int(item["mover"])
  mover_cajas(start,item["origen"],item["destino"])
salida=""
for item in cajas_dict:
  salida+=cajas_dict[item][-1]
print(salida)
