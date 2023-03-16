import pygame
import sys

############################################################
# 이미지 출력 / 풀스크린 전환 / 되돌리기 코드
# 이미지의 회전
# 2023-03-16 코드
############################################################

img_galaxy = pygame.image.load("image/galaxy.png")
img_sship = pygame.image.load("image/starship.png")

def main():
    pygame.init()
    pygame.display.set_caption("Pygame 사용법")
    screen = pygame.display.set_mode((960,720))
    clock = pygame.time.Clock()
    ang = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    screen = pygame.display.set_mode((960,720), pygame.FULLSCREEN)
                if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                    screen = pygame.display.set_mode((960, 720))

        screen.blit(img_galaxy, [0, 0])

        ang = (ang + 1) % 360
        img_rz = pygame.transform.rotozoom(img_sship, ang, 1.0)
        x = 480 - img_rz.get_width() / 2
        y = 360 - img_rz.get_height() / 2
        screen.blit(img_rz, [x, y])

        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__':
    main()