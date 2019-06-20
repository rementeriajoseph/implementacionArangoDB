# Este script debe ejecutarse en el mismo lugar donde se encuentran los datos que se desean cambiar.

def unir(lista):
    hilera = ""
    for valor in lista:
        hilera = hilera + valor + ","
    hilera = hilera[:-1]
    return hilera

indiceId = 0 # Este es el lugar donde se encuentra el id del archivo en el csv actual.
currentFile = "fares.txt" #Aqui va el archivo que se desea transformar
palabraClave = "fares/" #La "palabraClave" es lo que va a conformar el key, ej: fares/

otro = open("../DatosCambiados/" + currentFile, "a")
f = open(currentFile, "r")

primeraLinea = True
for x in f:
    lineaLista = x.split(",")
    if(primeraLinea) :
        primeraLinea = False
        lineaLista[indiceId] = "_key"
        union = unir(lineaLista)
        otro.write("_id," + union)
    else:
        valorId = lineaLista[indiceId]
        otro.write(palabraClave + valorId + "," + unir(lineaLista))
otro.close()
