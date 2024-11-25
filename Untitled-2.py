print("holaa")
deportes=["futbol","voleibol","natacion","basquetbol"]
print(deportes)
print(deportes[1])
pos=deportes.index("natacion")
print("la posicion de natacion es:", pos)
print(deportes.index("natacion"))
#agregar otro deporte al final
deportes.append("hanball")
print(deportes)
deportes.insert(2,"tenis")
print(deportes)

#for i in range(num):

cantidad_saludos=int(input("¿cuantos saludos quieres?"))
for i in range(cantidad_saludos):
    print("hola")

num_deportes=int(input("cuantos deportes agregaras: "))
for i in (range(num_deportes)):
    dep=input("ingresa deporte")
    deportes.append(dep)

print(deportes)

equipo=["emma"]
num_integrantes=int(input("¿cuantos integrantes mas va a agregar?: "))
for i in (range(num_integrantes)):
    integrantes=input("ingresa el integrante: ")
    equipo.append(integrantes)
print("tu equipo es: ", equipo) 




