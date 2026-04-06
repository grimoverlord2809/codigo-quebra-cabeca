# ============================================================
# PEÇA 1 - separar.png
# Função que separa uma data no formato DDMMAAAA em três partes:
# dia, mes e ano. Recebe tudo junto como um número inteiro!
# ============================================================

def separar_data(dma):
    # Pego o ANO: os últimos 4 dígitos do número (ex: 01011990 → 1990)
    a = dma % 10000

    # Jogo fora o ano dividindo por 10000 (ex: 01011990 → 0101)
    dma //= 10000

    # Pego o MÊS: os últimos 2 dígitos que sobraram (ex: 0101 → 01)
    m = dma % 100

    # Jogo fora o mês dividindo por 100 (ex: 0101 → 01)
    dma //= 100

    # O que sobrou é o DIA (ex: 01)
    d = dma

    # Retorno os três valores separados: dia, mês e ano
    return d, m, a


# ============================================================
# PEÇA 2 - signo.png
# Função que descobre o signo com base no dia e mês de nascimento.
# Cada signo tem uma data de início e fim — comparo o dia para decidir!
# ============================================================

def signo(dia, mes):
    # Março: antes do dia 21 é Peixes, do dia 21 em diante é Áries
    if mes == 3:
        return 'Peixes' if dia < 21 else 'Aries'

    # Abril: antes do dia 20 é Áries, do dia 20 em diante é Touro
    if mes == 4:
        return 'Aries' if dia < 20 else 'Touro'

    # Maio: antes do dia 21 é Touro, do dia 21 em diante é Gêmeos
    if mes == 5:
        return 'Touro' if dia < 21 else 'Gemeos'

    # Junho: antes do dia 22 é Gêmeos, do dia 22 em diante é Câncer
    if mes == 6:
        return 'Gemeos' if dia < 22 else 'Cancer'

    # Julho: antes do dia 23 é Câncer, do dia 23 em diante é Leão
    if mes == 7:
        return 'Cancer' if dia < 23 else 'Leao'

    # Agosto: antes do dia 23 é Leão, do dia 23 em diante é Virgem
    if mes == 8:
        return 'Leao' if dia < 23 else 'Virgem'

    # Setembro: antes do dia 23 é Virgem, do dia 23 em diante é Libra
    if mes == 9:
        return 'Virgem' if dia < 23 else 'Libra'

    # Outubro: antes do dia 23 é Libra, do dia 23 em diante é Escorpião
    if mes == 10:
        return 'Libra' if dia < 23 else 'Escorpiao'

    # Novembro: antes do dia 22 é Escorpião, do dia 22 em diante é Sagitário
    if mes == 11:
        return 'Escorpiao' if dia < 22 else 'Sagitario'

    # Dezembro: antes do dia 22 é Sagitário, do dia 22 em diante é Capricórnio
    if mes == 12:
        return 'Sagitario' if dia < 22 else 'Capricornio'

    # Janeiro: antes do dia 20 é Capricórnio, do dia 20 em diante é Aquário
    if mes == 1:
        return 'Capricornio' if dia < 20 else 'Aquario'

    # Fevereiro: antes do dia 19 é Aquário, do dia 19 em diante é Peixes
    if mes == 2:
        return 'Aquario' if dia < 19 else 'Peixes'


# ============================================================
# PEÇA 3 - remover.png
# Função que tira os acentos de um texto.
# Precisamos disso porque a URL do site não aceita letras acentuadas!
# Ex: "Capricórnio" → "Capricornio" → "capricornio"
# ============================================================

def remover_acentos(texto):
    # Importa a função normalize da biblioteca unicodedata (já vem no Python)
    from unicodedata import normalize

    # normalize('NFKD', texto): decompõe os caracteres acentuados
    # .encode('ASCII', 'ignore'): converte para ASCII removendo o que não é suportado
    # .decode('ASCII'): transforma de volta para texto normal sem acentos
    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')


# ============================================================
# PEÇA 4 - horoscopo.png  +  CORREÇÃO APLICADA
# Função que acessa o site e pega o texto da previsão do dia.
#
# ⚠️  CORREÇÃO: o original usava '<p class="text-pred">' como marcador,
# mas o site foi atualizado e essa classe não existe mais.
# Agora localizamos o bloco <article class="text-wrapper"> e
# pegamos o primeiro <p> dentro dele — só o texto da previsão,
# sem baixar a página toda nem exibir o HTML desnecessário.
# ============================================================

def horoscopo(signo_desejado):
    # Importa a biblioteca para fazer requisições HTTP (já vem no Python)
    import urllib.request

    # Remove os acentos e deixa o nome do signo em minúsculas para usar na URL
    # Ex: "Capricornio" → "capricornio"
    signo_formatado = remover_acentos(signo_desejado).lower()

    # Monta a URL da página do signo no site
    # Ex: "https://www.horoscopovirtual.com.br/horoscopo/capricornio"
    minha_url = 'https://www.horoscopovirtual.com.br/horoscopo/' + signo_formatado

    # Cria a requisição com um cabeçalho User-Agent para o site não bloquear
    # (alguns sites bloqueiam acesso que não pareça um navegador real)
    requisicao = urllib.request.Request(
        url=minha_url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    # Envia a requisição e recebe a resposta do servidor
    resposta = urllib.request.urlopen(requisicao)

    # Lê o conteúdo HTML da página e decodifica para texto legível (UTF-8)
    pagina = resposta.read().decode('utf-8')

    # --- CORREÇÃO: nova estratégia de extração ---

    # Localiza a posição do bloco <article class="text-wrapper"> no HTML
    # É dentro desse artigo que fica o parágrafo com a previsão do dia
    inicio_article = pagina.find('class="text-wrapper"')

    # Define os marcadores de início e fim do parágrafo da previsão
    marcador_inicio = '<p>'   # abre o parágrafo
    marcador_final = '</p>'   # fecha o parágrafo

    # Encontra a posição exata onde começa o texto (após a tag <p>)
    # passando inicio_article garante que buscamos DENTRO do article certo
    inicio = pagina.find(marcador_inicio, inicio_article) + len(marcador_inicio)

    # Encontra onde termina o texto (na tag </p> que vem depois do início)
    final = pagina.find(marcador_final, inicio)

    # Retorna o nome do signo + ': ' + somente o texto da previsão
    # pagina[inicio:final] é o "recorte" exato do texto, sem HTML ao redor
    return signo_desejado + ': ' + pagina[inicio:final]


# ============================================================
# PEÇA 5 - main.png
# Função principal que organiza tudo: entrada, processamento e saída.
# ============================================================

def main():
    # --- Entrada de dados ---
    # Pede ao usuário a data de nascimento como número inteiro (DDMMAAAA)
    nascimento = int(input("Digite sua data de nascimento no formato DDMMAAAA: "))

    # --- Processamento ---
    # Usa a função separar_data para extrair dia, mês e ano
    # O _ descarta o ano, pois não precisamos dele para o horóscopo
    dia, mes, _ = separar_data(nascimento)

    # Descobre o signo com base no dia e mês extraídos
    meu_signo = signo(dia, mes)

    # Busca a previsão do dia para o signo encontrado
    horoscopo_de_hoje = horoscopo(meu_signo)

    # --- Saída de dados ---
    # Exibe a previsão na tela
    print(horoscopo_de_hoje)


# ============================================================
# PEÇA 6 - name.png
# Bloco padrão do Python: só executa main() se este arquivo
# for rodado diretamente (não quando importado por outro script).
# ============================================================

if __name__ == '__main__':
    main()
