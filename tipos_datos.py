#Para saber el tipo de dato de una variable debemos utilizar la funcion type()

entero = 20
flotante = 3.14
texto = "Hola mundo"
booleano = True #En cualquier caso puedes probar con "False" respetando las mayúsculas
print(type(entero))
print(type(flotante))
print(type(texto))
print(type(booleano))

# Formas de concatenar cadenas de texto / string (str)
print("El primer saludo de mi aprendizaje es: " + texto)
"""Cuando se utiliza "+" para concatenar 2 string debes dejar espaciado"""

print("El primer saludo de mi aprendizaje es:", texto)
"""Cuando se ultiliza "," para concatenar 2 string el espaciado se hace automatico"""

# Tipo de dato Numerico (Numeric)
"""Podemos almacenar multiples valores como: Numeros enteros (Integer), Numeros Flotantes (Float), Numeros Complejos (Complex Number)"""

numero1 = 10
numero2 = 20
print("Suma:", numero1 + numero2)
print("Resta:", numero1 - numero2)
print("Multiplicacion:", numero1 * numero2)
print("Divicion:", numero1 / numero2)

"""Si queremos concatenar 2 tipos de datos numericos deberiamos almacenarlo en una variable de tipo string"""
numero3 = "10"
numero4 = "20"
print(numero3 + numero4) # El "+" en la concatenacion no hace espaciado
print(numero3, numero4) # La "," en la concatenacion hace espaciado

"""Para convertir una variable de tipo texto a entero debemos usar la funcion int()"""
print("Suma:", int(numero3) + int(numero4))

# Tipo de dato Diccionario (Dictionary)


# Tipo de dato Booleano 0 y 1, True y False (Boolean)


# Tipo de dato Set


# Tipo de dato Secuencia (Sequence)
"""En tipos de datos de secuencia se pueden almacenar multiples valores como: Strings (Cadenas de texto), Listas (List) y Tuplas (Tuple) """