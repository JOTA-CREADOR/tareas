# ejercicios 01

# Solicitar al usuario dos palabras
word1 = input('Ingresa la primera palabra: ')
word2 = input('Ingresa la segunda palabra: ')

# Determinar cuál palabra va primero en orden alfabético
if word1 < word2:
    print(f'{word1} va primero en orden alfabético')
else:
    print(f'{word2} va primero en orden alfabético')

    
    # ejercicios 02

lado1 = float(input("Ingresa la longitud del primer lado:"))
lado2 = float(input("Ingresa la longitud del segundo lado:"))
lado3 = float(input("Ingresa la longitud del tercer lado:"))

if lado1 == lado2 == lado3:
    print("El triangulo es equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triangulo es isóseles")
else:
    print("El triangulo es escaleno")

# ejercicio 03

def calcular_promedio(notas):
    total = sum(notas)
    promedio = total / len(notas)
    return promedio

notas_str = input("Ingresa las notas separadas por espacios: ")
notas = list(map(float, notas_str.split()))

promedio = calcular_promedio(notas)

print("El promedio de las notas ingresadas es:", promedio)

#ejercicio 04

def operaciones_aritmeticas(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2 if num2 != 0 else "No es posible dividir por cero"
    return suma, resta, multiplicacion, division

# Pedir al usuario que ingrese los dos números
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Realizar las operaciones aritméticas
resultado_suma, resultado_resta, resultado_multiplicacion, resultado_division = operaciones_aritmeticas(num1, num2)

# Imprimir los resultados
print("Suma:", resultado_suma)
print("Resta:", resultado_resta)
print("Multiplicación:", resultado_multiplicacion)
print("División:", resultado_division)

# ejercicio 05
# Pedir al usuario que ingrese un número entero
numero = int(input("Ingresa un número entero: "))

# Determinar si el número es par o impar
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

 # ejercicio 06

 # Pedir al usuario que ingrese tres números
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

# Determinar cuál de los tres números es el mayor
if numero1 > numero2 and numero1 > numero3:
    mayor = numero1
elif numero2 > numero1 and numero2 > numero3:
    mayor = numero2
else:
    mayor = numero3

print(f"El número mayor de los tres ingresados es: {mayor}")

# ejercicio 07

usuario = float(input("precio orginal del producto:"))

Cdescuento = input("Ingresa la categoria descuento(estudiante, jubilado, empleado u otro): ")
if Cdescuento == "estudiante":
    descuento = 0.10
elif Cdescuento == "jubilado":
    descuento = 0.15
elif Cdescuento == "empleado":
    descuento = 0.05
else:
    descuento = 0

preciofin = usuario * (1 - descuento) 
print(f"El precio final del producto para la categoria {Cdescuento} es: {preciofin}")

# ejercicio 08

usuario = float(input("Ingresa un numero:"))
if usuario > 0:
    print("es positivo")
elif usuario < 0:
    print("es negativo")
else:
    print("es cero")

# ejercicio 09
usuario = int(input('Ingresa un año: '))

if (usuario % 4 == 0 and usuario % 100 != 0) or (usuario % 400 == 0):
    print(usuario, 'es un año bisiesto')
else:
    print(usuario, 'no es un año bisiesto')

# ejercicio 10
usuario = float(input("Ingresa longitud en metros:"))
conversion = input("Ingresa la unidad (pies, pulgadas o yardas):")
if conversion == "pies":
    longitudconvertida = usuario * 3.28084
    print(f"la longitud convertida es:{longitudconvertida} pies")
elif conversion == "pulgadas":
    longitudconvertida = usuario * 39.3701
    print(f"la longitud convertida es: {longitudconvertida} pulgadas")
elif conversion == "pulgadas":
    longitudconvertida = usuario * 1.09361
    print(f"la longitud convertida es: {longitudconvertida} yardas")
else:
    print(f"La unidad ingresada no es valida, ingrese pies, pulgadas o yardas")

# ejercicio 11
peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))
imc = peso / (altura ** 2)
if imc < 18.5:
    categoria = "Bajo peso"
elif 18.5 <= imc < 24.9:
    categoria = "Normal"
elif 25 <= imc < 29.9:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"
print(f"Tu IMC es: {imc:.2f}")
print(f"Categoría: {categoria}")


# ejercicio 12
usuario = int(input("nro del 1 al 7:"))
if usuario ==  1:
    print("lunes")
elif usuario == 2:
    print("martes")
elif usuario ==  3:
    print("miercoles")
elif usuario ==  4:
    print("jueves")
elif usuario ==  5:
    print("viernes")
elif usuario ==  6:
    print("sabado")
elif usuario ==  7:
    print("domingo")
else:
    print("el numero ingresado no esta en rango del 1 al 7.")

# ejercicio 13
usuario = int(input("Ingrese su edad:"))
if usuario > 18:
    print("es mayor de edad")
else:
    print("es menor de edad")

# ejercicio 14
import random
opciones = ["piedra", "papel", "tijera"]
usuario = input("Elige 'piedra', 'papel' o 'tijera': ").lower()
if usuario not in opciones:
    print("Opción no válida.")
else:
    computadora = random.choice(opciones)
    print(f"Elección de la computadora: {computadora}")
    if usuario == computadora:
        print("¡Es un empate!")
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")


# ejercicio 15
numero = input("Introduce un número de teléfono de 10 dígitos: ")
if len(numero) == 10 and numero.isdigit():
    formato = f"({numero[:3]}) {numero[3:6]}-{numero[6:]}"
    print("Número de teléfono con formato:", formato)
else:
    print("El número debe tener exactamente 10 dígitos.")

    
    



 


