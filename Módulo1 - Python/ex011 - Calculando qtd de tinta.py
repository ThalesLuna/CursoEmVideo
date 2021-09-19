print('Exercicio 11 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessário para pintá-lo, sabendo que cada litro de tinta pinta uma área de 2m².')
print()

larg = float(input('Digita a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
print()

area = larg*alt

tinta = area/2

print('É necessário {} litros de tinta para pintar a parede'.format(tinta))

