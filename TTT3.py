# Version 1 implementations:
# * graphical window with 3x3 grid - DONE !
# * exit when 'X' is clicked - DONE !
#
# Version 2 implementations:
# * two player game - DONE ! 
# * change of turns, X and O appears - DONE ! 
# * flashing when clicking on occupied tile - DONE ! 
# * drawing out the content centered inside tile - DONE !
#
# Version 3 implementations: 
# * end of game conditions



import pygame
import random
# User-defined functions

def main():
    # initialize all pygame modules (some need initialization)
    pygame.init()
    # create a pygame display window
    pygame.display.set_mode((500, 400))
    # set the title of the display window
    pygame.display.set_caption('Tic Tac Toe')   
    # get the display surface
    w_surface = pygame.display.get_surface() 
    # create a game object
    game = Game(w_surface)
    # start the main game loop by calling the play method on the game object
    game.play() 
    # quit pygame and clean up the pygame window
    pygame.quit() 


# User-defined classes

class Game:
    # An object in this class represents a complete game.

    def __init__(self, surface):
        # Initialize a Game.
        # - self is the Game to initialize
        # - surface is the display window surface object

        # === objects that are part of every game that we will discuss
        self.surface = surface
        self.bg_color = pygame.Color('black')

        self.FPS = 60
        self.game_Clock = pygame.time.Clock()
        self.close_clicked = False
        self.continue_game = True

        # === game specific objects
        # CALL to the class method to set the surface for the Tile objects
        # format: <name of the class>.<name of the class method>(<argument>)
        Tile.set_surface(self.surface)
        self.board_size = 3
        self.flashers = []
        self.filled = []
        self.board = []
        self.create_board()
        self.player_1 = 'X'
        self.player_2 = 'O'
        self.turn = self.player_1
    
    def create_board(self):
        width = self.surface.get_width()//self.board_size
        height = self.surface.get_height()//self.board_size
        for row_index in range(0,self.board_size):
            row = []
            for col_index in range(0,self.board_size):
                # item = (row_index, col_index)
                # replace item with a Tile object
                x = width * col_index
                y = height * row_index
                tile = Tile(x,y,width,height)
                row.append(tile)
            self.board.append(row)

    def play(self):
        # Play the game until the player presses the close box.
        # - self is the Game that should be continued or not.

        while not self.close_clicked:  # until player clicks close box
            # play frame
            self.handle_events()
            self.draw()            
            if self.continue_game:
                self.update()
                self.decide_continue()
            self.game_Clock.tick(self.FPS) # run at most with FPS Frames Per Second 

    def handle_events(self):
        # Handle each user event by changing the game state appropriately.
        # - self is the Game whose events will be handled

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True
            if event.type == pygame.MOUSEBUTTONUP and self.continue_game:
                self.handle_mouse_up(event.pos)
    
                def a():
                    print("A")
                    return True
    def handle_mouse_up(self, position):
        # position is the (x,y) location of the click and is of type tuple
        for row in self.board:
            for tile in row:
                if tile.select(position, self.turn) == True: # click inside an unoccupied tile
                    self.filled.append(tile)
                    self.change_turn()
    def change_turn(self):
        if self.turn == self.player_1:
            self.turn = self.player_2
        else:
            self.turn = self.player_1
                    
    
    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw

        self.surface.fill(self.bg_color) # clear the display surface first
        if self.continue_game == False:
            tile = random.choice(self.flashers)
            tile.set_flashing_on()
        # Have to draw the grid here
        for row in self.board:
            for tile in row:
                tile.draw()
        
        pygame.display.update() # make the updated surface appear on the display

    def update(self):
        # Update the game objects for the next frame.
        # - self is the Game to update
        pass


    def is_same(self, list_of_tiles):
        # list_of_tiles is a list of 3 Tile object
        first = list_of_tiles[0] # bound to the first Tile object
        index = 1
        same = True
        while index < len(list_of_tiles) and same: 
            same = list_of_tiles[index].is_equal(first)
            index = index + 1
        if same == True:
            self.flashers = list_of_tiles
        return same
    
    def is_diagonal_win(self):
        diagonal_win = False
        red_diagonal = []
        green_diagonal = []
        for index in range(0, self.board_size):
            tile = self.board[index][index]
            red_diagonal.append(tile)
            tile = self.board[index][self.board_size-index-1]
            green_diagonal.append(tile)
        if self.is_same(red_diagonal) or self.is_same(green_diagonal):
            diagonal_win = True
        return diagonal_win            
    
    def is_column_win(self):
        column_win = False
        for col_index in range(0,self.board_size):
            column = []
            for row_index in range(0,self.board_size):
                tile = self.board[row_index][col_index]
                column.append(tile)
            if self.is_same(column) == True:
                column_win = True
        return column_win
    
    def is_row_win(self):
        row_win = False
        for row in self.board:
            if self.is_same(row) == True:
                row_win = True
        return row_win
    
    def is_tie(self):
        tie = False
        if len(self.filled) == self.board_size**2:
            tie = True
            self.flashers = self.filled
        return tie 
    
    def is_win(self):
        win = False
        if self.is_row_win() or self.is_column_win() or self.is_diagonal_win():
            win = True
        return win
    
    def decide_continue(self):
        # Check and remember if the game should continue
        # - self is the Game to check
        # lazy evaluation: short circuit evaluation: it is important to check
        # for the win before the tie, because ORDER matters in this game
        # if we have a win and a tie.. the win supersedes the tie
        # so check for win first 

        if self.is_win() or self.is_tie():
            self.continue_game = False


