# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 10:57:27 2020

@author: --
"""
# Informe laboratorio 10 - Desarrollo en Python
  
# Desarrollo ejerc. 7 potencia, sin usar ** ni librería math

# a_power_b retorna al ser invocada, el resultado de elevar "a" a la "b"
    #Se usa un for para multiplicar "a" por sí mismo, "b" cantidad de veces
    #Se usa if para algunas condiciones, p. Ej, si b es negativo
def a_power_b(a, b):
    acumul=1
    acumul2=1
    for i in range (abs(b)):
        if b < 0:
            acumul2 *= a
            acumul = (1/acumul2)
        else:
            acumul *= a
    return acumul

# Desarrollo ejerc. 9.2
    # a_power_b_bucle sigue calculando todas las potencias que el usario pida y se detiene
    # cuando el usuario introduce a = 0
        #Se usa un while, que se ejecutara hasta que a sea 0
        #Adicionalmente ahora cuenta el número de potencias realizadas 
        #y cuántas veces el resultado fue para o impar
def a_power_b_bucle():
    contador = 0
    par = 0
    impar = 0
    while True:
        a = int(input("Ingresar el valor de la base: "))
        if not a:
            print("Ha introducido base = 0. FIN.")
            print("Ud hizo", contador, "potencias")
            print("Ud hizo", par, "potencias pares")
            print("Ud hizo", impar, "potencias impares")
            break
        b = int(input("valor de el exponente: "))
        c = a_power_b(a, b)
        #Si a no es 0, se ejecutará también la función a_power_b invocada        
        contador +=1
        print("La potencia de " + str(a) + " elevado a la " + str(b) + " es: " + str(c))
        if (c%2 == 0):
            par += 1
        elif (c%2 == 1):
            impar += 1

a_power_b_bucle()