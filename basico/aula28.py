#testes com tulples
#tuplas nao podem ser modificadas

#Teste 1: Qual é o tipo?
a = (1, 2, 3)
b = [4, 5, 6]

print(type(a))  # ?
print(type(b))  # ?

#Teste 2: Mutabilidade
lista = [10, 20, 30]
tupla = (10, 20, 30)

lista[0] = 99
tupla[0] = 99  # O que acontece aqui?

#Teste 3: Append
lista = [1, 2, 3]
tupla = (1, 2, 3)

lista.append(4)
tupla.append(4)  # Isso funciona?

#Teste 4: Fatiamento
t = (10, 20, 30, 40, 50)
print(t[1:4])  # O que será impresso?
