import pygame
import sys

############################################################
# 이미지 출력 / 풀스크린 전환 / 되돌리기 코드
# 커밋설명이 제대로 출력되지 않아서 추가한 주석
# 2023-03-16 코드
############################################################

img_galaxy = pygame.image.load("image/galaxy.png")

def main():
    pygame.init()
    pygame.display.set_caption("pygame 사용법")
    screen = pygame.display.set_mode((960,720))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    screen = pygame.display.set_mode((960, 720), pygame.FULLSCREEN)
                if event.key == pygame.K_ESCAPE:
                    screen = pygame.display.set_mode((960, 720))

        screen.blit(img_galaxy,[0,0])
        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__':
    main()