#------------------------Metodos(Listas)------------------------


#------------------------LIST(Funcion)------------------------
#Crea una lista

lista = list([12, 2, 532, False, True, "Toma MAMA"])
print(lista)

#------------------------LEN------------------------
#Devuelve la cantidad de elementos de la lista
cadena = 'hola'
cantidad_elementos = len(lista)
print(cantidad_elementos)

#------------------------APPEND------------------------
#agregando un elemento a la lista

lista.append(128)
print(lista)

#------------------------IINSERT------------------------
#Agregando un elemento a la lista con un indeice especifico

lista.insert(2, 7213)
print(lista)

#------------------------EXTEND------------------------
#Agregando varios elementos a la lista

lista.extend([False, 2030])
print(lista)

#------------------------POP------------------------
#Eliminando un elemento de la lista (por su indice)

lista.pop(-1) # -1 para elmininar el ultimo elemento, -2 para el antepenultimo
print(lista)

#------------------------REMOVE------------------------
# Removiendo un elemento de la lista por su valor
#Si falla, envia una excepcion

lista.remove("Toma MAMA")
print(lista)

#------------------------CLEAR------------------------
#Eliminando todos los elementos de la lista

lista.clear()

#------------------------SORT------------------------
# Ordena la lista:
#Primero el False, despues los numero de menor a mayor
#Con el parametro "reverse=True" ordenamos la lista a la inversa -
# - es decir los numeros de mayor a menor y  de ultimo el False
lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

#------------------------REVERSE------------------------
#Invierte los elementos de la lista

lista.reverse()
print(lista)

#------------------------Buscar elementos de una lista------------------------

elemento_encontrado = lista.index(128)
print(elemento_encontrado)



