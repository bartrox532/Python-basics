#------------------------Metodos (cadenas)------------------------
#Los metodos se trabajan seguidos de alguna otra cosa.
#Todos los metodos son funciones pero no todas las funciones son metodos
#Para que sea un metodo tiene que tener una funcion especifica de un objetos
#------------------------DIR(funcion)------------------------
#Devuelve la lista de atributos validos del objeto pasado

cadena1 = 'Hola soy Ale'
cadena2 = 'Bienvenido pa'

resultado = dir(cadena1)

#print(resultado)

#------------------------UPPER------------------------
#Convierte el texto a MAYUSCULA
#estructura:
# dato.metodo()
cadena1 = 'Hola soy Ale'
cadena2 = 'Bienvenido pa'

mayusc = cadena2.upper()


#------------------------LOWER------------------------
#Convierte el texto a minuscula
#estructura:
# dato.metodo()
cadena1 = 'Hola soy Ale'
cadena2 = 'Bienvenido pa'

minusc = cadena2.lower()


#------------------------CAPITALIZE------------------------
#Convierte la primer letra en mayuscua
#estructura:
# dato.metodo()
cadena1 = 'hola soy Ale'
cadena2 = 'bienvenido pa'

capitalize = cadena2.capitalize()


#------------------------FIND------------------------
#Buscamos una cadena en otra cadena, si no encuentra nada retorna "-1"
#estructura:
# dato.metodo()
cadena1 = 'hola soy Ale'
cadena2 = 'bienvenido pa'

busqueda_find = cadena1.find('s')

print(busqueda_find)

#------------------------INDEX------------------------
#Buscamos una cadena en otra cadena, si no encuentra nada retorna una excepcion

cadena1 = 'Hola soy Ale'
cadena2 = 'Bienvenido pa'

busqueda_index = cadena1.index('A')

print(busqueda_index)

#------------------------ISNUMERIC------------------------
#Si es numerico (detecta algun numero) deveuelve "true", sino devuelve "false"

cadena13 = '123456789'
cadena2  = 'Bienvenido pa'

es_numerico = cadena13.isnumeric()

print(es_numerico)


#------------------------ISALPHA------------------------
#Si es alfanumerico (solo letras  sin espacios ni caracteres especiales) 
#deveuelve "true", sino devuelve "false"

cadena14 = 'helloman'
cadena2  = 'Bienvenido pa'

es_alfnumerico = cadena14.isalpha()

print(es_alfnumerico)


#------------------------COUNT------------------------
#Buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincida
#Devuelve el numero de ocurrencias de una subcadena en la cadena dada
#Si no encuentra nada retorna 0

cadena15 = 'hellomaaaaan'
cadena2  = 'Bienvenido pa'

contar_coincidencias = cadena15.count("a")

print(contar_coincidencias)
#------------------------LEN(Funcion)------------------------
#Cuenta los coincidencias de una cadena dentro de otra casde
#Devulve la cantidad de coincidencias

cadena15 = 'Hi'
cadena2  = 'Bienvenido pa'

contar_caracteres = len(cadena15)

print(contar_caracteres)

#------------------------STARTSWITH------------------------
#Verifica si una cadena comienza con otra cadena dada, si es asi devuelve true

cadena16 = 'helloman'
cadena2  = 'Bienvenido pa'

empieza_con = cadena16.startswith("he")

print(empieza_con)

#------------------------ENDSWITH------------------------
#Verifica si una cadena termina con otra cadena, si es asi devuelve true

cadena17 = 'helloman'
cadena2  = 'Bienvenido pa'

termina_con = cadena17.endswith("pa")

print(termina_con)

#------------------------REPLACE------------------------
#Si el valor 1, se encuentra en al cadena original, remplaza el valor - 
# - 1 de la misma por el valor de 2

cadena18 = 'helloman'
cadena2  = 'Bienvenido pa'

cadena_nueva = cadena18.replace("man", "girl")

print(cadena_nueva)

#------------------------SPLIT------------------------
#Separa cadenas con la cadena que le pasemos

cadena19 = 'Hola,Maquina,como,estas'
cadena2  = 'Bienvenido pa'

cadena_separada = cadena19.split(",")

print(cadena_separada[0])