import pygame
import random

class Chess(pygame.sprite.Sprite):
    
    def __init__(self, type):
        super().__init__()

        #determine whether it's an 'X' or 'O'
        self.type = type
        self.image = pygame.Surface((70, 70))
        self.image.fill((100, 200, 150))
        self.rect = self.image.get_rect()

        #draw 'X' or 'O' on surface
        if self.type == "O":
            pygame.draw.circle(self.image, color=(250, 250, 250),
                            center=(35, 35), radius=28, width=8)
        elif self.type == "X":
            pygame.draw.line(self.image, (15, 15, 15), (13, 10), (57, 60), 11)
            pygame.draw.line(self.image, (15, 15, 15), (57, 10), (13, 60), 11)
    
    def update_board(self, surface, mouse_pos, board):
        """
            Display chess on board according to mouse click position.
        """
        mouse_x, mouse_y = mouse_pos
        valid = 0

        # first column
        if 180 <= mouse_x <= 260:
            self.rect.centerx = 220
            if 30 <= mouse_y <= 110:
                # board[0][0]
                self.rect.centery = 70
                if board[0][0] == 0:
                    board[0][0] = self.type
                    valid = 1
            elif 110 <= mouse_y <= 190:
                # board[1][0]
                self.rect.centery = 150
                if board[1][0] == 0:
                    board[1][0] = self.type
                    valid = 1
            elif 190 <= mouse_y <= 270:
                # board[2][0]
                self.rect.centery = 230
                if board[2][0] == 0:
                    board[2][0] = self.type
                    valid = 1
        
        # second column
        elif 260 <= mouse_x <= 340:
            self.rect.centerx = 300
            if 30 <= mouse_y <= 110:
                # board[0][1]
                self.rect.centery = 70
                if board[0][1] == 0:
                    board[0][1] = self.type
                    valid = 1
            elif 110 <= mouse_y <= 190:
                # board[1][1]
                self.rect.centery = 150
                if board[1][1] == 0:
                    board[1][1] = self.type
                    valid = 1
            elif 190 <= mouse_y <= 270:
                # board[2][1]
                self.rect.centery = 230
                if board[2][1] == 0:
                    board[2][1] = self.type
                    valid = 1

        # third column
        elif 340 <= mouse_x <= 420:
            self.rect.centerx = 380
            if 30 <= mouse_y <= 110:
                # board[0][2]
                self.rect.centery = 70
                if board[0][2] == 0:
                    board[0][2] = self.type
                    valid = 1
            elif 110 <= mouse_y <= 190:
                # board[1][2]
                self.rect.centery = 150
                if board[1][2] == 0:
                    board[1][2] = self.type
                    valid = 1
            elif 190 <= mouse_y <= 270:
                # board[2][2]
                self.rect.centery = 230
                if board[2][2] == 0:
                    board[2][2] = self.type
                    valid = 1
        
        else:
            return board, valid

        # update graphics only if the move is valid
        if valid:
            surface.blit(self.image, self.rect)

        return board, valid

class AI():
    def __init__(self):
        self.type = "O"
    
    def play(self, background, board):
        """ 
            AI makes a move on the board. Returns the modified board. Graphically 
            updates the screen as well.
        """

        # AI algorithm
        is_full = True
        possible_moves = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    is_full = False
                    possible_moves.append((i, j))
        
        # board full, make no move
        if is_full:
            return board
        
        # otherwise, randomly choose a move
        y, x = random.choice(possible_moves)
        
        # calculate mouse position
        mouse_x = 220 + 80 * x
        mouse_y = 70 + 80 * y
        mouse_pos = (mouse_x, mouse_y)

        # create a chess object to play move
        chess = Chess(self.type)
        board, _ = chess.update_board(background, mouse_pos, board)

        return board
