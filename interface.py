from tkinter import *
from PIL import Image,ImageTk
from threading import Timer
from estrutura.funcoes_jogo import escolher_perguntas,gerar_alternativas,resposta_esta_certa


TOTAL_QUESTOES = 16

CAMINHO_LOGO = 'Fótons/Ícone.png'

LARGURA_JANELA,ALTURA_JANELA = 700,500
MARGEM_X,MARGEM_Y = 100,70
COR_FUNDO = 'black'

LARGURA_LOGO,ALTURA_LOGO = int(LARGURA_JANELA/3),int(ALTURA_JANELA/4)

LARGURA_BOTAO_INICIO,ALTURA_BOTAO_INICIO = int(LARGURA_JANELA/100),int(LARGURA_JANELA/700)
COR_FUNDO_BOTAO,COR_TEXTO_BOTAO = '#FF66FF','#66FFFF'

LARGURA_IMAGEM_FIM,ALTURA_IMAGEM_FIM = 400,300

global numero_questao,pontuacao,perguntas,pergunta_respondida
global enunciado,botao_alternativa,texto_pontuacao,foto_correcao_exibida,foto_resultado,botao_reinicio
global cronometro




def iniciar_jogo():

    global numero_questao,perguntas,pontuacao,pergunta_respondida
    global enunciado,botao_alternativa

    numero_questao = 1
    pontuacao = 0
    pergunta_respondida = False



    for elemento in janela.winfo_children():
        elemento.destroy()


    perguntas = escolher_perguntas(TOTAL_QUESTOES)

    pergunta = perguntas[numero_questao - 1]
    alternativas_esta_pergunta = gerar_alternativas(pergunta)

    enunciado = Label(janela,text = f'{numero_questao}) {pergunta}',
                      fg = 'white',bg = COR_FUNDO,font = ('Comic Sans MS',24,),
                      wraplength = LARGURA_JANELA)
    
    enunciado.pack()


    opcoes = list(alternativas_esta_pergunta.values())

    botao_alternativa_A = Button(janela,text = f'A) {opcoes[0]}',
                                        command = lambda :escolher_alternativa(pergunta,opcoes[0]),
                                        fg = 'white',bg = COR_FUNDO,
                                        font = ('Comic Sans Ms',16))
    
    botao_alternativa_B = Button(janela,text = f'B) {opcoes[1]}',
                                        command = lambda :escolher_alternativa(pergunta,opcoes[1]),
                                        fg = 'white',bg = COR_FUNDO,
                                        font = ('Comic Sans Ms',16))
    
    botao_alternativa_C = Button(janela,text = f'C) {opcoes[2]}',
                                        command = lambda :escolher_alternativa(pergunta,opcoes[2]),
                                        fg = 'white',bg = COR_FUNDO,
                                        font = ('Comic Sans Ms',16))
    
    botao_alternativa_D = Button(janela,text = f'D) {opcoes[3]}',
                                        command = lambda :escolher_alternativa(pergunta,opcoes[3]),
                                        fg = 'white',bg = COR_FUNDO,
                                        font = ('Comic Sans Ms',16))
    
    botao_alternativa_E = Button(janela,text = f'E) {opcoes[4]}',
                                        command = lambda :escolher_alternativa(pergunta,opcoes[4]),
                                        fg = 'white',bg = COR_FUNDO,
                                        font = ('Comic Sans Ms',16))
        
    botao_alternativa_A.bind('<Enter>',passar_mouse_alternativa)
    botao_alternativa_A.bind('<Leave>',retirar_mouse_alternativa)

    botao_alternativa_B.bind('<Enter>',passar_mouse_alternativa)
    botao_alternativa_B.bind('<Leave>',retirar_mouse_alternativa)

    botao_alternativa_C.bind('<Enter>',passar_mouse_alternativa)
    botao_alternativa_C.bind('<Leave>',retirar_mouse_alternativa)

    botao_alternativa_D.bind('<Enter>',passar_mouse_alternativa)
    botao_alternativa_D.bind('<Leave>',retirar_mouse_alternativa)

    botao_alternativa_E.bind('<Enter>',passar_mouse_alternativa)
    botao_alternativa_E.bind('<Leave>',retirar_mouse_alternativa)

    botao_alternativa_A.pack()
    botao_alternativa_B.pack()
    botao_alternativa_C.pack()
    botao_alternativa_D.pack()
    botao_alternativa_E.pack()



