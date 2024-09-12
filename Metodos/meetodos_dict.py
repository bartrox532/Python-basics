#------------------------Diccionarios------------------------

#------------------------Keys------------------------
#Devuelve las claves (tambien nos sirve para iterar)
#Obteniendo un elemento con get() (si no encuentra nada el programa continua)
#Nos devueleve un objeto dict_item

diccionario = {
    "nombre"   : 'Ale',
    "apellido" : 'Mendez',
    "edad"     :  20 
}

claves = diccionario.keys()
print(claves)

#------------------------Get------------------------
#Devuelve el valor de una clave
valor_de_lolapopo = diccionario.get("lolapopo")

print(claves)

#------------------------Clear------------------------
#Eliminando todo del diccionario

#diccionario.clearclear()
#print(claves)

#------------------------POP------------------------
#Eliminando un elemento del diccionario

diccionario.pop("edad")
print(diccionario)

#------------------------Items------------------------
#Obteniendoon elemento dict_items iterable
#Iterable es recorrer el elemento

diccionario_iterable = diccionario.items()
print(diccionario_iterable)
