
from random import shuffle

if __name__  == '__main__':
    from perguntas import *
else:
    from estrutura.perguntas import *


def escolher_perguntas(qtd_perguntas):

    perguntas_aleatorias = list(perguntas_respostas.keys())
    shuffle(perguntas_aleatorias)

    return perguntas_aleatorias[:qtd_perguntas]


def gerar_alternativas(pergunta):

    letras = 'ABCDE'
    possiveis_respostas_erradas = list(alternativas_erradas.get(pergunta))
    resposta_certa = perguntas_respostas.get(pergunta)

    shuffle(possiveis_respostas_erradas)
    respostas = possiveis_respostas_erradas[:4]
    
    respostas.append(resposta_certa)
    shuffle(respostas)

    alternativas = {letra : resposta for letra,resposta in zip(letras,respostas)}

    return alternativas


def resposta_esta_certa(pergunta,resposta_dada):

    return perguntas_respostas.get(pergunta) == resposta_dada


