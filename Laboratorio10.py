# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 10:57:27 2020

@author: --
"""
# Informe laboratorio 10 - Desarrollo en Python
  
# -------- Paquetes y librerías -------- #

import numpy as np

# Funciones #

# zeros(n) retorna un arreglo con n cantidad de ceros cuando sea invocada

def zeros(n):
       return np.zeros(n)

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

# Desarrollo ejerc. 9.3, 9.3.1
    # a_power_b_bucle ha sido modificada para que el usuario ingrese
    # el número de parejas de potencias que desea resolver, que mínimo serán 5
    # la función termina la ejecución cuando se hayan ingresado n número de parejas
        # 9.3.1 a_power_b_bucle al invocar la función zeros(n) forma 2 arreglos
        # de n ceros, según el n inicial
            #Se usa for para que el valor de array_a o b cambie en cada vuelta
    
def a_power_b_bucle(n):    
    contador = 0
    par = 0
    impar = 0
    # func. zeros(n) invocada
    array_a = zeros(n)
    array_b = zeros(n)
    if n>=5:
        for i in range(n):
            a = int(input("Ingresar el valor de la base: "))
            b = int(input("valor de el exponente: "))
            # cambio de valor en arreglo, según a y b ingresados en vuelta i
            array_a [i] = a
            array_b [i] = b
            c = a_power_b(a, b)
            contador +=1
            #Impresión potencias
            print("La potencia de " + str(a) + " elevado a la " + str(b) + " es: " + str(c))
            if (c%2 == 0):
                par += 1
            elif (c%2 == 1):
                impar += 1
        print("Ud hizo", contador, "potencias")
        print("Ud hizo", par, "potencias pares")
        print("Ud hizo", impar, "potencias impares")
    else:
        print("Ud quiere calcular menos de 5 potencias. FIN.")
    #Impresión arreglos
    print ("Arreglo de bases", array_a)
    print ("Arreglo de exponentes", array_b)

# n es la cantidad de potencias que se calcularán
n = int(input("Ingresar una cantidad a calcular: "))
a_power_b_bucle(n)