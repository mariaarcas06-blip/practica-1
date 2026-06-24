pin_correcto = 4321
contador_intentos = 0
max_intentos = 3

#pedir mientras queden intentos
while contador_intentos < max_intentos: 
    entrada= int(input("ingrese su pin: "))

    if entrada== pin_correcto:
        print ("acceso concedido")
        break
    else:
        print ("pin incorrecto")
        contador_intentos +=1 

if contador_intentos==max_intentos:
    print ("tarjeta bloqueada")
      
     
        