class Tile:
    # Class attributes are attributes that are same for all Tile objects - all of them goes here
    # when we don't know the value of the attributes - we have to create it: classmethod 
    surface = None # for example; this surface does not have a value YET, we have to create it
    border_width = 3
    border_color = pygame.Color('white')
    font_size = 133
    
    # decorator '@' classmethod --> any method that follows one, is considered a class method
    # a class method is used to set or change the value of a class attribute
    @classmethod
    def set_surface(cls, surface_from_Game):
        # -cls is a parameter gets bound to the name of the class which is Tile
        # -surface_from_Game get bound to the object the argument self.surface is bound to
        cls.surface = surface_from_Game
    
    # Instance methods/Attributes - all of them have to be listed in init
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.content = ''
        self.flashing = False
    
    def set_flashing_on(self):
        self.flashing = True
        
        
    def is_equal(self, other_tiles):
        if self.content != '' and self.content == other_tiles.content:
            return True
        else:
            return False
    
    def draw(self):
        # a black rectangle with 3 pixel white border
        if self.flashing == True:
            # draw a white rectangle
            pygame.draw.rect(Tile.surface, Tile.border_color, self.rect)
            self.flashing = False
        else:
            # draw a black rectangle with 3 pixel white boarder
            pygame.draw.rect(Tile.surface, Tile.border_color, self.rect, Tile.border_width)            
            self.draw_content()
    def draw_content(self):
        # size, color, location
        font = pygame.font.SysFont('',Tile.font_size)
        # render the font object
        text_box = font.render(self.content, True, Tile.border_color)
        # location - top left corner of the text_box
        text_box_width = text_box.get_width()
        text_box_height = text_box.get_height()
        d_x = (self.rect.width - text_box_width)//2
        d_y = (self.rect.height - text_box_height)//2
        x = self.rect.x + d_x
        y = self.rect.y + d_y
        location = (x,y)
        Tile.surface.blit(text_box, location)
        
    def select(self,position, current_player):
        valid_click = False
        if self.rect.collidepoint(position):
            if self.content == '':
                self.content = current_player
                valid_click = True
            else:
                self.flashing = True
        return valid_click
                
                
            

main()