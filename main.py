import pygame
from pygame.locals import *
import os
from mapa import *
from level import Level
from bd import *
#from player import Player

# inicia o pygame
pygame.init()
 
# centrar a aplicação
os.environ['SDL_VIDEO_CENTERED'] = '1'
 
#resolução
screen=pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("Imagens/cave3.jpg")

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText
 
 
#cores
branco=(255, 255, 255)
preto=(0, 0, 0)
cor_fundo=(16, 58, 125)
cor_titulo=(230, 108, 32)
 
#Tipo de letra
font = "Chicken Cripsy.ttf"
 
 
#FPS
clock = pygame.time.Clock()
FPS = 30

#variaveis de jogo
level = Level(mapa1, screen)
start_time = 0
coins = 0
time = 0
selection = "menu"
jogo_correndo = False


#menu principal
def main_menu():
     
    selected = 1
 
    while True:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            
            #seleçao das opçoes
            if event.type==KEYDOWN:
                if event.key == K_UP:
                    if (selected != 1):
                        selected -= 1
                if event.key == K_DOWN:
                    if(selected != 4):
                        selected +=1
                if event.key == K_SPACE or event.key == K_RETURN:
                    if(selected == 1):
                        return "jogar_reset"
                    if(selected == 2):
                        return "instrucoes"
                    if(selected == 3):
                        return "leaderboard"
                    if(selected == 4):
                        return "quit"

        #texto do menu
        screen.fill(cor_fundo)
        title=text_format("JUMPY", font, 60, cor_titulo)
        if selected == 1:
            text_start=text_format("JOGAR", font, 55, branco)
        else:
            text_start = text_format("JOGAR", font, 55, preto)
        if selected == 2:
            text_instrucoes=text_format("INSTRUCOES", font, 55, branco)
        else:
            text_instrucoes = text_format("INSTRUCOES", font, 55, preto)
        if selected == 3:
            text_leaderboard = text_format("LEADERBOARD", font, 55, branco)  
        else:
            text_leaderboard = text_format("LEADERBOARD", font, 55, preto)
        if selected == 4:
            text_quit=text_format("SAIR", font, 55, branco)
        else:
            text_quit = text_format("SAIR", font, 55, preto)
        
            title_rect=title.get_rect()
            start_rect=text_start.get_rect()
            instrucoes_rect=text_instrucoes.get_rect()
            quit_rect=text_quit.get_rect()
            leaderboard_rect = text_leaderboard.get_rect()
        
        #posição do texto
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_instrucoes, (screen_width/2 - (instrucoes_rect[2]/2), 360))
        screen.blit(text_leaderboard, (screen_width/2 - (leaderboard_rect[2]/2), 420))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 480))

        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Jumpy")


#menu para quando o jogo esta em pausa
def menu_pausa():

    selected = 1

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            
            #seleçao das opçoes
            if event.type==KEYDOWN:
                if event.key == K_UP:
                    if (selected != 1):
                        selected -= 1
                if event.key == K_DOWN:
                    if(selected != 5):
                        selected +=1
                if event.key == K_SPACE or event.key == K_RETURN:
                    if(selected == 1):
                        return "jogar_continue"
                    if(selected == 2):
                        return "jogar_reset"
                    if(selected == 3):
                        return "instrucoes"
                    if(selected == 4):
                        return "leaderboard"
                    if(selected == 5):
                        return "quit"
                    

        #texto do menu
        screen.fill(cor_fundo)
        title=text_format("JOGO EM PAUSA", font, 60, cor_titulo)
        if selected == 1:
            text_continue=text_format("CONTINUAR", font, 55, branco)
        else:
            text_continue = text_format("CONTINUAR", font, 55, preto)
        if selected == 2:
            text_restart = text_format("RESTART", font, 55, branco)
        else:
            text_restart = text_format("RESTART", font, 55, preto)
        if selected == 3:
            text_instrucoes=text_format("instrucoes", font, 55, branco)
        else:
            text_instrucoes = text_format("instrucoes", font, 55, preto)
        if selected == 4:
            text_leaderboard = text_format("LEADERBOARD", font, 55, branco)  
        else:
            text_leaderboard = text_format("LEADERBOARD", font, 55, preto)
        if selected == 5:
            text_quit=text_format("SAIR", font, 55, branco)
        else:
            text_quit = text_format("SAIR", font, 55, preto)
        
            title_rect=title.get_rect()
            continue_rect=text_continue.get_rect()
            restart_rect = text_restart.get_rect()
            instrucoes_rect=text_instrucoes.get_rect()
            leaderboard_rect = text_leaderboard.get_rect()
            quit_rect=text_quit.get_rect()
            
        
        #posição do texto
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_continue, (screen_width/2 - (continue_rect[2]/2), 300))
        screen.blit(text_restart, (screen_width/2 - (restart_rect[2]/2), 360))
        screen.blit(text_instrucoes, (screen_width/2 - (instrucoes_rect[2]/2), 420))
        screen.blit(text_leaderboard, (screen_width/2 - (leaderboard_rect[2]/2), 480))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 540))

        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Jumpy")


