#------------------------Condicionales (if / else / elif)------------------------
#if anidados y else if (elif)

ingreso_mensual = 72000
gasto_mensual = 800000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print('estas en deficit')
    elif ingreso_mensual - gasto_mensual > 3000:
        print('Vivis bien en cualquier parte del mundo')
    else:
        print('estas gastanto mucho')
    
elif ingreso_mensual > 1000:
    print('Estas bien en LATAM')
    
elif ingreso_mensual > 500:
    print('Estas bien en Argentina')
    
elif ingreso_mensual > 200:
    print('Estas bien en Venezuela')
    
else:
    print('Sos pobre')