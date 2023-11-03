mapaPalabras = {}
palabra = ""
nveces = 0

def contarPalabras():
    with open("message_01.txt") as archivo:
        for linea in archivo:
            for palabra in linea.split():
                #print(palabra)
                if palabra in mapaPalabras:
                    mapaPalabras[palabra] = mapaPalabras[palabra] + 1
                else:
                    mapaPalabras[palabra] = 1

            

contarPalabras()

solucion = ""

for key in list(mapaPalabras.keys()):
    print(key, mapaPalabras[key])
    solucion += key + str(mapaPalabras[key])

sortedMapa = sorted(mapaPalabras.items(), key=lambda x:x[1], reverse=True)
 
#print(sortedMapa)
#print(mapaPalabras)
print(solucion)