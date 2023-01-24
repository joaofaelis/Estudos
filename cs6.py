import os


List = []
while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        list.append(valor)



    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')
        try:
                indice = int(indice_str)
                del list[indice]
        except ValueError:
            print('Não foi possivel achar esse indice.')
        except IndexError:
            print('Indice não existe na lista')
        except Exception:
            print('Erro desconhecido')

        
    elif opcao == 'l':
        os.system('clear')

        if len(list) == 0:
            print('Nada para listar')
        for i, valor in enumerate(list):
            print(i, valor)



    else:
        print('Escolha uma opção: "i", "a" ou "l" por favor.')