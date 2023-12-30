'''
perguntas_respostas = {'Quem criou a linguagem Python?':'Guido Van Rossum',
             'Qual é o formato da Terra?':'Geóide',
             'Quem descobriu o Brasil?':'Já existiam povos aqui antes dos europeus',
             'Quem venceu a 2a Guerra Mundial?':'Aliados',
             'Qual banda é a rival da Mimol Band?':'3 da Tarde',
             'Como que o Comando Vermelho executa as suas vítimas?':'Micro-ondas',
             'Quem é considerado o homem mais poderoso do mundo (2021)?':'Xi-Jinping',
             'Em que ano nasceu Jeff Bezos':1964,
             'Quem inventou o avião?':'Santos Dumont',
             'Quem perdeu o relacionamento após soltar um torpedo na casa do(a) parceiro(a)?':'Pablosky',
             'Onde as batatas foram fritas pela primeira vez?':'Bélgica',
             'Qual desses países perdeu uma guerra para fazendeiros vietnamitas?':'Estados Unidos',
             'Quais países NÃO utilizam o sistema métrico?':'Myanmar, Libéria e Estados Unidos',
             'Os veículos elétricos emitem mais ou menos CO2 em comparação aos a combustão?':'Depende da matriz energética',
             'É possível reproduzir um ciclo Carnot no mundo real?':'Não',
             'Qual movimento literário serviu de inspiração para o sistema operacional Mimox?':'Parnasianismo'}

alternativas_erradas = {'Quem criou a linguagem Python?':('MC Poze do Rodo','Gabriel Monteiro',
    'Hans Schwiegersohn','Harry Williams','Gabriel Jucá','Todas as alternativas',
    'Larry Page','Elon Musk','Albert Einstein','Thomas Bangalter'),
      'Qual é o formato da Terra?':('Parabólico','Esférico','Plano','Hiperbólico',
      'Senoidal','Euclidiano','Nenhuma das alternativas'),
      'Quem descobriu o Brasil?':('George Soros','Deus','Marília Mendonça','Jair Bolsonaro',
       'Pedro Álvares Cabral','Cristóvão Colombo','Vasco da Gama','Bill Gates','Adolf Hitler',),
      'Quem venceu a 2a Guerra Mundial?':('Os nazistas','O eixo','Japão','Namíbia','Afeganistão',
      'Estados Unidos','Chade','Alemanha','Suíça','Países Baixos','Itália','Brasil'),
      'Qual banda é a rival da Mimol Band?':('3 da manhã','One Direction','Daft Punk','Nirvana',
      'Artic Monkeys','Guns n Roses','Led Zeppelin','Legião Urbana','Engenheiros do Havaí'),
      'Como que o Comando Vermelho executa as suas vítimas?':('Fogão','Geladeira','Cadeira elétrica',
      'Injeção letal','Usando uma pena','Empalamento','Usando uma sacola','Obrigando a ouvir funk paulista'),
      'Quem é considerado o homem mais poderoso do mundo (2021)?':('Gabigol','Jean Wyllys','Pablo Vittar','Bruno Henrique',
      'Carl Johnson','Joe Biden','Nicolás Maduro','Jair Bolsonaro','Gabriel Monteiro','Olaf Scholz','Eduardo Cunha','Elon Musk',
      'Jeff Bezos','Jorge Jesus','Deus','Getúlio Vargas','Vladmir Putin','Neymar Jr.','George Soros'),
      'Em que ano nasceu Jeff Bezos':(1960,1970,1962,1980,1979,1975,1955,1954,1961,1963,1965,1966,1967),
      'Quem inventou o avião?':('Irmãos Wright','Machado de Assis','Marechal Deodoro','Adolf Hitler',
      'Vladmir Lênin','Neymar Jr.','Kevin o Chris','Olavo Bilac','Isaac Newton','Albert Einstein','Stephen Hawking'),
      'Quem perdeu o relacionamento após soltar um torpedo na casa do(a) parceiro(a)?':('Vladmir Putin','Joel Morvan',
      'Donald Trump','Yuri Gagarin','Eudemar Sovislei','Gabigordo','Jovem Dex','Eduardo Cunha'),
      'Onde as batatas foram fritas pela primeira vez?':('França','Estados Unidos','Países Baixos','Alemanha',
      'McDonalds','Salmonela Lanches','Suíça','Itália','Brasil','Etiópia','Somália','China'),
      'Qual desses países perdeu uma guerra para fazendeiros vietnamitas?':('México','União Soviética','Coreia do Norte',
      'Japão','China','Alemanha','Brasil','França','Portugal','África do Sul','Angola','Quênia'),
      'Quais países NÃO utilizam o sistema métrico?':('Portugal,Estados Unidos e China','Estados Unidos, Japão e Coreia do Norte',
      'Brasil, China e Estados Unidos','República Centro-Africana, Libéria e Rússia','Canadá, México e Estados Unidos'),
      'Os veículos elétricos emitem mais ou menos CO2 em comparação aos a combustão?':('Mais','Menos','Muito mais','Muito menos',
      'Mesma coisa','Depende dos processos termodinâmicos','Depende da massa do veículo','Tudo indica que talvez'),
      'É possível reproduzir um ciclo Carnot no mundo real?':('Sim','Somente usando combustíveis fósseis',
      'Somente usando combustíveis renováveis','Somente em combustão completa','Somente em combustão incompleta'),
      'Qual movimento literário serviu de inspiração para o sistema operacional Mimox?':('Romantismo','Modernismo','Futurismo',
      'Trovadorismo','Barroco','Arcadismo','Simbolismo','Naturalismo','Realismo')}
'''
import pandas as pd

dados = pd.read_excel('estrutura/Base de dados.xlsx',index_col=0)

perguntas = dados.index.values
respostas = dados['Respostas'].values
respostas_erradas_df = dados['Respostas Erradas'].values

perguntas_respostas = {pergunta:resposta for pergunta,resposta in zip(perguntas,respostas)}
alternativas_erradas = {pergunta:tuple(conjunto_respostas_erradas.split(';')) 
                        for pergunta,conjunto_respostas_erradas in zip(perguntas,respostas_erradas_df)}

total_questoes = len(perguntas_respostas)