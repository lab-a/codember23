#Para la solución de este reto he utilizado la estructura de datos Dictionary de Python para contar las palabras
#resultando en tupla por palabra del estilo (palabra, frecuencia)

mapaPalabras = {}

#La función contarPalabras() leerá cada palabra del fichero message_01.txt
#Si la palabra ya ha sido añadida al diccionario, se aumenta la frecuencia en +1
#Si no estaba la palabra, se inserta en el diccionario
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

#Muestra por pantalla el resultado del diccionario y se añade a un string solucion para moldear la solución al formato especificado
for key in list(mapaPalabras.keys()):
    print(key, mapaPalabras[key])
    solucion += key + str(mapaPalabras[key])

print(solucion)