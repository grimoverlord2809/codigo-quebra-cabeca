# Horóscopo do Dia 🔮

Programa em Python que, a partir da data de nascimento do usuário, identifica o signo e exibe a previsão do dia buscada diretamente do site [Horóscopo Virtual](https://www.horoscopovirtual.com.br).

---

## Como executar

```bash
python app.py
```

Informe a data de nascimento no formato `DDMMAAAA` quando solicitado:

```
Digite sua data de nascimento no formato DDMMAAAA: 01011990
Capricornio: O dia pede escuta interna e planejamento silencioso...
```

---

## Estrutura do código

### `separar_data(dma)`
Recebe um inteiro no formato `DDMMAAAA` e separa dia, mês e ano usando aritmética de divisão inteira e módulo.

```
01011990 → dia=01, mes=01, ano=1990
```

| Operação | Resultado |
|----------|-----------|
| `dma % 10000` | ano (últimos 4 dígitos) |
| `dma //= 10000` → `dma % 100` | mês |
| `dma //= 100` | dia |

---

### `signo(dia, mes)`
Determina o signo zodiacal com base no dia e mês de nascimento, usando as datas de corte de cada signo.

| Mês | Antes do dia | Signo | A partir do dia | Signo |
|-----|-------------|-------|-----------------|-------|
| 1 | 20 | Capricornio | 20 | Aquario |
| 2 | 19 | Aquario | 19 | Peixes |
| 3 | 21 | Peixes | 21 | Aries |
| 4 | 20 | Aries | 20 | Touro |
| 5 | 21 | Touro | 21 | Gemeos |
| 6 | 22 | Gemeos | 22 | Cancer |
| 7 | 23 | Cancer | 23 | Leao |
| 8 | 23 | Leao | 23 | Virgem |
| 9 | 23 | Virgem | 23 | Libra |
| 10 | 23 | Libra | 23 | Escorpiao |
| 11 | 22 | Escorpiao | 22 | Sagitario |
| 12 | 22 | Sagitario | 22 | Capricornio |

---

### `remover_acentos(texto)`
Remove acentos do nome do signo usando normalização Unicode (`NFKD`), necessário para montar a URL corretamente.

```python
"Capricórnio" → "Capricornio" → "capricornio"
```

---

### `horoscopo(signo_desejado)`
Faz uma requisição HTTP ao site `horoscopovirtual.com.br`, baixa o HTML da página do signo e extrai o texto da previsão do dia localizando o bloco `class="text-wrapper"` e o primeiro `<p>` dentro dele.

---

### `main()`
Orquestra o fluxo completo:
1. Lê a data de nascimento (entrada)
2. Separa dia, mês e ano
3. Determina o signo
4. Busca o horóscopo online
5. Exibe o resultado

---

### `if __name__ == '__main__'`
Garante que `main()` só seja executado quando o arquivo é rodado diretamente, não quando importado como módulo.

---

## Script completo

```python
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
```

---

## Requisitos

- Python 3.x
- Bibliotecas padrão apenas (`urllib`, `unicodedata`) — sem instalações adicionais
- Conexão com a internet
