def separar_data(dma):
    a = dma % 10000
    dma //= 10000

    m = dma % 100
    dma //= 100

    d = dma
    return d, m, a


def signo(dia, mes):
    if mes == 3:
        return 'Peixes' if dia < 21 else 'Aries'
    if mes == 4:
        return 'Aries' if dia < 20 else 'Touro'
    if mes == 5:
        return 'Touro' if dia < 21 else 'Gemeos'
    if mes == 6:
        return 'Gemeos' if dia < 22 else 'Cancer'
    if mes == 7:
        return 'Cancer' if dia < 23 else 'Leao'
    if mes == 8:
        return 'Leao' if dia < 23 else 'Virgem'
    if mes == 9:
        return 'Virgem' if dia < 23 else 'Libra'
    if mes == 10:
        return 'Libra' if dia < 23 else 'Escorpiao'
    if mes == 11:
        return 'Escorpiao' if dia < 22 else 'Sagitario'
    if mes == 12:
        return 'Sagitario' if dia < 22 else 'Capricornio'
    if mes == 1:
        return 'Capricornio' if dia < 20 else 'Aquario'
    if mes == 2:
        return 'Aquario' if dia < 19 else 'Peixes'


def remover_acentos(texto):
    from unicodedata import normalize

    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')


def horoscopo(signo_desejado):
    import urllib.request

    signo_formatado = remover_acentos(signo_desejado).lower()

    minha_url = 'https://www.horoscopovirtual.com.br/horoscopo/' + signo_formatado

    requisicao = urllib.request.Request(
        url=minha_url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    resposta = urllib.request.urlopen(requisicao)

    pagina = resposta.read().decode('utf-8')

    inicio_article = pagina.find('class="text-wrapper"')
    marcador_inicio = '<p>'
    marcador_final = '</p>'

    inicio = pagina.find(marcador_inicio, inicio_article) + len(marcador_inicio)
    final = pagina.find(marcador_final, inicio)

    return signo_desejado + ': ' + pagina[inicio:final]


def main():
    # Entrada de dados
    nascimento = int(input("Digite sua data de nascimento no formato DDMMAAAA: "))

    # Processamento
    dia, mes, _ = separar_data(nascimento)
    meu_signo = signo(dia, mes)
    horoscopo_de_hoje = horoscopo(meu_signo)

    # Saida de dados
    print(horoscopo_de_hoje)


if __name__ == '__main__':
    main()
