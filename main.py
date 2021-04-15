def converte(numero):
    convert = (
        f'[Sinal]: {sinal(numero)} | [Expoente]: {expoente(numero)} | [Mantissa]: {mantissa(numero)}')
    return convert


def numero_to_bin(numero):
    valor = str(numero).split('.')

    # Resgata apenas a parte dos números decimais.
    join = float(''.join('0.' + valor[1]))
    resultados = []

    # Faz a multiplicação dos números decimais até o requisito ser cumprido.
    while join != 1.0:
        if join > 1.0:
            join -= 1
        else:
            join *= 2
            resultados.append(join)
    # Não é nescessário converter os números para binário, pois eles já são
    # entregues em forma de 1 e 0.
    numeros_iniciais = [str(x)[0:1] for x in resultados]
    decimal_bin = ''.join(numeros_iniciais)

    # Trechos responsáveis para fazer a conversão do número inteiro em binário.
    inteiro = ''.join(valor[0])
    # Caso houver o símbolo de negativo, remove para não dar conflito com a
    # operação.
    if inteiro[0] == '-':
        inteiro = inteiro.replace('-', '')
    inteiro = bin(int(inteiro))
    binary = ''.join(inteiro[2:])

    # Número enviado completo em binário
    complete_number = binary + '.' + decimal_bin
    return complete_number


def sinal(numero):
    # Se o número for positivo retorna o Bit desativado, se não ativado.
    if numero > 0:
        return '0'
    else:
        return '1'


def expoente(numero):
    # Número completo em binário, resgata a parte do número inteiro,
    # conta os caracteres é remove 1, assim sendo o valor do expoente.
    valor = str(numero_to_bin(numero))

    # Caso o número seja 0.n, é nescessário movimentar a vírgula, contando
    # quantas casas foram puladas, sendo o expoente negativo.
    if numero < 1 and numero > -1:
        split = valor.split('.')[1]
        cont = 0
        for i in split:
            cont += 1
            if i == '1':
                break

        expoente = bin(127 - cont)[2:]

        if len(expoente) < 8:
            expoente = str(expoente.zfill(8))

        return expoente

    valor = valor.split('.')
    qtd = len(valor[0])
    qtd -= 1
    # Padrão da operação 127(bias) + expoente.
    expoente = bin(127 + qtd)[2:]
    # Caso o valor seja menor que 8 bits, usa a função zfill para preencher
    # com zeros a esquerda, até o número informado.
    if len(expoente) < 8:
        expoente = str(expoente.zfill(8))
    return expoente


def mantissa(numero):
    # Resgata todo o número em binário apenas tirando o primeiro valor.
    valor = str(numero_to_bin(numero))

    # Caso o número inteiro for 0.n, é nescessário chegar até um
    # valor que seja 1 em binário e após considerar como parte fracionária.
    if float(valor) < 1 and float(valor) > -1:
        valor = valor.replace('.', '')[1:]
        cont = 0
        for i in valor:
            cont += 1
            if i == '1':
                mantissa = valor[cont:]
                mantissa = mantissa.ljust(23, '0')
                if len(mantissa) > 23:
                    mantissa = mantissa[0:23]
                return mantissa

    valor = valor.replace('.', '')[1:]
    # Caso o valor da mantissa seja menor que 23 bits, alinha a esquerda e
    # complementa com zeros usando a função ljust.
    mantissa = valor.ljust(23, '0')
    # Caso seja maior que 23, captura só 23 bits.
    if len(mantissa) > 23:
        mantissa = mantissa[0:23]
    return mantissa
