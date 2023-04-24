nombre1 = ""
nombre2 = ""
contador1 = 0
contador2 = 0
estado = 0
jgj2 = 0
Jgj1 = 0
nj = ""
punto = ''

def puntaje():
    global contador1
    global contador2
    punto = str(input("Que jugador hizo punto? "))
    if contador1 < 30  and contador2 < 30:
        
        if punto == nombre1:
            contador1 += 15
            contador2 += 0
            print('Puntaje')
            print(f'{nombre1}: [{contador1}] - {nombre2}: [{contador2}]')
            return contador1
        
        elif punto == nombre2:
            contador2 += 15
            contador1 += 0
            print('Puntaje')
            print(f'{nombre1}: [{contador1}] - {nombre2}: [{contador2}]')
            return contador2
        
    elif contador1 < 30 and contador2 > 30 :
        
        if punto == nombre1:
            contador1 += 15
            contador1 += 0
            print('Puntaje')
            print(f'{nombre1}: [{contador1}] - {nombre2}: [{contador2}]')
            return contador1
        
        elif punto == nombre2:
            contador2 += 10
            contador1 += 0
            print('Puntaje')
            print(f'{nombre1}: [{contador1}] - {nombre2}: [{contador2}]')
            return contador2
        
    elif contador1 > 30 and contador2 < 30 :
        
        if punto == nombre1:
            contador1 += 10
            contador1 += 0
            print('Puntaje')
            print(f'{nombre1}: [{contador1}] - {nombre2}: [{contador2}]')
            return contador1
        
        elif punto == nombre2:
            contador2 += 15
            contador1 += 0
            print('Puntaje')
            print(f'{nombre1}: [{contador1}] - {nombre2}: [{contador2}]')
            return contador2
        
    else:
        
        if punto == nombre1:
            contador1 += 10
            contador2 += 0
            print('Puntaje')
            print(f'{nombre1}: [{contador1}] - {nombre2}: [{contador2}]')
            return contador1
        
        elif punto == nombre2:
            
            contador2 += 10 
            contador1 += 0
            print('Puntaje')
            print(f'{nombre1}: [{contador1}] - {nombre2}: [{contador2}]')
            return contador2

def Ganador():
    global estado
    if contador1 > contador2:
        if contador1-contador2 > 10:
            print(f"Gana {nombre1}")
            estado = 1
            return estado
        else:
            print("Es necesaria otra ronda")
            estado = 3
            return estado
    elif contador2 > contador1:
        if contador2-contador1 > 10:
            print(f"Gana {nombre2}")
            estado = 2
            return estado
        else:
            print("Es necesaria otra ronda")
            estado = 3
            return estado
    else:
        print("Es un empate es necesario otra ronda")
        estado = 3
        return estado
    
def desempate():
    global de
    de = 0
    punto = input("Que jugador hizo punto ")
    if punto ==  nombre1:
        if punto == nombre1:
            print(f"Gana jugador {nombre1}")
            de = 1
            return de
        else:
            print('No se pudo desempatar')
            de = 3
            return de
    elif punto == nombre2:
        if punto == nombre2:
            print(f"Gana jugador {nombre2}")
            de = 2
            return de
        else:
            print('No se pudo desempatar')
            de = 3
            return de

def juegos_ganados():
    global Jgj1
    global jgj2
    if estado == 1:
        Jgj1 += 1
        print('Puntaje global')
        print(f'{nombre1}: [{Jgj1}] - {nombre2}: [{jgj2}]')
        return Jgj1
    elif estado == 2:
        jgj2 += 1
        print('Puntaje global')
        print(f'{nombre1}: [{Jgj1}] - {nombre2}: [{jgj2}]')
        return jgj2
    else:
        print('Puntaje global')
        print(f'{nombre1}: [{Jgj1}] - {nombre2}: [{jgj2}]')


nombre1 = str(input("Por favor ingrese el nombre del jugador 1 "))
nombre2 = str(input("Por favor ingrese el nombre del jugador 2 "))

    
while True:
    print(f'Jugador 1 es {nombre1}')
    print(f'jugador 2 es {nombre2}')
    
    for i in range(8):
        puntaje()
        if contador1 >= 40 | contador2 >= 40:
            break   
    Ganador()
    juegos_ganados()
    if estado == 1 | estado == 3 :
        break
    else:
        for i in range(4):
            desempate()
            if de == 3:
                desempate()
            else:
                break
