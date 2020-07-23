#codigo em Pyhton para verificar se um cpf é válido ou não.

cpf = input("Informe seu CPF (apenas números) : ")
cpfValidator = cpf[:-2]

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

#evitando sequencias
sequence = cpfValidator == str(cpfValidator[0]) * len(cpf)

if cpf == cpfValidator and not sequence:
	print('CPF válido')
else:
	print('CPF inválido')

