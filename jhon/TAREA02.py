# ejercicio 01
texto = "python"
longitud = len(texto)
longitud_float = float(longitud)
longitud_str = str(longitud_float)
print(f"Texto original: '{texto}'")
print(f"Longitud del texto: {longitud}")
print(f"Longitud como float: {longitud_float}")
print(f"Longitud como string: '{longitud_str}'")
 
# ejercicio 02
numero = int(input("Introduce un número: "))
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

# ejercicio 03

division_entera = 7 // 3           # la division entera es igual al valor convertido.
valor_convertido = int(2.7)
print("es:",division_entera)
print("la conversion es:",valor_convertido)

# ejercicio 04
cadena = '10'
numero = 10
tipo_cadena = type(cadena)
tipo_numero = type(numero)
# Comparar los tipos
if tipo_cadena == tipo_numero:
    print("El tipo de '10' es igual al tipo de 10.")
else:
    print("El tipo de '10' no es igual al tipo de 10.")

# ejercicio 05
# Convertir '9.8' a float primero y luego a int
valor_float = float('9.8')
valor_convertido = int(valor_float)
if valor_convertido == 10:
    print(f"int('9.8') es igual a 10.")
else:
    print(f"int('9.8') no es igual a 10. El valor convertido es {valor_convertido}.")

# ejercicio 06
usuario = float(input("Introduce las horas trabajadas: "))
tarifa_por_hora = float(input("Introduce la tarifa por hora: "))
salario_semanal = usuario * tarifa_por_hora
print(f"Tu salario semanal es {salario_semanal:.2f}")

# ejercicio 07
usuario = int(input("ingresa el nro de años:"))
# Definir el número promedio de segundos en un año 
# 1 año = 365 días
# 1 día = 24 horas
# 1 hora = 60 minutos
# 1 minuto = 60 segundos
segundos_por_año = 365 * 24 * 60 * 60
segundos_vividos = usuario * segundos_por_año
print(f"Has vivido durante {segundos_vividos} segundos.")

# ejercicio 08
n = 5
for i in range(1, n + 2):
    # Crear una lista para almacenar los valores de la fila actual
    fila = []
    for j in range(n - 1):
        # Calcular el valor como i elevado a la potencia de j
        valor = i ** j
        fila.append(valor)
    # Unir los valores de la fila con un espacio y mostrarlos
    print(' '.join(map(str, fila)))


# ejercicio 09
cadena = input("Introduce una cadena: ")
# slicing
cadena_invertida = cadena[::-1]
print("La cadena invertida es:", cadena_invertida)

# ejercicio 10
cadena = input("Introduce una cadena: ")
vocales = "aeiouAEIOU"
contador_vocales = 0
for caracter in cadena:
    if caracter in vocales:
        contador_vocales += 1
print(f"El número de vocales en la cadena es: {contador_vocales}")

# ejercicio 11
cadena = input("Introduce una cadena:")
cadena_limpia = ''.join(cadena.split()).lower()

# Invertir la cadena limpia
cadena_invertida = cadena_limpia[::-1]

# Verificar si la cadena limpia es igual a la cadena invertida
if cadena_limpia == cadena_invertida:
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")

# ejercicio 12
cadena = input("Introduce una cadena: ")             
cadena_modificada = cadena.replace(' ', '_')         # Reemplazar los espacios con guiones bajos
print("La cadena modificada es:", cadena_modificada)

# ejercicio 13
cadena = input("Introduce una cadena: ")
palabras = cadena.split()
numero_de_palabras = len(palabras)
print(f"El número de palabras en la cadena es: {numero_de_palabras}")

# ejercicio 14
usuario = input("Ingrese una cadena: ")
uppercase_string = usuario.upper()            # mayúsculas
print("En mayúsculas:", uppercase_string)
lowercase_string = usuario.lower()            # minúsculas
print("En minúsculas:", lowercase_string)

# ejercicio 15
usuario = input("Introduce una cadena: ")
cadena_sin_espacios = usuario.strip()
print("La cadena sin espacios al principio y al final es:", cadena_sin_espacios)

# ejercicio 16
usuario = input("Ingrese una cadena: ")
indice_ini = int(input("Ingrese el índice de inicio: "))
indice_fin = int(input("Ingrese el índice de fin: "))
subcadena = usuario[indice_ini:indice_fin]            # Extraer la subcadena
print("La subcadena extraída es:", subcadena)

# ejercicio 17
cadena = input("Introduce una cadena: ")
prefijo = input("Introduce el prefijo a verificar: ")
sufijo = input("Introduce el sufijo a verificar: ")
comienza_con_prefijo = cadena.startswith(prefijo)
termina_con_sufijo = cadena.endswith(sufijo)
if comienza_con_prefijo and termina_con_sufijo:
    print(f"La cadena '{cadena}' comienza con '{prefijo}' y termina con '{sufijo}'.")
else:
    if not comienza_con_prefijo:
        print(f"La cadena '{cadena}' no comienza con '{prefijo}'.")
    if not termina_con_sufijo:
        print(f"La cadena '{cadena}' no termina con '{sufijo}'.")













