print("holaaaa")

edad=int(input("ingresa tu edad: "))
if(edad>=18):
    print("eres mayor de edad")
else:
    print("eres menor de edad")

temp=float(input("ingresa la temperatura: "))
if(temp<=0):
    print("hace frio abrigate")
elif(temp>0 and temp<=35):
    print("esta templado")
elif(temp>35 and temp<=100):
    print( "hace mucho calor")
else:
    print("temperatura no valida")

cantidad_saludos=int(input("¿cuantos saludos quieres?"))
for i in range(cantidad_saludos):
    print("hola")

num_deportes=int(input("cuantos deportes agregaras"))
for i in (range(num_deportes)):
    dep=input("ingresa deporte")
    deportes.append(dep)

print(deportes)



