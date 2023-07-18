import pygame

vermelho=(255, 0, 0)

run = [pygame.image.load("Imagens/RunR/runR1.png"),
            pygame.image.load("Imagens/RunR/runR2.png"),
            pygame.image.load("Imagens/RunR/runR3.png"),
            pygame.image.load("Imagens/RunR/runR4.png"),
            pygame.image.load("Imagens/RunR/runR5.png"),
            pygame.image.load("Imagens/RunR/runR6.png")]


idle = [pygame.image.load("Imagens/IdleR/idleR1.png"),
            pygame.image.load("Imagens/IdleR/idleR2.png"),
            pygame.image.load("Imagens/IdleR/idleR3.png"),
            pygame.image.load("Imagens/IdleR/idleR4.png"),
            pygame.image.load("Imagens/IdleR/idleR5.png"),
            pygame.image.load("Imagens/IdleR/idleR6.png"),
            pygame.image.load("Imagens/IdleR/idleR7.png"),
            pygame.image.load("Imagens/IdleR/idleR8.png"),
            pygame.image.load("Imagens/IdleR/idleR9.png")]


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__() 
        self.image = pygame.transform.scale(idle[0], (50, 50))
        self.rect = self.image.get_rect(topleft = pos)
        
        self.direction = pygame.math.Vector2(0,0)   
        self.speed = 13  
        self.gravity = 0.8
        self.jump_speed = -13
        self.jumped = 0
        self.move_frame = 0
        self.idle_frame = 0
        self.idle_direction = 0

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if pressed_keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.image = pygame.transform.flip(pygame.transform.scale(run[self.move_frame], (50,50)), True, False)
            self.move_frame += 1
            self.idle_frame = 0
            self.idle_direction = 1
        elif pressed_keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.image = pygame.transform.scale(run[self.move_frame], (50,50))
            self.move_frame += 1
            self.idle_frame = 0
            self.idle_direction = 0
        else:
            self.direction.x = 0
            if(self.idle_direction == 0):
                self.image = pygame.transform.scale(idle[int(self.idle_frame/10)], (50,50))
            if(self.idle_direction == 1):
                self.image = pygame.transform.flip(pygame.transform.scale(idle[int(self.idle_frame/10)], (50,50)), True, False)
            self.idle_frame += 1
            self.move_frame = 0
        
        if pressed_keys[pygame.K_UP] and self.jumped == 0 and self.pressed_up == False:
            self.jump()
            self.jumped = 1
            self.pressed_up = True
        if pressed_keys[pygame.K_UP] and self.jumped == 1 and self.pressed_up == False:
            self.jump()
            self.jumped = 2
            self.pressed_up = True
        if self.direction.y == 0:
            self.jumped = 0  
            self.pressed_up = False
        if pressed_keys[pygame.K_UP] == False and self.jumped == 1:
            self.pressed_up = False

                
    def gravity_mov(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
     

        
    def jump(self):
        self.direction.y = self.jump_speed
        
          
    def update(self):
        if(self.move_frame > 5):
            self.move_frame = 0
        if(self.idle_frame > 80):
            self.idle_frame = 0
        self.move()
        