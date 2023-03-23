valorPadrão = 1024

def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)



def mbyteParagbyte(valorASerConvertido):
    print('/8clear')
    mbytesCalculado = valorASerConvertido / valorPadrão
    return mbytesCalculado

def gbyteParambyte(valorASerConvertido):
    print('Valor convertido de byte para bit')
    gbytesCalculado = valorASerConvertido * valorPadrão
    return gbytesCalculado


print('Insira o valor a ser convertido')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = mbyteParagbyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)