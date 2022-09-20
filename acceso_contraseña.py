'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 5: Funciones
Ejercicio 4: Realizar un programa que solicite inicialmente un nombre de usuario y una contraseña, posteriormente
             simular un inicio de sesión, donde el usuario capturara un nombre de usuario y una contraseña, si estos
             son iguales a los datos ingresados inicialmente se indicara un “feliz inicio de sesión” de lo contrario
             indicara un “información incorrecta”. Se tendrá un máximo de 4 intentos, de lo contrario, se deberá
             indicar que no se pudo acceder. El programa deberá retorna la cantidad de intentos que se realizaron
             para iniciar sesión.
Fecha: 22 De Septiembre De 2022
'''

def acceso (user,password):
    print("2 Horas Más Tarde...")
    usuario=str(input("Nombre De Usuario: "))
    contrasena=str(input("Contraseña: "))
    intentos=1
    if usuario!=user or contrasena!=password: # Si Los Datos No Coinciden
        while (usuario!=user or contrasena!=password) and intentos<4: # Ciclo Para Seguir Intentando
            print("Información Incorrecta")
            usuario=str(input("Nombre De Usuario: "))
            contrasena=str(input("Contraseña: "))
            intentos+=1
            if intentos==4:
                print("No Se Puede Acceder A La Cuenta")
                break
            elif usuario==user and contrasena==password: # Se Muestra Cuando Los Datos Coinciden
                print("Feliz Inicio De Sesión")
    else:
        print("Feliz Inicio De Sesión")
