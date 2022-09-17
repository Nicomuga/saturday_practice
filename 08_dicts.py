#Los diccionarios al igual que los arreglos nos permite guardar conexiones, pero accedemos a sus elementos mediante la llave.

student = {
    'name' : 'Bob',
    'lastname' : 'Esponja',
    'grades' : [7, 6.5, 7, 6.6, 5],
    'adress' : 'Casa pina en el fondo de bikini'
}

# La variable sum nos sirve como variable acumuladora, una variable auxiliar
aux_sum = 0
for grade in student['grades']:
    aux_sum = aux_sum + grade

average = aux_sum/len(student['grades'])
print(sum)
print(average)

print('nombre:', student['name'], student['lastname'])
print('student:', student['adress'])

'''
# este metodo requiere importar el modulo math
import math

#fsumcsirve para sumar datos en formato float, si se desea sumar numeros enteros se utiliza el sum
alternative_sum = math.fsum(student[grades])
average = alternative_sum/len(estudent[grades])'''

#Tambien se puede sumar con la funcion sum sin necesidad de llamar a math

numbers = [1,2,3]
last_sum = sum(numbers)

print(last_sum)