def escolher_alternativa(pergunta,resposta_dada):
    global pontuacao,foto_correcao_exibida,pergunta_respondida
    global cronometro

    if not pergunta_respondida:

        pergunta_respondida = True

        if resposta_esta_certa(pergunta = pergunta,resposta_dada = resposta_dada):
            pontuacao += 1
            foto_correcao = foto_certo_modificada
            
        else:
            foto_correcao = foto_errado_modificada
            

        foto_correcao_exibida = Label(janela,image = foto_correcao,bg = COR_FUNDO)

        foto_correcao_exibida.pack(anchor = 'se')
        
        cronometro = Timer(1.5,function = proxima_pergunta)
        cronometro.start()
    
    
    


    
    

def proxima_pergunta():

    global numero_questao,pontuacao,pergunta_respondida
    global enunciado,botao_alternativa

    pergunta_respondida = False

    for elemento in janela.winfo_children():
                elemento.destroy()

    if numero_questao < TOTAL_QUESTOES:

        numero_questao += 1 
        pergunta = perguntas[numero_questao - 1]
        alternativas_esta_pergunta = gerar_alternativas(pergunta)
        alternativa_escolhida = StringVar(value = '')

        enunciado = Label(janela,text = f'{numero_questao}) {pergunta}',
                        fg = 'white',bg = COR_FUNDO,font = ('Comic Sans MS',24,),
                        wraplength = LARGURA_JANELA)
        
        enunciado.pack()


        opcoes = list(alternativas_esta_pergunta.values())

        botao_alternativa_A = Button(janela,text = f'A) {opcoes[0]}',
                                            command = lambda :escolher_alternativa(pergunta,opcoes[0]),
                                            fg = 'white',bg = COR_FUNDO,
                                            font = ('Comic Sans Ms',16))
        
        botao_alternativa_B = Button(janela,text = f'B) {opcoes[1]}',
                                            command = lambda :escolher_alternativa(pergunta,opcoes[1]),
                                            fg = 'white',bg = COR_FUNDO,
                                            font = ('Comic Sans Ms',16))
        
        botao_alternativa_C = Button(janela,text = f'C) {opcoes[2]}',
                                            command = lambda :escolher_alternativa(pergunta,opcoes[2]),
                                            fg = 'white',bg = COR_FUNDO,
                                            font = ('Comic Sans Ms',16))
        
        botao_alternativa_D = Button(janela,text = f'D) {opcoes[3]}',
                                            command = lambda :escolher_alternativa(pergunta,opcoes[3]),
                                            fg = 'white',bg = COR_FUNDO,
                                            font = ('Comic Sans Ms',16))
        
        botao_alternativa_E = Button(janela,text = f'E) {opcoes[4]}',
                                            command = lambda :escolher_alternativa(pergunta,opcoes[4]),
                                            fg = 'white',bg = COR_FUNDO,
                                            font = ('Comic Sans Ms',16))
            
        botao_alternativa_A.bind('<Enter>',passar_mouse_alternativa)
        botao_alternativa_A.bind('<Leave>',retirar_mouse_alternativa)

        botao_alternativa_B.bind('<Enter>',passar_mouse_alternativa)
        botao_alternativa_B.bind('<Leave>',retirar_mouse_alternativa)

        botao_alternativa_C.bind('<Enter>',passar_mouse_alternativa)
        botao_alternativa_C.bind('<Leave>',retirar_mouse_alternativa)

        botao_alternativa_D.bind('<Enter>',passar_mouse_alternativa)
        botao_alternativa_D.bind('<Leave>',retirar_mouse_alternativa)

        botao_alternativa_E.bind('<Enter>',passar_mouse_alternativa)
        botao_alternativa_E.bind('<Leave>',retirar_mouse_alternativa)

        botao_alternativa_A.pack()
        botao_alternativa_B.pack()
        botao_alternativa_C.pack()
        botao_alternativa_D.pack()
        botao_alternativa_E.pack()


        
    else:
        exibir_pontuacao()


