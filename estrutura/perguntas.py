import pandas as pd

dados = pd.read_excel('estrutura/Base de dados.xlsx',index_col=0)

perguntas = dados.index.values
respostas = dados['Respostas'].values
respostas_erradas_df = dados['Respostas Erradas'].values

perguntas_respostas = {pergunta:resposta for pergunta,resposta in zip(perguntas,respostas)}
alternativas_erradas = {pergunta:tuple(conjunto_respostas_erradas.split(';')) 
                        for pergunta,conjunto_respostas_erradas in zip(perguntas,respostas_erradas_df)}

total_questoes = len(perguntas_respostas)
