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

# Desarrollo ejerc. 9.1
    # a_power_b_bucle calcula todas las potencias que el usario pida, se detiene
    # cuando el usuario introduce a = 0
        #Se usa un while, que se ejecutara hasta que a sea 0

def a_power_b_bucle():
    while True:
        a = int(input("Ingresar el valor de la base: "))
        if not a:
            print("Ha introducido base = 0. FIN.")
            break
        b = int(input("valor de el exponente: "))
        #Si a no es 0, se ejecutará también la función a_power_b invocada
        c = a_power_b(a, b)
        print("La potencia de " + str(a) + " elevado a la " + str(b) + " es: " + str(c))

a_power_b_bucle() 