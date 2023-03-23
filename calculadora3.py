valorPadrão = 1024

def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)



def mbyteParatbyte(valorASerConvertido):
    print('/8clear')
    tbytesCalculado = valorASerConvertido / valorPadrão
    return tbytesCalculado

def tbyteParambyte(valorASerConvertido):
    print('Valor convertido de byte para bit')
    mbytesCalculado = valorASerConvertido * valorPadrão
    return mbytesCalculado


print('Insira o valor a ser convertido')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = mbyteParatbyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)