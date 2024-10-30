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


def display_article():
    screen.fill(BLUE)
    font = pygame.font.Font(None, int(height * 0.05))
    text = font.render(str(np.news[title]["title"]), True, WHITE)
    text_render = text.get_rect()
    text_render.center = (width*0.5, height*0.05)
    screen.blit(text, text_render)
    for nums in range(len(np.news[title]["content"])):
        if np.news[title]["content"][nums]["type"] == "text":
            print(np.news[title]["content"][nums]["value"])
    text = font.render("Das\nist\nein\nTest", True, WHITE)
    text_render = text.get_rect()
    text_render.center = (width*0.5, height*0.5)
    screen.blit(text, text_render)


def check_title():
    for nums in range(len(np.news)):
        if height*0.05+height*0.1*nums+y <= mouse_y <= height*0.05+height*0.1*nums+y+height*0.1:
            return nums
    return None


running = True
while running:
    clock.tick(FPS)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                y += speed
            if event.button == 5:
                y -= speed
            if event.button == 1 and type(check_title()) == int and title is None:
                title = check_title()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and title is not None:
                title = None
    if title is None:
        display_screen()
    else:
        display_article()
    pygame.display.update()
pygame.quit()
