
# estructura for: 
# imprimir un triangulo de asteriscos de la sig forma puede ser de n filas(a criterio):

longitud = int(input("longitud del triangulo de asteriscos: "))

for i in range (1,longitud+1):
    print("*"*i)


# 2: invertida
longitud = int(input("2.- longitud del triangulo de asteriscos: "))
arreglo=[]
for i in range (longitud,1-1,-1):
    print("*"*i)

# 3: creciente y descrece

longitud = int(input("3.- longitud del triangulo de asteriscos: "))

for i in range (1,longitud+1):
    print("*"*i)

for i in range (longitud+1,1-1,-1):
    print("*"*i)

# 4: cuadrado
longitud = int(input("4.- longitud del triangulo de asteriscos: "))

for i in range (1,longitud+1):
    print("*"*longitud)