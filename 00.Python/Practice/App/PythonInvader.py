import pygame
import sys

class Cannon(pygame.sprite.Sprite):
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(name)
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 400
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

def main():
    pygame.init()
    # TODO:スクリーンサイズを変更できるようにする フルスクリーンも可能にする
    screen = pygame.display.set_mode((640,480)) # windowの表示
    pygame.display.set_caption("Invader Style") # タイトルの表示
    cannon = Cannon("cannon.png")

    # windowの継続表示
    while True:
        cannon.draw(screen)
        pygame.display.update()
        for event in pygame.event.get():
            # ×が押された場合、windowsの表示を終了する
            if event.type == pygame.QUIT:
                exit_game()

def exit_game():
    sys.exit()

main()