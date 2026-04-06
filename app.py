# PECA 1 - separar.png
# Separa a data DDMMAAAA em dia, mes e ano usando divisao inteira e modulo
def separar_data(dma):
    a = dma % 10000      # pega os ultimos 4 digitos = ano
    dma //= 10000

    m = dma % 100        # pega os 2 digitos que sobraram = mes
    dma //= 100

    d = dma              # o que sobrou e o dia
    return d, m, a


# PECA 2 - signo.png
# Retorna o signo comparando o dia com a data de corte de cada signo
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


# PECA 3 - remover.png
# Remove acentos do texto para que o nome do signo funcione na URL
def remover_acentos(texto):
    from unicodedata import normalize
    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')


# PECA 4 - horoscopo.png
# Acessa o site e extrai apenas o texto da previsao do dia
#
# CORRECAO: o codigo original usava '<p class="text-pred">' como marcador,
# mas o site foi atualizado e essa classe nao existe mais.
# Agora localizamos o bloco <article class="text-wrapper"> e pegamos
# o primeiro <p> dentro dele, evitando capturar HTML indesejado.
def horoscopo(signo_desejado):
    import urllib.request

    # Monta a URL com o nome do signo sem acentos e em minusculas
    signo_formatado = remover_acentos(signo_desejado).lower()
    minha_url = 'https://www.horoscopovirtual.com.br/horoscopo/' + signo_formatado

    # Envia a requisicao com User-Agent para nao ser bloqueado pelo site
    requisicao = urllib.request.Request(
        url=minha_url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    resposta = urllib.request.urlopen(requisicao)
    pagina = resposta.read().decode('utf-8')

    # Localiza o artigo da previsao e recorta apenas o texto do <p>
    inicio_article = pagina.find('class="text-wrapper"')
    marcador_inicio = '<p>'
    marcador_final = '</p>'
    inicio = pagina.find(marcador_inicio, inicio_article) + len(marcador_inicio)
    final = pagina.find(marcador_final, inicio)

    return signo_desejado + ': ' + pagina[inicio:final]


# PECA 5 - main.png
# Funcao principal: entrada de dados, processamento e saida
def main():
    # Entrada de dados
    nascimento = int(input("Digite sua data de nascimento no formato DDMMAAAA: "))

    # Processamento
    dia, mes, _ = separar_data(nascimento)  # _ descarta o ano
    meu_signo = signo(dia, mes)
    horoscopo_de_hoje = horoscopo(meu_signo)

    # Saida de dados
    print(horoscopo_de_hoje)


# PECA 6 - name.png
# Executa main() somente quando o arquivo e rodado diretamente
if __name__ == '__main__':
    main()
