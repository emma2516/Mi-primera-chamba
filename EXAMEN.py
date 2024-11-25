#NECESITO UNA VARIABLE QUE SE VA A USAR
#PARA TERMINAR EL CICLO
numero=1
while numero>0:
    emocion=input("¿como te sientes?")
    print("interesanteque te sientas", emocion)
    numero=int(input("permanecer en el programa, 0 salir"))

opcion=1
#en un ciclo while realiza operaciones hasta que el usuario escriba 0
while opcion!=0:
 num1=int(input("ingresa el primer numero"))
 num2=int(input("ingresa el segundo numero"))
 print("ingresa 1. sumar")
 print("ingresa 2.restar")
 print("ingresa 3. multiplicar")
 print("ingresa 4. dividir")
 op=int(input("¿que operacion quieres realizar?"))
 if (op==1):
    sum=num1+num2
    print("la suma de los numeros es:", sum)
 elif(op==2):
    res=num1-num2
    print("la suma de los numeros es:", res)
 elif(op==3):
    mul=num1*num2
    print("lñamultiplicacion de tus numeros es:", mul)
 elif(op==4):
    div=num1/num2
    print("la divicion de tus numeros es:", div)
 else:
    print("no valido")
opcion=int(input("deseas continuar, si no preciona 0, para salir"))
 

    
    