#ecra com as instrucoes/teclas
def instrucoes():
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
               if event.key == K_ESCAPE:
                   return "menu"
               
        screen.fill(cor_fundo)

        #texto
        title=text_format("INSTRUCOES", font, 60, cor_titulo)
        explicacao = text_format("APANHE A CHAVE PARA ABRIR A PORTA E ACABAR O NIVEL", font, 30, preto)
        move_up = text_format("SALTAR - SETA PARA CIMA", font, 30, preto)
        move_right = text_format("ESQUERDA - SETA PARA A ESQUERDA", font, 30, preto)
        move_left = text_format("DIREITA - SETA PARA A DIREITA", font, 30, preto)
        select_option = text_format("SELECIONAR OPCAO - BARRA DE ESPACO / ENTER", font, 30, preto)

        title_rect=title.get_rect()
        explicacao_rect = explicacao.get_rect()
        up_rect = move_up.get_rect()
        right_rect = move_right.get_rect()
        left_rect = move_left.get_rect()
        select_rect = select_option.get_rect()

        #posicao do texto
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(explicacao, (screen_width/2 - (explicacao_rect[2]/2), 200))
        screen.blit(move_up, (screen_width/2 - (up_rect[2]/2), 300))
        screen.blit(move_left, (screen_width/2 - (left_rect[2]/2), 360))
        screen.blit(move_right, (screen_width/2 - (right_rect[2]/2), 420))
        screen.blit(select_option, (screen_width/2 - (select_rect[2]/2), 480))

        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Jumpy")

#ecra da leaderboard
def leaderboard():

    scores = mostrarDados()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
               if event.key == K_ESCAPE:
                   return "menu"
               
        screen.fill(cor_fundo)

        #texto
        title=text_format("LEADERBOARD", font, 60, cor_titulo)
        text_colunas = text_format("USERNAME      MOEDAS        TEMPO", font, 30, preto)

        title_rect=title.get_rect()
        colunas_rect = text_colunas.get_rect()
        
        count = 0

        for line in scores:
            count += 1
            text_count = text_format(str(count), font, 30, preto)
            text_username = text_format(str(line[1]), font, 30, preto)
            text_coins = text_format(str(line[2]), font, 30, preto)
            text_time = text_format(str(line[3]), font, 30, preto)
            screen.blit(text_count, (350, 200+35*count))
            screen.blit(text_username, (420, 200+35*count))
            screen.blit(text_coins, (625, 200+35*count))
            screen.blit(text_time, (825, 200+35*count))

        #posicao do texto
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_colunas, (screen_width/2 - (colunas_rect[2]/2), 150))

        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Jumpy")


#ecra para pedir o username ao jogador
def pedir_username():

    username = ""

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    username = username[:-1]
                elif event.key == K_RETURN:
                    if len(username) > 2:
                        return username
                else:
                    if len(username) < 10 and event.unicode.isalpha():
                        username += event.unicode

        screen.fill(cor_fundo)
        title=text_format("USERNAME", font, 60, cor_titulo)
        username_text = text_format(username, font, 50, preto)

        title_rect=title.get_rect()
        username_rect = username_text.get_rect()

        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(username_text, (screen_width/2 - (username_rect[2]/2), 200))

        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Jumpy")

#ecra para quando se perde o jogo
def game_over():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
               if event.key == K_SPACE or event.key == K_RETURN:
                   return
               
        screen.fill(cor_fundo)

        #texto
        title=text_format("GAME OVER", font, 60, cor_titulo)
        back_text = text_format("PRESSIONE BARRA DE ESPACOS OU ENTER PARA VOLTAR AO MENU", font, 30, preto)

        title_rect=title.get_rect()
        back_rect = back_text.get_rect()
        #posicao do texto
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(back_text, (screen_width/2 - (back_rect[2]/2), 300))

        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Jumpy")


#ecra com o jogo
def jogo():
    
    global time
    global coins
    global jogo_correndo

    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
               if event.key == K_ESCAPE:
                   return "menu"
        
        screen.blit(background, (0,0))

        
        time = pygame.time.get_ticks() - start_time
        final_time = int(time/1000)
        time_text = text_format(str(final_time), font, 40, preto)
        time_rect = time_text.get_rect()

        
        coins, state = level.run()

        if state == "win":
            jogo_correndo = False
            username = pedir_username()
            inserirDados(username, coins, final_time)
            return "leaderboard"
        if state =="lose":
            jogo_correndo = False
            game_over()
            return "menu"

        screen.blit(time_text, (screen_width - time_rect[2]*2, 0))

        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Jumpy")

  

#game loop
while True:
    if selection == "menu":
        if jogo_correndo == False:
            selection = main_menu()
        else:
            selection = menu_pausa()
    if selection == "jogar_reset":
        level = Level(mapa1, screen)
        start_time = pygame.time.get_ticks()
        jogo_correndo = True
        selection = jogo()
    if selection == "jogar_continue":
        jogo_correndo = True
        start_time = pygame.time.get_ticks() - time
        selection = jogo()
    if selection == "instrucoes":
        selection = instrucoes()
    if selection == "leaderboard":
        selection = leaderboard()
    if selection == "quit":
        pygame.quit()
        quit()


