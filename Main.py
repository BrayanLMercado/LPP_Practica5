'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 5: Funciones
Archivo Principal
Fecha: 22 De Septiembre De 2022
'''

from Factorial import*
from entrada_fiesta import*
from Casas import*
from acceso_contraseña import*

print("           Menu         ")
print("1) Factorial De Un Número")
print("2) Entrada A La Fiesta")
print("3) Compra De Casas Y Mesualidades")
print("4) Usuario y Contrseña")
print("5) Salir")

opc=int(input("Selecciona Una Opción: "))
while opc<0 or opc>5:
    print("Captura Una Opción Valida")
    opc=input("Selecciona Una Opción: ")

if opc==1:
    num=int(input("Captura Un Número: "))
    print("El Factorial De",num,"Es",factorial(num))
elif opc==2:
    edad=int(input("¿Cuantos Años Tienes? "))
    while edad<0 :
        print("Captura Una Edad Valida")
        edad=int(input("¿Cuantos Años Tienes? "))
    entrada(edad)
elif opc==3:
        ingresos=float(input("Ingresos Al Mes: "))
        costo=float(input("Costo De La Casa Que Desea Comprar: "))
        while ingresos<0 or costo<0:
            print("Captura Valores Validos")
            ingresos=float(input("Ingresos Al Mes: "))
            costo=float(input("Costo De La Casa Que Desea Comprar: "))
        if ingresos<=8000:
            opcPago1(costo,ingresos)
        else:
            opcPago2(costo,ingresos)
elif opc==4:
    user=str(input("Nombre Del Nuevo Usuario: "))
    password=str(input("Contraseña Del Nuevo Usuario: "))
    acceso(user,password)

else:
    print("Gracias Por Usar El Programa")
