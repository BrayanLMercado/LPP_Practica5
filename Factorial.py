'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 5: Funciones
Ejercicio 1: Elaborar un programa que utilice una función que retorne
             el factorial de un número capturado por el usuario.
Fecha: 22 De Septiembre De 2022
'''

def factorial(num):
    n=1
    fact=1
    while n<num+1:
        fact*=n
        n+=1
    return fact

