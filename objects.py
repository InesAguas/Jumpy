import pygame

img = [pygame.image.load("Imagens/Coin/goldCoin1.png"),
        pygame.image.load("Imagens/Coin/goldCoin2.png"),
        pygame.image.load("Imagens/Coin/goldCoin3.png"),
        pygame.image.load("Imagens/Coin/goldCoin4.png"),
        pygame.image.load("Imagens/Coin/goldCoin5.png"),
        pygame.image.load("Imagens/Coin/goldCoin6.png"),
        pygame.image.load("Imagens/Coin/goldCoin7.png"),
        pygame.image.load("Imagens/Coin/goldCoin8.png"),
        pygame.image.load("Imagens/Coin/goldCoin9.png")]

class Moeda(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__() 
        self.image = img[0]
        self.rect = self.image.get_rect(topleft = pos)
        self.frame = 0

    def update(self):
        if(self.frame > 40):
            self.frame = 0
        self.image = img[int(self.frame/5)]
        self.frame += 1

class Key(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("Imagens/key.png"), (30,30))
        self.rect = self.image.get_rect(topleft = pos)
        self.caught = False

class Door(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__() 
        self.image = pygame.image.load("Imagens/door.closed.png")
        self.rect = self.image.get_rect(topleft = pos)

ground = pygame.image.load("Imagens/brick1.png")
class Tile(pygame.sprite.Sprite):
    def __init__(self,pos, size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.blit(ground, (0,0))
        self.rect = self.image.get_rect(topleft = pos)

trap = pygame.image.load("Imagens/trap.png")
class Trap(pygame.sprite.Sprite):
    def __init__(self, pos, side):
        super().__init__() 
        if side == "up":
            self.image = trap
        if side == "down":
            self.image = pygame.transform.rotate(trap, 180)
        if side == "left":
            self.image = pygame.transform.rotate(trap, 90)
        if side == "right":
            self.image = pygame.transform.rotate(trap, -90)
        self.rect = self.image.get_rect(topleft = pos)
