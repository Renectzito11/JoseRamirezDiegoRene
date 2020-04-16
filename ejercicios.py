#!
numeros=input("Introducir numeros A,B: ")
x = numeros.split(" ")
suma=0
for i in x:
    suma+=int(i)
print("suma: ",suma)

#2
limite=int(input("Numero: "))
suma=0
for x in range (1,limite+1):
    suma+=x
print("suma:",suma)

#3
n=int(input("Numero: "))
print(1)
contador=2
aux=1
while contador!= n:
        if contador%2==0 or contador%3==0 or contador%5==0:
            print (contador)
        contador+=1
        


