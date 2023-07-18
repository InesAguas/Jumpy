import pygame
from mapa import tile_size, screen_width, screen_height
from player import Player
from objects import Moeda, Key, Door, Tile, Trap

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
    
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.moedas = pygame.sprite.Group()
        self.key = pygame.sprite.GroupSingle()
        self.door = pygame.sprite.GroupSingle()
        self.traps = pygame.sprite.Group()
        
        self.moedas_apanhadas = 0
        self.door_open = False
        self.game_state = ""

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'X':
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
                if cell == 'C':
                    moeda = Moeda((x,y))
                    self.moedas.add(moeda)
                if cell == 'D':
                    door_sprite = Door((x,y-30))
                    self.door.add(door_sprite)
                if cell == 'K':
                    key_sprite = Key((x,y))
                    self.key.add(key_sprite)
                if cell == '1':
                    trap_sprite = Trap((x,y), "down")
                    self.traps.add(trap_sprite)
                if cell == '2':
                    trap_sprite = Trap((x,y+15), "up")
                    self.traps.add(trap_sprite)
                if cell == '3':
                    trap_sprite = Trap((x+15,y), "left")
                    self.traps.add(trap_sprite)
                if cell == '4':
                    trap_sprite = Trap((x,y), "right")
                    self.traps.add(trap_sprite)
        
        
    def limit(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        
        if player_x < 32 and direction_x < 0:
            player.speed = 0
        elif player_x > screen_width-32 and direction_x > 0:
            player.speed = 0
        else:
            player.speed = 13

    def h_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed #movimento no eixo x
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                #se o player estiver a andar para a esquerda... a colisão ocorre na esquerda
                if player.direction.x < 0: 
                    player.rect.left = sprite.rect.right
                    
                #se o player estiver a andar para a direita... a colisão ocorre na direita
                if player.direction.x > 0: 
                    player.rect.right = sprite.rect.left
    
    def v_collision(self):
        player = self.player.sprite
        player.gravity_mov()
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):

                if player.direction.y > 0: 
                    player.rect.bottom = sprite.rect.top
                    #sem esta linha, a gravidade vai aumentando, até que o player simplesmente cai e desaparece
                    player.direction.y = 0
                    
                if player.direction.y < 0: 
                    player.rect.top = sprite.rect.bottom  
                     #sem esta linha, o player ao bater na parte de baixo de uma plataforma, demora a cair
                    #player.direction.y = 0  

    def coin_catch(self):
        for moeda in self.moedas:
            if moeda.rect.colliderect(self.player.sprite.rect):
                self.moedas.remove(moeda)  
                self.moedas_apanhadas += 1   

    def key_catch(self):
        for key in self.key:
            if key.rect.colliderect(self.player.sprite.rect):
                self.key.remove(key)
                self.door.sprite.image = pygame.image.load("Imagens/door.open.png")
                self.door_open = True
    
    def enter_door(self):
        for door in self.door:
            if door.rect.colliderect(self.player.sprite.rect) and self.door_open == True:
                self.game_state = "win"
    
    def fall(self):
        if(self.player.sprite.rect.top > screen_height):
            self.game_state = "lose"
    
    def trap_collision(self):
        for trap in self.traps:
            if trap.rect.colliderect(self.player.sprite.rect):
                self.game_state = "lose"
                    
    def run(self):
        self.tiles.draw(self.display_surface)
        self.limit()
        
        self.moedas.update()
        self.player.update()
        self.h_collision()
        self.v_collision()
        self.coin_catch()
        self.key_catch()
        self.enter_door()
        self.fall()
        self.trap_collision()
        self.traps.draw(self.display_surface)
        self.key.draw(self.display_surface)
        self.door.draw(self.display_surface)
        self.moedas.draw(self.display_surface)
        self.player.draw(self.display_surface)
        

        return self.moedas_apanhadas, self.game_state
        