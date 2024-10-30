from settings import *
import newspage as np


def display_screen():
    screen.fill(BLUE)
    pygame.draw.rect(screen, WHITE, (width-height*0.01-width*0.3, height*0.01, width*0.3, height*0.05))
    font = pygame.font.Font(None, int(height*0.05))
    for nums in range(len(np.news)):
        text = font.render(np.news[nums]["title"], True, WHITE)
        text_render = text.get_rect()
        text_render.center = (width*0.5, height*0.1+height*0.1*nums+y)
        screen.blit(text, text_render)
        pygame.draw.rect(screen, WHITE, (0, height*0.05+height*0.1*nums+y, width, height*0.1), int(height*0.005))


running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                y += speed
            if event.button == 5:
                y -= speed
    display_screen()
    pygame.display.update()
pygame.quit()
