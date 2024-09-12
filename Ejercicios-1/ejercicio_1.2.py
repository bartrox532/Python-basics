
#Le pedimos al usuario que nos de una frase
frase = frase = input("Dime una frase y te calculo cuanto tardarias si tuvieras que decirla: ")

#Creamos una lista con todas las palabras de la frase(se separan cada vez que haya un espacio en blanco)
palabras_separadas = frase.split(" ")

#Usamo len() para ver la cantidad de elementos en la lista
cantidad_de_palabras = len(palabras_separadas)

#En caso de que tarde mas de 1 minuto en decielo, le decimos que pare un poco
if cantidad_de_palabras > 120:
    print("Mucho texto pa")

#Calculamos cuanto tardaria en decir las palabras y se lo decimos
print(f"Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo")
print(f"Dalto lo diria en {cantidad_de_palabras * 100 // 2 / 1.3 // 100} segundos")

