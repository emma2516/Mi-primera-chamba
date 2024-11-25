opcion=1
print("holaaa" )
nombre=input("¿como te llamas?")
print("bienvenido ", nombre, "a tu calculadora")
while opcion!=0:
    print("ingresa 1. para Area de triangulo")
    print("ingresa 2. para Area de rectangulo")
    print("ingresa 3. para Area de circulo")
    print("ingresa 4. para Convertir temperatura F a C")
    print("ingresa 5. para Convertir temperatura C a F")
    print("INGRESA 0. para salir")
    op=int(input("¿que actividad quieres realizar?"))

    if(op==1):
        b1=int(input("¿cuanto mide su base?"))
        h1=int(input("¿cuanto mide de altura?"))
        a1=b1*h1/2
        print(" tu triangulo tiene un area de ", a1)

    elif(op==2):
        b2=int(input("¿cuanto mide su base"))
        h2=int(input("¿cuanto mide de altura?"))
        a2=b2*h2
        print(" tu rectangulo tiene un area de ", a2)

    elif(op==3):
      rad=int(input("¿de cuanto es su radio?"))
      a3=rad*rad*3.1416
      print("su area mes de: ", a3)

    elif(op==4):
     f=int(input("¡cuantos grados Fahrenheit deseas convertir?"))
     c=(f-32)*5/9
     print("el resultado es: ", c)

    elif(op==5):
     C=int(input("¡cuantos grados  deseas convertir?"))
     F=(C*9/5)+32
     print("equivale a :", F, " grados Fahrenheit")

    else:
     print("ingresa una de las opciones mencionadas")
opcion=int(input("deseas continuar, si no preciona 0, para salir"))

        
