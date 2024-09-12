#------------------------Crear una lista / tupla ------------------------
#Posiciones [0,1,2,3,4,5,6,7,8,9]
#Posicion 0 = Aljandro, 1= Mendez, 2 = True, 3 = 1.70
#Lo que esta entre "[]" es el dato que se va a mostrar

lista = ["Alejandro", "Mendez", True, 1.72]
print(lista[0])

#tupla y print hacen lo mismo, con la diferencia de que la lista se puede -
# - modificar en otras variables o procesos y la tupla no se puede modificar
#tupla se usa con "()" no con "[]"

tupla = ("Alejandro", "Mendez", True, 1.72)
print(tupla[1])

#------------------------ Crear un conjunto (set)------------------------
#En el conjunto no se puede acceder por el indice
#El conjunto no pueden haber datos duplicados
#Son datos desordenados
conjunto = {"Alejandro", "Mendez", True, 1.72}
print(conjunto)

#------------------------ Crear un diccionario (dic)------------------------
# por defecto se ordena asi:
# 0: "Marco",
# 1: "Rojas",
# 2:  True,
# 3:  1.70,
# los numeros serian las "claves" y los datos los "valores"
# 'key': "value", 
# 'nombre: "Marco",
diccionario = {
    'nombre'    :      "Marco",
    'apellido'  :      "Rojas", 
    'estado'    :       True, 
    'altura'    :       1.72, 
    'altura'    :       1.72 
}

print(diccionario['altura'])
# +10 a la altura de la lista seria:
# print(diccionario['altura']+ 10)
print(lista[3])

