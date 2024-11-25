#CREAR UNA FUNCION

#FUNCION llamada saludar, va a recivir el nombre
def saludar(nombre):
    print("Holaaa",nombre)

nom=input("ingresa tu nombre")
saludar(nom)

#funcion llamada sumita, va a recibir 5 numeros
#va a regresar el valor de la suma
def sumita(n1,n2,n3,n4,n5):
    res_suma=n1+n2+n3+n4+n5
    return res_suma

num1=int(input("ingresa el primer numero"))
num2=int(input("ingresa el segundo numero"))
num3=int(input("ingresa el tercero numero"))
num4=int(input("ingresa el cuarto numero"))
num5=int(input("ingresa el quinto numero"))

#mandar llamar a la funcion/ USARLA
print(sumita(num1, num2, num3, num4,num5)) 

#crear una funcion llamada area_triangulo
#que reciba base y altura
#regresa el sesultado de la area 
def area_triangulo(b,h):
    area=(b*h)/2
    return area
#usar la funcion
print(area_triangulo(4,5))

######EJERCICIOS
'1)Crear una funcion llamada multiplicar que reciva 3 numeros, regrese el resultado'
def multiplicar(N1,N2,N3):
    resultado=N1*N2*N3
    return resultado
    

#USAR LA FUNCION 
print(multiplicar(4,5,5))
'2)Crear una funcion llamada largo_Cadena que reciba un texto y devuelva la cantidad de caracteres de la misma'
def largo_cadena(texto):
    caracteres=len(texto)
    return caracteres

text=input("ingresa tu texto para contar los caracteres")
print(largo_cadena, text)

#usar funcion
#print(largo_cadena)("el mundo es bonito"))
'3)crear una funcion llamada promedo que reciva 2 calificaciones y devuelva el promedio'
def promedio(cal1, cal2):
    res_prom=(cal1+cal2)/2
    return res_prom

#pedir calif. primer y segundo parcial
c1=float(input("ingresa calf1"))
c2=float(input("ingresa calf2"))
print ("el promedio es:", promedio(c1, c2))