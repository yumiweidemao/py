import pygame
from pygame.locals import *
from classes import Chess

#initialize game variables
game_active = 0
anti_aliasing = 0
font_size = 26
now_playing = "X"
mode = None
board = [[0 for _ in range(3)] for _ in range(3)]

def main():
    global board
    global now_playing

    #initialize pygame module
    pygame.init()

    #initialize screen
    screen = pygame.display.set_mode((600, 300))
    pygame.display.set_caption("Tic Tac Toe")

    #initialize background
    background = pygame.Surface(screen.get_size())
    background = background.convert()  
    background.fill((100, 200, 150))

    #draw the board onto surface
    pygame.draw.line(background, (0, 80, 0), (260, 30), (260, 270), 5)
    pygame.draw.line(background, (0, 80, 0), (340, 30), (340, 270), 5)
    pygame.draw.line(background, (0, 80, 0), (180, 110), (420, 110), 5)
    pygame.draw.line(background, (0, 80, 0), (180, 190), (420, 190), 5)

    #draw buttons onto surface
    button_rect1 = pygame.draw.rect(background, (80, 150, 80), (25, 60, 95, 40))
    button_rect2 = pygame.draw.rect(background, (80, 150, 80), (25, 130, 95, 40))

    #display button text
    font = pygame.font.Font(None, font_size)
    text1 = font.render("PvP", anti_aliasing, (30, 30, 30))
    text1_pos = text1.get_rect()
    text1_pos.centerx = button_rect1.centerx
    text1_pos.centery = button_rect1.centery
    background.blit(text1, text1_pos)

    text2 = font.render("vs. AI", anti_aliasing, (30, 30, 30))
    text2_pos = text2.get_rect()
    text2_pos.centerx = button_rect2.centerx
    text2_pos.centery = button_rect2.centery
    background.blit(text2, text2_pos)

    #blit onto screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    #main loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == MOUSEBUTTONDOWN:
                # only care for left mouse button
                if event.button == 1:
                    chess = Chess(now_playing)
                    board = chess.update_board(background, event.pos, board)
                    print(board)
                    # switch turn
                    now_playing = "X" if now_playing == "O" else "O"
            elif event.type == MOUSEMOTION:
                mouse_pos = event.pos
                # check if mouse is on any button, update button color
                update_button_color(mouse_pos, background, text1_pos, text2_pos, font)

        #update screen
        screen.blit(background, (0, 0))
        pygame.display.flip()

def update_button_color(mouse_pos, background, text1_pos, text2_pos, font):
    """ updates the button color if mouse is hovering the button """
    mouse_x, mouse_y = mouse_pos
    if 25 <= mouse_x <= 120 and 60 <= mouse_y <= 100:
        # mouse hovering button 1
        text1 = font.render("PvP", anti_aliasing, (250, 250, 250))
    else:
        # mouse not hovering button 1
        text1 = font.render("PvP", anti_aliasing, (30, 30, 30))
    background.blit(text1, text1_pos)

    if 25 <= mouse_x <= 120 and 130 <= mouse_y <= 170:
        # mouse hovering button 2
        text2 = font.render("vs. AI", anti_aliasing, (250, 250, 250))
    else:
        # mouse not hovering button 2
        text2 = font.render("vs. AI", anti_aliasing, (30, 30, 30))
    background.blit(text2, text2_pos)

def select_mode(mouse_pos):
    mouse_x, mouse_y = mouse_pos 

if __name__ == "__main__":
    main()
