import time
#Este programa ayuda a saber si podemos hacer un triangulo dadas 3 longitudes

print("Hola te voy a ayudar con eso de los triangulos")
l1 = int(input("Ingresa la longitud uno\n"))
l2 = int(input("Ingresa la longitud dos\n"))
l3 = int(input("Ingresa la longitud tres\n"))

print("Las longitudes entregadas hasta el momento son!")

print(l1,l2,l3)

a1 = [l1,l2,l3]


if(l1 <= l2+l3):
    print("vamos bien, revisemos el siguiente")
    time.sleep(0.5)
    if(l2 <= l1+l3):
        print("vamos bien, revisemos el siguiente")
        time.sleep(0.5)
        if(l3 <= l1+l2):
            print("Si es posible el triangulo")
        else: 
            print('No es posible el triangulo', l3, 'No es menor que ', l1, "+", l2)
    else: 
        print('No es posible el triangulo', l2, 'No es menor que ', l1, "+", l3)
else: 
    print('No es posible el triangulo.', l1, 'No es menor que ', l2, "+", l3 )