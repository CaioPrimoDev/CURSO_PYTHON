"""
nome = "Caio"
sobrenome_1 = "Nunes "
sobrenome_2 = "Primo"



print(nome, end=" ")
print(sobrenome_1)
print(sobrenome_2)

print(nome, end=" " + sobrenome_1 + sobrenome_2 + "\n > Teste Finalizado\n")
print(nome, sobrenome_1, sobrenome_2, "\n > Teste Finalizado")

print("Profissão: \"Estudante\" ")
"""

nome = input("Qual é o seu nome?\n> ")
print(":", nome)

idade = input("Qual a sua idade?\n> ")
# "input" vai receber os valores do teclado, e registrar como String, ou seja, não é possível fazer cálculos
print(":", idade)

idade = int(idade)
print("Sua idade(- 1) é: %d" % (idade - 1))

num_1 = 11
num_2 = 5
num_3 = "1"

print("Soma: ", num_1 + num_2, num_3)

print("Soma: ", num_1 + num_2)
print("Subtração: ", num_1 - num_2)
print("Multiplicação: ", num_1 * num_2)

# a diferença entra " \ " e " \\ " é que a barra dupla asignifica divisão inteiro, ou seja, o programa só retorna um valor inteiro

print("Divisão Inteira: ", num_1 // num_2)
print("Divisão: ", num_1 / num_2)
print("Potência(9 ao quadrado): ", 9 ** 2)