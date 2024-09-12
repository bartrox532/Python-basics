#------------------------Operadores Logicos------------------------


#------------------------AND------------------------
#Solo nos devulve true si las 2 son true
#Si una condicion NO se cumple siempre es false

Resultado =  True  & True   #Deveoloper True
Resultado2 = False & True   #Deveoloper False
Resultado3 = True  & False  #Deveoloper False
Resultado4 = False & False  #Deveoloper False

#------------------------OR------------------------
#Solo nos devulve falso si las 2 son falso
#Si una condicion se cumple siempre es true


Resultado5 = True  | True   #Deveoloper True
Resultado6 = False | True   #Deveoloper True
Resultado7 = True  | False  #Deveoloper True
Resultado8 = False | False  #Deveoloper False

#------------------------NOT------------------------
#Si le damos un valor true lo hace false
#Si le damos un valor false lo hace true

Resultado9  = not True #Deveoloper Falso
Resultado10 = not False #Deveoloper True

print(Resultado10)