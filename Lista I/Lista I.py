#1) Faça um programa que peça dois números inteiros 
#e imprima a soma desses dois números

print('#Exercício 1')
N1 = int(input('Numero 1: '))
N2 = int(input('Numero 2: '))
print (N1+N2)

#2) Escreva um programa que leia um valor em metros 
#e o exiba convertido em milímetros

print('#Exercício 2')
N = int(input('Valor: '))
print(N*1000)

#3) Escreva um programa que leia a quantidade de dias, 
#horas, minutos e segundos do usuário. Calcule
#o total em segundos.

print('#Exercício 3')
D = int(input('Dias:'))
H = int(input('Horas:'))
M = int(input('Minutos:'))
S = int(input('Segundos:'))
TD=D*60*60*24
TH=H*60*60
TM=M*60
TOTAL = TD+TH+TM+S
print(TOTAL)

#4) Faça um programa que calcule o aumento de um salário. 
#Ele deve solicitar o valor do salário e a
#porcentagem do aumento. Exiba o valor do aumento e do novo salário.

print('#Exercício 4')
S = int(input('Salário:'))
P = int(input('Aumento %:'))
A = S/100*P
NS = S+A
print(f'O Aumento é R$ {A:.2f}')
print(f'O Novo Salário é R$ {NS:.2f}')

#5) Solicite o preço de uma mercadoria e o percentual 
#de desconto. Exiba o valor do desconto e o preço a pagar.


print('#Exercício 5')
P = int(input('Preço:'))
D = int(input('Desconto %:'))
V = P/100*D
NP = P-V
print(f'O Desconto é R$ {V:.2f}')
print(f'O Novo Preço é R$ {NP:.2f}')

#6) Calcule o tempo de uma viagem de carro. Pergunte a distância 
#a percorrer e a velocidade média esperada para a viagem.

print('#Exercício 6')
D = int(input('Distância km:'))
V = int(input('Velocidade média km/h:'))
T = int(D/V)
print('Tempo H:',T)

#7) Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32

print('#Exercício 7')
C = float(input('Celsius:'))
F = 9*C/5 + 32
print('Fahrenheit:',F)

#8) Faça agora o contrário, de Fahrenheit para Celsius.

print('#Exercício 8')
F = float(input('Fahrenheit:'))
C = (F-32)*5/9
print('Celsius:',C)

#9) Escreva um programa que pergunte a quantidade de km percorridos 
#por um carro alugado pelo usuário, assim como a quantidade de dias 
#pelos quais o carro foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

print('#Exercício 9')
KM = int(input('KM:'))
D = int(input('Dias alugados:'))
P = KM*0.15+D*60
print(f'Preço a pagar R${P:.2f}')

#10) Escreva um programa para calcular a redução do tempo de vida de 
#um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos 
#anos ele já fumou. Considere que um fumante perde 10 minutos de vida a 
#cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
#total de dias.

print('#Exercício 10')
C = int(input('Cigarros fumados por dia: '))
A = int(input('Anos: '))*365
CT = C*A
T = int(CT*10/1440)
print('Dias de vida perdidos:',T)

#11) Sabendo que str( ) converte valores numéricos para string, calcule 
#quantos dígitos há em 2 elevado a um milhão.

print('#Exercício 11')
D = str(2**1000000)
print ('Numero de Digitos: ', len(D))
