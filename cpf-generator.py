#código em Python para gerar um número de cpf válido

from random import randint #importando randint para gerar números randomicos e passa-los pela lógica de validação

cpf = str(randint(100000000, 999999999))
cpfValidator = cpf

#cálculo com os 8 primeiros números do cpf informado
total = 0
x = 10 
 
for i in range(9):
	total += int(cpfValidator[i]) * x
	x = x-1
	
digit1 = 11 - (total % 11)

if digit1 > 9:
	digit1 = 0

#calculo dos 8 primeiros números + novo dígito adicionado
cpfValidator += str(digit1)
total = 0
x = 11

for i in range(10):
	total += int(cpfValidator[i]) * x
	x = x-1

digit = 11 - (total % 11)

if digit > 9:
    digit2 = 0
else:
    digit2 = digit
    
cpfValidator += str(digit2)

print(cpfValidator)
