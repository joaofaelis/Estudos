"""Teste de desenvolvimento"""
  # Calculadora de consumo de aguá.

main = float(input('Informe seu peso: '))
fisic = float(input('Agora informe sua altura: '))

def imc():
        calculo = main / (fisic * fisic)
        result = calculo
        print(f'{result:.2f}')
imc()

def water():
        ml = 0.35
        peso = main*ml
        # conversao = peso/100
        print(f'{peso:.1f}')

print(f' acordo com seu IMC voce precisa tomar diariamente:{water()}')
