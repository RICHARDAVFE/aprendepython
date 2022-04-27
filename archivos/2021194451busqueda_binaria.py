import random
def bubble_sort(lista):
    lista1=[]
    lista2=[]
    for i in range(len(lista)):
        if lista[i]>=50:
            lista1.append(lista[i])
        else:
            lista2.append(lista[i])
   
    for tope in range(len(lista1)-1, 0, -1):
        for i in range(tope):
            if lista1[i] > lista1[i+1] :
                temp = lista1[i]
                lista1[i] = lista1[i+1]
                lista1[i+1] = temp
    for tope in range(len(lista2)-1, 0, -1):
        for i in range(tope):
            if lista2[i] < lista2[i+1] :
                temp = lista2[i]
                lista2[i] = lista2[i+1]
                lista2[i+1] = temp
    print("RESPUESTA")
    print("1-50: ", ', '.join(str(i) for i in lista2))
    print("50-100: ",', '.join(str(i) for i in lista1))
lista1=[]
for i in range(10):
    x=random.randint(1,100)
    lista1.append(x)

print("NUMEROS GENERADOS")
print(", ".join(str(i) for i in lista1))
bubble_sort(lista1)
