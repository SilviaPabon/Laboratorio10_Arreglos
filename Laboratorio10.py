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
    #b no puede ser float porque no se pueden dar 1,3 vueltas
def a_power_b(a, b):
    acumul=1
    acumul2=float(1)
    for i in range (abs(b)):
        if b < 0:
            acumul2 *= a
            acumul = (1/acumul2)
        else:
            acumul *= a
    return acumul

# 9.3.2 mean_arreglo(array) función para hallar el promedio de los valores
    # de un arreglo unidimensional, no importa el tamaño ni contenido del arreglo

def mean_arreglo(array):
    long = len(array)
    sumat = 0
    for i in range (0, long):
        sumat += array[i]
    return sumat/long

# 9.3.4 función calcula la desviación estándar de arreglo unidimensional

def std_arreglo(array):
    acumul = 0
    for i in range(0, len(array)):
        mean_arreglo(array)
        cuad = (array[i] - mean_arreglo(array))**2
        acumul += cuad
        div = acumul / len(array)
        desviación = (div**(1/2))  
    return desviación   

# 9.3.6 función que estándariza los datos en un arreglo

def norm_arreglo(array):
    arraynorm = zeros(len(array))
    for i in range (0, len(array)):
        norm = (array[i]-mean_arreglo(array))/std_arreglo(array)
        arraynorm [i] = norm    
    return arraynorm

# Desarrollo ejerc. 9.3, 9.3.1
    # a_power_b_bucle ha sido modificada para que el usuario ingrese
    # el número de parejas de potencias que desea resolver, que mínimo serán 5
    # la función termina la ejecución cuando se hayan ingresado n número de parejas
        # 9.3.1 a_power_b_bucle al invocar la función zeros(n) forma 2 arreglos
        # de n ceros, según el n inicial
            #Se usa for para que el valor de array_a o b cambie en cada vuelta 
    
   
contador = 0
par = 0
impar = 0
# n es la cantidad de potencias que se calcularán   
n = int(input("Ingresar una cantidad a calcular: "))
# func. zeros(n) invocada 
array_a = zeros(n)
array_b = zeros(n)
if n>=5:        
    for i in range(n):
        a = float(input("Ingresar el valor de la base: "))
        b = int(input("Ingresar valor del exponente (no ingrese decimales): "))
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
    
    # Impresión arreglos
    
    print ("Arreglo de bases", array_a)
    print ("Arreglo de exponentes", array_b)
    
    # 9.3.2. se invoca la función mean_arreglo para calcular
    # el promedio de los arreglos obtenidos antes
    
    print ("Promedio arreglo bases", mean_arreglo(array_a))    
    print ("Promedio arreglo exponentes", mean_arreglo(array_b))
    
    # 9.3.3. Se invoca de nuevo la función a_power_b para obtener
    #la potencia b promedio de a promedio
    
    z = float(mean_arreglo(array_a))
    y = int(mean_arreglo(array_b))
    
        #En este resultado, si el valor que representa b es decimal, se obtendrá
        #potencia de a elevado al valor de b aproximado
    print ("Potencia b promedio(aproximado) de a promedio", a_power_b(z, y))
    
    # 9.3.5. Resultado de desviación estándar de arreglos a y b
    print ("Desviación estándar arreglo a :", std_arreglo(array_a))
    print ("Desviación estándar arreglo b :", std_arreglo(array_b))
    
    # 9.3.7. Resultado de normalización de valores de arreglo a y b
    print("Normalización arreglo a: ", norm_arreglo(array_a))
    print("Normalización arreglo b: ", norm_arreglo(array_b))
    
    # 9.3.8. Resultado nuevo promedio y desviación estándar de arreglos con datos normalizados
    
    array_a_2 = (norm_arreglo(array_a))
    array_b_2 = (norm_arreglo(array_b))
    
    print ("Nuevo promedio arreglo a normalizado:", mean_arreglo(array_a_2))
    print ("Nuevo promedio arreglo b normalizado:", mean_arreglo(array_b_2))
    
    print ("Nueva desv. estándar arreglo a normalizado:", std_arreglo(array_a_2))
    print ("Nueva desv. estándar arreglo b normalizado:", std_arreglo(array_b_2))

else:
    print("Ud quiere calcular menos de 5 potencias. FIN.")
