#Menu
#Nombre, edad, País, Equipo y tiempo en minutos
from fucniones import crearCiclista, calcularTime, ciclistas

print("**MENU**")
print("0.SALIR")
print("1.Agregar ciclista")
print("2.Calcular Ciclista mas rapido")

observador=100

while(observador !=0):
    observador=int(input("Digite una opcion  (▀̿̿Ĺ̯̿▀̿ ̿): "))
    if(observador==0):
        print("Chao pichurria 凸-_-凸")
    elif(observador==1):
        if(ciclistas != []):
            print(f'Estos son los ciclistas {ciclistas}')
        ciclistas.append(crearCiclista())
    elif(observador==2):
        calcularTime()
    else:
        print("Digite los numeros del menu (-_-;)")
else:
    print("termine")
