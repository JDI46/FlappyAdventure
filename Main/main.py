import pygame

def run_game():
    pygame.init()
    home_screen = pygame.display.set_mode((1280, 720))
    run_game = True

    while run_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        home_screen.fill("blue")


        pygame.display.flip()

    
    pygame.quit()


run_game()