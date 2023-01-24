# print('--------Cozinhar-------')
# Forno = int(input('Informe em °C a temperatura do forno que irá cozinhar o steak:  '))
# try:
#     if Forno <= 48:
#         print('Steak está selado')
#     elif Forno >= 54:
#         print('Ao ponto pra mal')
#     elif Forno >= 60:
#          print('ao ponto')
#     elif Forno >= 65:
#         print('ao ponto pra bem')
#     elif Forno >= 71:
#        print('bem passada')
# except:
#      print('Coloque um valor valido')
 
# print('-----Calculo de tinta-------')
# Rendimento = int(input('Informe o Rendimento da lata de tinta:  '))
# altura = float(input('Informe a altura da parede:  '))
# largura = float(input('Agora informe a largura de parede:  '))

# def calculo():
#     area = altura*largura     
#     resultado = area/Rendimento
#     print(f'Voce ira precisa de {resultado} latas de tintas')

# print(calculo())

# funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
# turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
# turno_noite = ['Pedro', 'Sophia', 'Bruno']
# tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

# lista1 = set(tem_carro).intersection(turno_noite)
# print(lista1)

# lista2 = set(tem_carro).intersection(turno_dia)
# print(lista2)

# lista3 = set(funcionarios).difference(tem_carro)
# print(lista3)

Numeros = (11)


while True:
    print('''aperte 11 para continuar ou qualquer outra tecla para sair...''')
    entrada = int(input('Quer sair ou continuar?  '))
    if entrada != Numeros:
        print('VOCE SAIU')
        break
    else:    
        Peso = float(input('Digite seu Peso: '))
        Altura = float(input('Digite sua altura: '))
        calculo = Peso/(Altura)**2 
    if calculo < 18.5:
        print(f'{calculo:.2f} = Magreza')
    elif calculo >= 18.5 and calculo == 24.9:
        print(f'{calculo:.2f} = Normal')
    elif calculo >= 25.0 and calculo == 29.9:
        print(f'{calculo:.2f} = sobrepeso')
    elif calculo >= 30.0 and calculo == 39.9:
        print(f'{calculo:.2f} = obesidade')
    elif calculo >= 40.0:
        print(f'{calculo:.2f} = obesidade grave')
        continue
        
    
