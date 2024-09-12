#------------------------Suma y Resta (+ y -)------------------------

suma  = 12 + 8
resta = 20 - 12

print(suma)
print(resta)

#------------------------Multi y Division (* y /)------------------------
#la division nos devuelve un dato float (flotante)

multi = 2 * 5
divi  = 10 / 2 

print(multi)
print(divi)

#------------------------Potenciacion (exponente) (**)------------------------

exponente = 2 ** 5

print(exponente)

#------------------------Division baja (//)------------------------
# si la division tiene algun punto "2.1" lo que esta despues de la coma lo borra
division_baja = 20//2

print(division_baja)

#------------------------DResto o Modulo (%)------------------------
# si la division tiene algun punto "2.1" lo que esta despues de la coma lo muestra
#type() nos devuelve que tipo de dato es
resto = 12 % 5
tipo_de_dato = type(5) #int
tipo_de_dato = type("Hola") #string
tipo_de_dato = type(["hola", 22, 24]) #lista
tipo_de_dato = type(("hola", 22, 24)) #tupla
print(resto)