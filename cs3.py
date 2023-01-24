
Name = 'Faelis'
indice = 0
new_name = ''

while indice < len(Name):
    letra = Name[indice]
    new_name += f'*{letra}'
    indice += 1
print(new_name)

###############################################



while True:  # laço de repetição quando as infos forem true.
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
    try:  #  o try irá tentar executar as variaveis, caso não consiga irá pular para o except.
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são invalidos.')
        continue

    operados_permitidos = '+=/*'

    if operador not in operados_permitidos:
        print('Operador Inválido.')
        continue


    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando a sua conta, confira abaixo: ')


    if operador == '+':
        print(f'{num_1_float} + {num_2_float} =', num_1_float + num_2_float)
    
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} =', num_1_float - num_2_float)

    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} =', num_1_float / num_2_float)

    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} =', num_1_float * num_2_float)

    else:
        print('Nunca Deveria Chegar aqui.')
    



    sair = input('Quer sair? [s]im ou [n]ão: ').lower().startswith('s')



    if sair is True:
        break 


