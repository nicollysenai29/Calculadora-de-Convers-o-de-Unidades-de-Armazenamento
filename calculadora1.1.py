valorPadrão = 1024

def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)



def pbyteParatbyte(valorASerConvertido):
    print('/8clear')
    pbytesCalculado = valorASerConvertido / valorPadrão
    return pbytesCalculado

def tbyteParaKpbte(valorASerConvertido):
    print('Valor convertido de byte para bit')
    tbytesCalculado = valorASerConvertido * valorPadrão
    return tbytesCalculado


print('Insira o valor a ser convertido')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = pbyteParatbyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)