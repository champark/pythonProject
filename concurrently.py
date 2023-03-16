import pygame
import sys

############################################################
# 여러버튼이 동시에 눌러졌을때의 처리
# 여러 버튼을 동시에 클릭했을 때의 반응처리
# 2023-03-16 코드
############################################################

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def main():
    pygame.init()
    pygame.display.set_caption("Pygame 사용법")
    screen = pygame.display.set_mode((960, 720))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 80)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        key = pygame.key.get_pressed()
        txt1 = font.render("UP{} DOWN{}".format(key[pygame.K_UP], key[pygame.K_DOWN]), True, WHITE, GREEN)
        txt2 = font.render("LEFT{} RIGHT{}".format(key[pygame.K_LEFT],key[pygame.K_RIGHT]), True, WHITE, BLUE)
        txt3 = font.render("SPACE{} Z{}".format(key[pygame.K_SPACE], key[pygame.K_z]), True, WHITE, RED)
        screen.blit(txt1, [100, 100])
        screen.blit(txt2, [100, 200])
        screen.blit(txt3, [100, 300])

        pygame.display.update()
        clock.tick(10)

if __name__ == "__main__":
    main()