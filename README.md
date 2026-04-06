# Semana 09 - Quebra Cabeca

**Prof:** Jose Ritomar Carneiro Torquato  
**Curso:** Tecnico em Desenvolvimento de Sistemas  
**Local:** Teresina Central (IFPI - Campus Teresina Central)

**Aluno:** Valdeney Sousa Amaral  
**Disciplina:** Programacao Estruturada de Computadores

---

## O que e esse projeto?

Esse projeto foi uma atividade de quebra-cabeca: o professor deu 6 imagens, cada uma com um pedaco de codigo Python, e a gente teve que montar o programa na ordem certa.

O programa pede a data de nascimento da pessoa, descobre o signo dela e busca o horoscopo do dia direto do site [Horoscopo Virtual](https://www.horoscopovirtual.com.br).

---

## As pecas do quebra-cabeca

### Peca 1 — separar.png
![separar.png](separar.png)

Essa funcao `separar_data` recebe a data toda junta como numero (ex: `01011990`) e separa em dia, mes e ano. Ela usa divisao inteira e modulo pra isso.

---

### Peca 2 — signo.png
![signo.png](signo.png)

Essa funcao `signo` olha o dia e o mes e devolve o nome do signo. Tem um `if` pra cada mes do ano, comparando com a data de corte de cada signo.

---

### Peca 3 — remover.png
![remover.png](remover.png)

Essa funcao `remover_acentos` tira os acentos das palavras. Precisa disso porque o nome do signo vai ser usado na URL do site, e URL nao aceita acento (ex: `Capricornio` vira `capricornio`).

---

### Peca 4 — horoscopo.png  ⚠️ Correcao feita aqui!
![horoscopo.png](horoscopo.png)

Essa funcao `horoscopo` acessa o site e pega apenas o texto da previsao do dia.

**Problema que encontrei:** o codigo da imagem usava `<p class="text-pred">` pra achar o texto no HTML, mas quando fui testar o programa nao funcionava. Descobri que o site foi atualizado e essa parte do HTML nao existe mais.

**Como resolvi:** procurei no HTML do site onde a previsao estava e achei que agora ela fica dentro de um `<article class="text-wrapper">`. Entao mudei o codigo pra localizar esse artigo primeiro e depois pegar o `<p>` que tem o texto da previsao. Assim so aparece o texto, sem mostrar o HTML todo.

---

### Peca 5 — main.png
![main.png](main.png)

Essa funcao `main` e a principal, que junta tudo: pede a data pro usuario, chama as outras funcoes e imprime o resultado.

---

### Peca 6 — name.png
![name.png](name.png)

Esse bloco `if __name__ == '__main__'` e um padrao do Python. Ele garante que o programa so comeca a rodar quando o arquivo e executado diretamente.

---

## Como rodar

```bash
python app.py
```

Ai so digitar a data de nascimento no formato `DDMMAAAA`:

```
Digite sua data de nascimento no formato DDMMAAAA: 01011990
Capricornio: O dia pede escuta interna e planejamento silencioso...
```

---

## O que cada funcao faz (resumo)

| Funcao | Imagem | O que faz |
|--------|--------|-----------|
| `separar_data` | separar.png | Separa DDMMAAAA em dia, mes e ano |
| `signo` | signo.png | Descobre o signo pelo dia e mes |
| `remover_acentos` | remover.png | Tira acentos para usar na URL |
| `horoscopo` | horoscopo.png | Busca o horoscopo no site |
| `main` | main.png | Funcao principal, junta tudo |
| `if __name__` | name.png | Ponto de entrada do programa |

---

## O que precisei mudar no codigo original

A unica mudanca necessaria foi na funcao `horoscopo` (peca 4):

| | Codigo da imagem | Codigo corrigido |
|--|--|--|
| Marcador original | `<p class="text-pred">` | `class="text-wrapper"` + `<p>` |
| Motivo | Classe foi removida do site | — |
| Resultado | Programa nao achava o texto | Busca e mostra so a previsao |

---

## O que precisa ter instalado

- Python 3
- Nao precisa instalar nada extra, usa so bibliotecas que ja vem no Python
- Precisa de internet pra acessar o site
