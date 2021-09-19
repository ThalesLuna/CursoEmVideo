print('Exercicio 10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares '
      'ela pode comprar.')
print()
print('Considere US$1.00 = R$3.27')
print()

n1 = float(input('Digite o valor que possui na carteira: R$ '))
print()

r = n1/3.27

print('É possível comprar US$ {:.2f}!'.format(r))

