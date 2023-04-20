medida = 1024
unidades = ["bit","byte","kilobyte","megabyte","gigabyte","terabyte","petabyte"]

def conversor(valorInicial,unidade1,unidade2):
    print(f'Conversão executada ({unidade1} PARA {unidade2})')
    valorFinal = valorInicial
    if(unidade1 == "bit"):
        valorFinal = valorFinal / 8
        unidade1 = "byte"
    if(unidades.index(unidade1) < unidades.index(unidade2)):
        for i in range(unidades.index(unidade1), unidades.index(unidade2)):
            valorFinal = valorFinal / medida
    else:
        for i in range(unidades.index(unidade1), unidades.index(unidade2),-1):
            valorFinal = valorFinal * medida
        if(unidade2 == "bit"):
            valorFinal = (valorFinal / medida) * 8
    return print(valorFinal)