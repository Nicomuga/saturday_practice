#La funcion principal para manejar archivos
# Esta funcion reibe dos parametros, el nombre del archivo y el modo
''' Los modos son:

r: para leer y da error si el archivo no existe

a: para realizar append (agregar al final). Si el archivo no existe, lo crea.

w: para reescribir. Elimina el contenido anterior si existe.'''

file = open('file_handling/example.txt', 'r')

# A la funcion read le podemos pasar un numero y va a imprimir esa cantidad de numeros
print(file.read(54))

#Tambien existe la funcion readline() que lee linea por linea

print('ejemplo de readline ()\n')
print(file.readline())
print(file.readline())

#debemos cerrar el archivo despues de usarlo. De lo contrario el sistema operativo considera al archivo como abierto y por lo tanto no se podra leer en el futuro
file.close()

