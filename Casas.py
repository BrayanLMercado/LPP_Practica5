'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 5: Funciones
Ejercicio 3: Una empresa de bienes raíces ofrece casas de interés social, bajo las siguientes condiciones:
             Si los ingresos del comprador son $8,000 pesos o menos, el enganche será del 15% del costo de la
             casa y el resto se distribuirá en pagos mensuales, a pagar en 15 años.
             Si los ingresos del comprador son mayores a $8,000 pesos, el enganche será del 30% del costo de la
             casa y el resto se distribuirá en pagos mensuales a pagar en 7 años.
             La empresa quiere obtener cuánto debe pagar un comprador por concepto de enganche y cuánto por
             cada pago parcial.
             Especificaciones:
                - Es necesario hacer una función para cada caso.
                - Cada función deberá calcular e imprimir el monto de enganche y mensualidades requeridas.
                - Las funciones deberán recibir dos valores: el costo de la casa y los ingresos del comprador.
Fecha: 22 De Septiembre De 2022
'''

def opcPago1 (costo,ingresos):
    enganche=costo*0.15
    pagoRestante=costo-enganche
    mensualidadesTotales=12*15
    pagoMensual=pagoRestante/mensualidadesTotales
    print("Monto De Enganche:",enganche)
    print(mensualidadesTotales,"Mensualidades Requeridas De",round(pagoMensual,2))

def opcPago2 (costo,ingresos):
    enganche=costo*0.30
    pagoRestante=costo-enganche
    mensualidadesTotales=12*7
    pagoMensual=pagoRestante/mensualidadesTotales
    print("Monto De Enganche:",enganche)
    print(mensualidadesTotales,"Mensualidades Requeridas De",round(pagoMensual,2))

