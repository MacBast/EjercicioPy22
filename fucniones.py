ciclistas=[]

def crearCiclista():
    ciclista={}
    ciclista['nombre']=(input("Dijite nombre del ciclista: "))
    ciclista['edad']=(input("Dijite edad del ciclista: "))
    ciclista['pais']=(input("Dijite pais del ciclista: "))
    ciclista['equipo']=(input("Dijite equipo del ciclista: " ))
    ciclista['tiempoEnMinutos']=(int(input("Dijite tiempo en minutos del ciclista: ")))
    return ciclista

def calcularTime():
    tiempoMeno=300
    for ciclista in ciclistas:
        tmc=ciclista['tiempoEnMinutos']
        if (tmc<tiempoMeno):
            nombre=ciclista['nombre']
            equipo=ciclista['equipo']
            tiempoMeno=tmc
    print(f'Con un tiempo de {tmc}minutos el nombre del ciclista ganador es: {nombre} ')
    print(f'El equipo de {nombre} es {equipo}')
