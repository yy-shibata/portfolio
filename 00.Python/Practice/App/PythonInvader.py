import pygame
import sys

invaders = 16
invader_list =[0] * invaders

class Cannon(pygame.sprite.Sprite):
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(name)
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 430
        self.move = 0
        self.limit_right = 592
        self.limit_left = 0
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Beam(pygame.sprite.Sprite):
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.sound_shot = pygame.mixer.Sound("shot.wav")
        self.sound_hit = pygame.mixer.Sound("hit.wav")
        self.image = pygame.image.load(name)
        self.rect = self.image.get_rect()
        self.rect.y = 430
        self.move = 0
        self.state = False
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Invader(pygame.sprite.Sprite):
    def __init__(self, name, invader_no):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(name)
        self.rect = self.image.get_rect()
        self.rect.x = 20 + invader_no % 8 * 50
        self.rect.y = 50 + int(invader_no / 8) * 50
        self.movex = 1
        self.movey = 50
        self.limit_right = 592
        self.limit_left = 0
        self.damage = False
    def draw(self, screen):
        screen.blit(self.image, self.rect)

def main():
    pygame.init()
    # TODO:スクリーンサイズを変更できるようにする フルスクリーンも可能にする
    screen = pygame.display.set_mode((640,480)) # windowの表示
    pygame.display.set_caption("Invader Style") # タイトルの表示
    score_value = 0
    gameover = False
    cannon = Cannon("cannon.png")
    beam = Beam("shot.png")
    for invader_no in range(invaders):
        invader_list[invader_no] = Invader("invader.png", invader_no)

    turn = False

    # windowの継続表示
    while True:
        screen.fill((0,0,0))
        cannon.draw(screen)
        if beam.state == True:
            beam.draw(screen)
            for invader_no in range(invaders):
                if invader_list[invader_no].damage == False:
                    invader_list[invader_no].draw(screen)
        font = pygame.font.SysFont(None, 24)
        score = font.render("SCORE : " + str(score_value), True, (255,255,255))
        score.blit(score,(20, 20))
        pygame.display.update()
        if score_value >= invaders or gameover == True:
            if score_value >= invaders:
                font = pygame.font.SysFont(None, 40)
                text = font.render("GAME CLEAR", True, (255,255,255))
            else:
                font = pygame.font.SysFont(None, 40)
                text = font.render("GAME OVER", True, (255,255,255))
            screen.blit(text, (225, 200))
            game_stop()
        pygame.time.wait(4)

        for event in pygame.event.get():
            # ×が押された場合、windowsの表示を終了する
            if event.type == pygame.QUIT:
                exit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cannon.move = -2
                if event.key == pygame.K_RIGHT:
                    cannon.move = 2
                if event.key == pygame.K_SPACE:
                    if beam.state == False:
                        beam.state = True
                        beam.sound_shot.play()
                        beam.move = -2
                        beam.rect.x = cannon.rect.x + 24
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    cannon.move = 0

        cannon.rect.x += cannon.move
        if cannon.rect.x <= cannon.limit_left:
            cannon.rect.x = cannon.limit_left
        if cannon.rect.x >= cannon.limit_right:
            cannon.rect.x = cannon.limit_right

        beam.rect.y += beam.move
        if beam.rect.y <= 0:
            beam.rect.y = 430
            beam.move = 0
            beam.state = False
            beam.kill()

        for invader_no in range(invaders):
            invader_list[invader_no].rect.x += invader_list[invader_no].movex
            if invader_list[invader_no].damage == False and (invader_list[invader_no].rect.x <= invader_list[invader_no].limit_left or invader_list[invader_no].rect.x >= invader_list[invader_no].limit_right):
                turn = True
            break

        if turn == True:
            for invader_no in range(invaders):
                invader_list[invader_no].movex = - invader_list[invader_no].movex
                invader_list[invader_no].rect.y += invader_list[invader_no].movey
                if invader_list[invader_no].damage == False and invader_list[invader_no].rect.y > 400:
                    gameover = True
            turn = False

        for invader_no in range(invaders):
            if beam.state == True and pygame.sprite.collide_rect(beam, invader_list[invader_no]) == True and invader_list[invader_no].damage == False:
                beam.sound_hit.play()
                beam.kill()
                beam.rect.y = 430
                beam.move = 0
                beam.state = False
                invader_list[invader_no].kill()
                invader_list[invader_no].damage = True
                score_value += 1

def game_stop():
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

def exit_game():
    sys.exit()

main()