

import string


print("Menu")
print("1. para ingresar datos")
print("2. para mostrar el saldo")
print("3. para editar el saldo")
print("4. para retirar el saldo")
print("5. Salir")
opcion=100

datos=[]

while(opcion !=0):
    opcion=int(input("***Digite una opcion: "))
    if(opcion==1):
        banco={}
        banco['nombre']= input("Digite el nombre: ")
        banco['apellido']=input("Digite el apellido: ")
        banco['cedula']=input("Digite la cedula: ")
        banco['ciudad']=input("Digite la ciudad: ")
        banco['nrocuenta']=input("Digite el numero de la cuenta: ")
        banco['saldo']=int(input("Digite el saldo: "))

        datos.append(banco)
        opcion=opcion+1
        print("se agregaron los datos exitosamente")
    elif(opcion==2):
        for saldo in datos:
            print(f"El saldo de tu cuenta es: {saldo['saldo']}")
    elif(opcion==3):
        for saldo in datos:
            datos[0]['saldo']=int(input("ingrese el valor a reemplazar: "))
    else:
        print("Digite los numeros del menu (-_-;)")
else:
    print("termine")