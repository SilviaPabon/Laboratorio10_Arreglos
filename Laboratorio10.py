# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 10:57:27 2020

@author: --
"""
# Informe laboratorio 10 parte  
# Desarrollo ejerc. potencia, sin usar ** ni librería math

# lín. 16, Se realiza un ciclo for, donde "a" será multiplicado por sí mismo, n veces según sea el valor de b
    # 16 Se utiliza valor absoluto para cuando b sea negativo
    # Cuando hay exponentes negativos, n < 0, la potencia queda de la forma 1/(a**(n))

def a_power_b_(a, b):
    acumul=1
    acumul2=1
    for i in range (abs(b)):
        if b < 0:
            acumul2 *= a
            acumul = (1/acumul2)
        else:
            acumul *= a
    return acumul

# a es la entrada para el número que es la base 
a = int(input("Ingresar el valor de la base: "))
# b es la entrada para el número que es la base
b = int(input("Ingresar el valor del exponente: "))

# invocación de la función para luego imprimir el resultado
c= a_power_b_(a, b)

print("La potencia de " + str(a) + " elevado a la " + str(b) + " es: " + str(c))