def exibir_pontuacao():

    global texto_pontuacao,foto_resultado,botao_reinicio

    if pontuacao == 1:
         texto = f'Você fez 1 ponto!'
    else:
         texto = f'Você fez {pontuacao} pontos!'

    texto_pontuacao = Label(janela,text= texto,
                                    fg = 'white',bg = COR_FUNDO,font=('Comic Sans MS',24))
            
    texto_pontuacao.pack(anchor = 'center')

    botao_resultado = Button(janela, text = 'Jogar novamente',command = iniciar_jogo,
                      font = ('Comic Sans MS',18,'bold'),fg = COR_TEXTO_BOTAO,bg = COR_FUNDO_BOTAO,
                      width = 2*LARGURA_BOTAO_INICIO , height = int(0.8*ALTURA_BOTAO_INICIO))
 
    botao_resultado.place(relx = 1/2,rely = 9/10, anchor = 'center')

    botao_resultado.bind('<Enter>',passar_mouse_botao)
    botao_resultado.bind('<Leave>',tirar_mouse_botao)

    if pontuacao <= 5:
         foto_resultado = Label(janela,image = foto_pontuacao_baixa_modificada,bg = COR_FUNDO)
    elif pontuacao <= 10:
         foto_resultado = Label(janela,image = foto_pontuacao_media_modificada,bg = COR_FUNDO)
    else:
         foto_resultado = Label(janela,image = foto_pontuacao_alta_modificada,bg = COR_FUNDO)
    
    foto_resultado.place(x = (LARGURA_JANELA - LARGURA_IMAGEM_FIM)/2,y = (ALTURA_JANELA - ALTURA_IMAGEM_FIM)/2)




def passar_mouse_botao(evento):
    evento.widget.config(fg = '#337F7F',bg = '#853594')


def tirar_mouse_botao(evento):
    evento.widget.config(fg = COR_TEXTO_BOTAO,bg = COR_FUNDO_BOTAO)

def passar_mouse_alternativa(evento):
    evento.widget.config(fg = 'grey')

def retirar_mouse_alternativa(evento):
    evento.widget.config(fg = 'white')


janela = Tk()

janela.config(bg = COR_FUNDO)
janela.title('Quiz')

janela.geometry(f'{LARGURA_JANELA}x{ALTURA_JANELA}+{MARGEM_X}+{MARGEM_Y}')

icone = PhotoImage(file = CAMINHO_LOGO)
janela.iconphoto(True,icone)

logo = Image.open('Fótons/Ícone.png').resize((LARGURA_LOGO,ALTURA_LOGO))
logo_tela_inicial = ImageTk.PhotoImage(logo)

rotulo_imagem = Label(janela,image = logo_tela_inicial,bg = COR_FUNDO)
rotulo_imagem.place(x = (LARGURA_JANELA - LARGURA_LOGO)/2,y = ALTURA_JANELA/8)

botao_inicio = Button(janela, text = 'Jogar',command = iniciar_jogo,
                      font = ('Comic Sans MS',20,'bold'),fg = COR_TEXTO_BOTAO,bg = COR_FUNDO_BOTAO,
                      width = LARGURA_BOTAO_INICIO , height = ALTURA_BOTAO_INICIO)

botao_inicio.place(relx = 1/2,rely = 2/3, anchor = 'center')

botao_inicio.bind('<Enter>',passar_mouse_botao)
botao_inicio.bind('<Leave>',tirar_mouse_botao)

autor = Label(janela,text='© Lobato J.F.C \n a.k.a Imperador João',font=('Comic Sans MS',13),
              fg = 'white',bg = COR_FUNDO)
autor.pack(anchor='ne')


#Fotos a serem exibidas

foto_certo = Image.open('Fótons/Certo.png').resize((70,70))
foto_errado = Image.open('Fótons/Errado.png').resize((70,70))

foto_certo_modificada = ImageTk.PhotoImage(foto_certo)
foto_errado_modificada = ImageTk.PhotoImage(foto_errado)


foto_pontuacao_baixa = Image.open('Fótons/Pontuação baixa.jpg').resize((LARGURA_IMAGEM_FIM,ALTURA_IMAGEM_FIM))
foto_pontuacao_baixa_modificada = ImageTk.PhotoImage(foto_pontuacao_baixa)

foto_pontuacao_media = Image.open('Fótons/Pontuação media.jpg').resize((LARGURA_IMAGEM_FIM,ALTURA_IMAGEM_FIM))
foto_pontuacao_media_modificada = ImageTk.PhotoImage(foto_pontuacao_media)

foto_pontuacao_alta = Image.open('Fótons/Pontuação alta.jpg').resize((LARGURA_IMAGEM_FIM,ALTURA_IMAGEM_FIM))
foto_pontuacao_alta_modificada = ImageTk.PhotoImage(foto_pontuacao_alta)

janela.mainloop()