# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13MN6qOv308WqPmX9PBlBDcHx1ZvGz3qa
"""

numeros = input("Por favor ingrese 3 numeros." )
maximo = max(1500)
print ("maximo = " + str(maximo))

import random
import matplotlib.pyplot as plt
import numpy as np

def piedra_papel_tijera():
    opciones = ['piedra', 'papel', 'tijera']
    while True:
        jugador = input("Elige piedra, papel o tijera: ").lower()
        if jugador not in opciones:
            print("Opción no válida, por favor elige piedra, papel o tijera.")
            continue
        computadora = random.choice(opciones)
        print(f"Computadora eligió {computadora}.")
        if jugador == computadora:
            print("Empate.")
        elif jugador == 'piedra' and computadora == 'tijera' or \
            jugador == 'papel' and computadora == 'piedra' or \
            jugador == 'tijera' and computadora == 'papel':
            print("¡Ganaste!")
        else:
            print("Perdiste.")
        break


def adivinar_numero():
    intentos = 0
    numero = random.randint(1, 100)
    while intentos < 7:
        adivinanza = int(input("Adivina el número (entre 1 y 100): "))
        intentos += 1
        if adivinanza < numero:
            print("El número es mayor.")
        elif adivinanza > numero:
            print("El número es menor.")
        else:
            print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
            break

    else:
        print(f"No adivinaste el número. El número era {numero}.")



def tirar_dado():
    print(f"El número del dado es: {random.randint(1, 6)}.")

def graficar_funcion():
    x = np.linspace(-10, 10, 100)
    y = eval(input("Introduce una función matemática de 'x': "))
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfica de función')
    plt.show()

while True:
    opcion = input("Elige una opción: \n1. Jugar a piedra, papel, tijera \n2. Adivinar un número \n3. Tirar un dado \n4. Graficar una función matemática \n5. Salir \n")
    if opcion == '1':
        piedra_papel_tijera()
    elif opcion == '2':
        adivinar_numero()
    elif opcion == '3':
        tirar_dado()
    elif opcion == '4':
        graficar_funcion()
    elif opcion == '5':
        break
    else:
        print("Opción no válida, por favor elige una opción del 1 al 5.")