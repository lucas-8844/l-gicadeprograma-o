from functools import reduce


numeros = [-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8,9,10,15]
sucessor = list(map(lambda x: x+1,numeros)) #sucessor
antecessor = list(map(lambda x: x-1,numeros)) #antecessor
quintuplo = list(map(lambda x: x*5 +1,numeros)) #sucessor do quintuplo de cada numero
pares = list(filter(lambda x: x % 2 ==0 ,numeros))
positivos = list(filter(lambda x: x > 0 ,numeros))
impares = list(filter(lambda x: x%2 != 0, numeros))
negativos = list(filter(lambda x: x < 0 ,numeros))
multiplos_3_5 = list(filter(lambda x: x%3==0 and x%5==0,numeros)) 
total = reduce(lambda acumulador,n: acumulador + n ,numeros,0)
print(sucessor)
print(antecessor)
print(quintuplo)
print(pares)
print(positivos)
print(impares)
print(negativos)
print(multiplos_3_5)
print(total)