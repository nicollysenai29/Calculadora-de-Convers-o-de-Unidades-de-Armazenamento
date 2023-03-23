valorPadrão = 1024

def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def bitParaByte(valorASerConvertido):
    print('/8clear')
    bytesCalculado = valorASerConvertido / 8
    return bytesCalculado

def byteParaBit(valorASerConvertido):
    print('Valor convertido de byte para bit')
    bitsCalculado = valorASerConvertido * 8
    return bitsCalculado

def byteParaKByte(valorASerConvertido):
    print('/8clear')
    kbytesCalculado = valorASerConvertido / valorPadrão
    return kbytesCalculado

def kbyteParaByte(valorASerConvertido):
    print('Valor convertido de byte para bit')
    bytesCalculado = valorASerConvertido * valorPadrão
    return bytesCalculado

def byteParaKByte(valorASerConvertido):
    print('/8clear')
    kbytesCalculado = valorASerConvertido / valorPadrão
    return kbytesCalculado

def kbyteParaByte(valorASerConvertido):
    print('Valor convertido de byte para bit')
    bytesCalculado = valorASerConvertido * valorPadrão
    return bytesCalculado


print('Insira o valor a ser convertido')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = kbyteParaByte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

