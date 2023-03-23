valorPadrão = 1024

def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)



def tbyteParapbyte(valorASerConvertido):
    print('/8clear')
    tbytesCalculado = valorASerConvertido / valorPadrão
    return tbytesCalculado

def pbyteParaybyte(valorASerConvertido):
    print('Valor convertido de byte para bit')
    pbytesCalculado = valorASerConvertido * valorPadrão
    return pbytesCalculado


print('Insira o valor a ser convertido')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = tbyteParapbyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)