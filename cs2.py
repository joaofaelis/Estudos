
var1 = input('Digite um numero: ')
if var1.isdigit():
    var2 = int(var1)
    var3 = var2 % 2 == 0
    var4 = "ímpar"
    if var2:
        var4 = 'par'
    print(f'o numero {var1} é {var4}')
else:
    print('voce não digitou um numero inteiro.')
    ######################################################

hora1 = input('digite um horario em numeros inteiros:  ')
try:
    hora = int(hora1)
    if hora >= 0 and hora <= 11:
        print(f'{hora} então é BOM DIA !')

    elif hora >= 12 and hora <= 17:
        print(f'{hora} então é BOA TARDE')

    elif hora >= 18 and hora <= 23:
        print(f'{hora} então é BOA NOITE')

    else:
        print('não conheco essa hora.')
    
except:
    print('Por favor, digite apenas numeros inteiros.')
    ##########################################################

nome = input('Digite seu nome: ')
nome1 = len(nome)
if nome1 <= 4:
        print('seu nome é curto, tente novamente')
elif nome1 > 6:
    print('seu nome é muito grande, tente novamente')
else:
    print('seu nome é ideal')
###########################################################################3