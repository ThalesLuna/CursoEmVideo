#definição da função soma

def soma (a, b):
    r = a + b
    return r

    """
    Retorna a soma de dois números
    
    Parâmetros
    ---------
    a,b,c int ou float
    Números a serem somados
    
    Retorno
    ----------
    int ou float
    Resultado da soma
    
    """
#-------------------------
#deinição da função média
def media(a, b, c):
    r = (a+b+c)/3
    return r

#-------------------------
#definição da função entrada de dados
def entrada_dados():
    n = int(input('Número: '))
    return n

#---------------------------
#definição da função par ou impar
def par_ou_impar(x, y, z):
    if(x %2 == 0):
        print('x é par')
    else:
        print('x é impar')

    if(y %2 == 0):
        print('y é par')
    else:
        print('y é impar')

    if(z %2 == 0):
        print('z é par')
    else:
        print('z é impar')

#--------------------------
#Programa principal
#Executa a função entrada de dados

#entrada de dados
x = entrada_dados()
y = entrada_dados()
z = entrada_dados()

#processamento
r_media = media(x, y, z)
r_soma = soma(x,y)

#saida de dados
print('Média: ', r_media)
print('Soma: ',r_soma)
par_ou_impar(x,y,z)

help(soma)









