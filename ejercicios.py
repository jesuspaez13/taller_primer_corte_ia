# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 15:59:28 2021

@author: USER
"""
# Ejercicio 1
#  y = ( (5+2-5)^2 * 5+8/2 -30 ) / 2 * 5 -3
parentesis = 5 + 2 - 5
parentesis_al_cuadrado = parentesis ** 2
division = 8 / 2
operacion = 5 + division - 30
parentesis_total = parentesis_al_cuadrado * operacion
dos_por_cinco_menos_tres = 2 * 5 - 3
division_total = parentesis_total / dos_por_cinco_menos_tres
print(f'El resultado de la operacion es: {division_total}')

# Ejercicio 2
# z=5
# n=3
# m= z-n
# y = (( (z+2-n)^2 * m+8/2 -30 ) / 2 * 5 -3)^ 5 + 15 * 3 - 9/3
z = 5
n = 3
m = z - n
parentesis_pequeño = z + 2 - n
potencia = parentesis_pequeño ** 2
ol = m + 8 / 2 - 30
parentesis_mediano = potencia * ol
old = 2 * 5 - 3
parentesis_grande = parentesis_mediano / old
potencia_grande = parentesis_grande ** 5
os = (15 * 3) - (9 / 3)
total = potencia_grande + os
print(f'El resultado de la operacion es: {total}')

# Ejercicio 3
# z=5
# n=( (8+2-4)^2 * 5+8+7/2 -30*5 ) / 2 * 5 -3
# m= z^2*3+n
# y = ((( (z+2-n)^2 x m+8/2 -30 ) / 2 * 5 -3)^ 5 + 15 * 3 - 9/3) ^ 2 – 5/4
z = 5
n = (((8 + 2 - 4) ** 2) * (5 + 8 + 7 / 2 - 30 * 5)) / 2 * 5 - 3
m = (z ** 2) * 3 + n
sy = (((z + 2 - n) ** 2) * (m + 8 / 2 - 30))
op = ((sy / (2 * 5 - 3)) ** 5)
suma = op + (15 * 3 - 9 / 3)
suma_al_cuadrado = suma ** 2
total = suma_al_cuadrado - (5 / 4)
print(f'El resultado de la operacion es: {total}')

# Problema 1
presion = float(input('Digite la presion: '))
volumen = float(input('Digite el volumen: '))
temperatura = float(input('Digite la temperatura: '))
m = presion * volumen
s = temperatura + 460
mu = 0.37 * s
d = m / mu
print(f'La masa es igual a: {d}')

# Problema 2
edad = float(input('Digite la edad: '))
r = 200 - edad
d = r / 10
print(f'El numeo de pulsaciones que esta persona debe tener es de: {d}')




















