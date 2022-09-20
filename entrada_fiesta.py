'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 5: Funciones
Ejercicio 2: María va a realizar su fiesta de quince años. Por lo cual ha invitado a una gran cantidad personas, pero
             también ha decidido algunas reglas. Escriba un programa que utilice una función que pida la edad de
             la persona e imprima en qué situación se encuentra:
            - Todas las personas mayores de 15 sólo pueden entrar si traen regalo.
            - Los jóvenes de 15 entran gratis.
            - Los menores de 15 no pueden entrar.
Fecha: 22 De Septiembre De 2022
'''

def entrada(edad):
    if edad<15:
        print("Lo Sentimos, Pero No Puedes Entrar A La Fiesta")
    elif edad==15:
        print("Puedes Entrar A La Fiesta Gratis")
    else:
        print("Puedes Entrar, Pero Necesitas Un Regalo")
