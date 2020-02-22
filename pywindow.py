import pygame
import sys


def main():
    pygame.init()
    clock = pygame.time.Clock()
    fps = 60
    size = [200, 200]
    bg = [255, 255, 255]

    screen = pygame.display.set_mode(size)

    buttonF = pygame.Rect(50, 40, 100, 20 )
    buttonFp = pygame.Rect(50, 90, 100, 20 )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button

                if buttonF.collidepoint(mouse_pos):
                    # prints current location of mouse
                    print('buttonF was pressed at {0}'.format(mouse_pos))
                if buttonFp.collidepoint(mouse_pos):
                    # prints current location of mouse
                    print('buttonFp was pressed at {0}'.format(mouse_pos))

        screen.fill(bg)

        pygame.draw.rect(screen, [0, 0, 0], buttonF)
        pygame.draw.rect(screen, [0, 0, 0], buttonFp)# draw button

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    sys.exit

if __name__ == '__main__':
    main()
