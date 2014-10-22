__author__ = 'Ja'

lista = [[1,2], [2,7], [5, 10], [9, 11]]
print(lista)
for x in lista:
    x[0] = 3
    print(x)

print(lista)
lista=[]

if not([3,2] in lista):
    print("no se encuentra")
else:
    print("si se encuentra")