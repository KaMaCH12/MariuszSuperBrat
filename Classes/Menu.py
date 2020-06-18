import pygame

class Menu:
    def __init__(self,wsize):
        self.surface = pygame.display.set_mode((wsize[0], wsize[1]))
        pygame.display.set_caption('Mariusz Super Brat')

    def text_sufrace(self,text, font,color):
        white = (255, 255, 255)
        surf = pygame.Surface(font.size(text))
        surf.fill(white)
        textSurface = font.render(text, True, color, surf)
        return textSurface

    def next_state(self):
        return self.next_s

    def draw(self,screen):
        clock = pygame.time.Clock()

        background = pygame.image.load("Assets/main_menu_bg.png")
        titleText = pygame.font.Font("Assets/pcsenior.ttf", 35)
        buttonText = pygame.font.Font("Assets/pcsenior.ttf", 15)
        title =       [pygame.Rect(100, 100, 600, 100),(0,0,0), self.text_sufrace("Mariusz Super Brat", titleText, (0,96,128))]
        game_button = [pygame.Rect(300, 300, 200, 50), (0,0,0), self.text_sufrace("Start game", buttonText, (0,128,0))]
        quit_button = [pygame.Rect(300, 400, 200, 50), (0,0,0), self.text_sufrace("Quit game", buttonText, (0,128,0))]

        handle=True
        while handle:
            self.surface.blit(background,(0,0))
            for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.locals.QUIT:
                    handle=False
                    return 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button==1: #Check if it's the LMB
                        if game_button.get_rect().collidepoint(event.pos):
                            #Game button is pressed
                        if quit_button.get_rect().collidepoint(event.pos):
                            #Quit button is pressed
            game_button[2] = self.text_sufrace("Start game", buttonText, game_button[1])
            quit_button[2] = self.text_sufrace("Quit game", buttonText, quit_button[1])
            pygame.draw.rect(self.surface, game_button[1], game_button[0], 5)
            pygame.draw.rect(self.surface, quit_button[1], quit_button[0], 5)
            screen.blit(title[2],(95,140))
            screen.blit(game_button[2], (332,316))
            screen.blit(quit_button[2], (340,416))
            screen.blit(self.surface,(0,0))

            pygame.display.update()
            clock.tick(15)

