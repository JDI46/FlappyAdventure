import pygame

def run_game():
    pygame.init()
    home_screen = pygame.display.set_mode((1280, 720))
    home_screen = pygame.display.set_mode((1060, 600))
    run_game = True

    background = True
    surface = True
    font = True
    text = True
    get_text_pos = True
    
    while run_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        home_screen.fill("blue")


        pygame.display.flip()


    pygame.quit()
