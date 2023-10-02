import random

conjunto = set()
i = 0
x = 0

while i <= 1000:
    conjunto.add(i)
    # tenta inserir valores repetidos
    while x <= 1000:
        conjunto.add(x)
        #if conjunto.add(i) == False:
         #   print("Não consegui inserir o número repetido")
        x += 1
    i += 1

print(2 in conjunto)   # True
print(4 in conjunto)   # False

excluidos = []

while x <= 10:
    excluidos[x] = conjunto.remove(random.choice(conjunto))
    conjunto.remove(excluidos[x])
    x += 1

conjunto.remove(2)
print(2 in conjunto)    # False

print("O tamanho do conjunto ficou em: ",len(conjunto))   
print("E os seus valores sao: ", list(conjunto))  
