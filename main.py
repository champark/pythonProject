import pygame
import sys

############################################################
# 숫자 상승 + 색조 변경
# 2023-03-16 코드
############################################################

WHITE = (255,255,255)
BLACK = (0, 0, 0)

def main():
    pygame.init()
    pygame.display.set_caption("Pygame 사용법")
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 80)
    tmr = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        tmr = tmr + 1
        col = (0, tmr % 256, 0)
        pygame.draw.rect(screen, col, [100, 100, 600, 400])

        sur = font.render(str(tmr), True, WHITE)
        screen.blit(sur, [300, 200])

        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__':
    main()