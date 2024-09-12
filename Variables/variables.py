#------------------------Variables como Numeros------------------------

a = 1
b = 2
c = 3
d = a + b + c
print (d)

#------------------------Suma y Resta de variables con el mismo nombre +1, -1------------------------

numero = 10
numero += 10
numero += 10
numero -= 5
print(numero)

#------------------------Variables de Texto------------------------

nombre = "Ale"
apellido = "mendez"
edad = "20"
print (nombre)


#------------------------Concatenar variables de texto------------------------

nombre = "Ale"
apellido = "mendez"
edad = "20"
datos = "Sus Datos son: " "Nombre: "+ nombre + " " + "Apellido: " + apellido + " " + "Edad: " + " " + edad
print (datos)

#------------------------#Concatenar variables de numeros y texto------------------------
#El "f string, convierte cualquier tipo de dato a texto"
#Con "del" eliminamos una variable, si se coloca ael nombre de la variable -
#- despues de que se cambia en la variable "datos" no lo elimina porque ya -
#diferente y no tiene que borrar.

nombre = "Ale"
edad = 20
datos = f"Hola {nombre, edad} Que tal?"
del nombre
print (datos)


#------------------------Operadores de pertenencia------------------------
# (in / not in)
#Imprimir una variable con un pedazo del texto de otra variable
#Encontrar "ola" dentro de la variable "datos"

nombre = "Ale"
datos = f"Hola {nombre} Que tal?" #true
print ("Hola" in datos)

nombre = "Ale"
datos = f"Hola {nombre} Que tal?" #false
print ("Hola" not in datos)

