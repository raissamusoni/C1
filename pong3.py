# Pong 1
# 
# Pong is a two-player game. Left player controls the left paddle by
# pressing the 'q' key to move upwards and 'a' key to move downwards.
# Right player controls the right paddle, pressing 'p' to move upwards,
# and 'l' to move downwards. The players move the paddles, to prevent a ball 
# from bouncing off their respective walls.
# Otherwise the other player earns a point. Game ends when a score reaches
# 11.
#
# Version 1 implementations:
# * display ball and both paddles - DONE !
# * ball bounces from window edges - DONE !
# * ball goes through - DONE !
# * paddles stay in place - DONE !
# * no score is kept - DONE !
# * game ends only when player closes window - DONE ! 
#
# Version 2 implementations:
# * score is updated/kept - DONE !
# * game ends when a score reaches 11 - DONE !
# * ball bounces off front side of each paddle & goes through back side - DONE ! 
#
# Version 3 implementations: 
# * game responds to players moving paddles - DONE !
# * game responds to key being held down - DONE !
#
# Some of the source code contained in this program is not original. It was borrowed from:
# https://stackoverflow.com/questions/33426238/how-to-make-paddles-move-in-pygame-pong
# used to understand how collidepoint works 


import pygame


# User-defined functions

def main():
    # initialize all pygame modules (some need initialization)
    pygame.init()
    # create a pygame display window
    pygame.display.set_mode((500, 400))
    # set the title of the display window
    pygame.display.set_caption('Pong v3')   
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
        obj_color = 'white'
        xpos = self.surface.get_width() * .5
        ypos = self.surface.get_height() * .5
        center = [int(xpos), int(ypos)]
        small_dot_radius = 6
        self.small_dot = Dot(obj_color, small_dot_radius, center, [5, 2], self.surface)
        
        pygame.key.set_repeat(20, 20)
        
        height = 40
        width = 10
        x_offset = self.surface.get_width() - width
        rect_left = x_offset * .25
        rect_right = (x_offset + width) * .75
        self.rect_top = (self.surface.get_height() - height) * 1/2
        rect_width = width
        rect_height = height
        self.rect_color = pygame.Color('white') 
        self.lrect_params = pygame.Rect(rect_left, self.rect_top, rect_width, rect_height)
        self.rrect_params = pygame.Rect(rect_right, self.rect_top, rect_width, rect_height)        
        
        
        self.score1 = 0
        self.score2 = 0       
        
        self.max_frames = 1000
        self.frame_counter = 0
    
    

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

            if event.type == pygame.KEYDOWN and self.continue_game:
                self.handle_keydown(event.key)
    
    def handle_keydown(self, key):
        height = self.surface.get_height()
        steps = 10
        tborder = 0
        lborder = height - 40
        if key == pygame.K_q:
            self.lrect_params.top = self.lrect_params.top - steps
            if self.lrect_params.top <= tborder:
                self.lrect_params.top = tborder            
        if key == pygame.K_p:
            self.rrect_params.top = self.rrect_params.top - steps
            if self.rrect_params.top <= tborder:
                self.rrect_params.top = tborder            
        if key == pygame.K_a:
            self.lrect_params.top = self.lrect_params.top + steps
            if self.lrect_params.top >= lborder:
                self.lrect_params.top = lborder            
        if key == pygame.K_l:
            self.rrect_params.top = self.rrect_params.top + steps
            if self.rrect_params.top >= lborder:
                self.rrect_params.top = lborder             

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw

        self.surface.fill(self.bg_color) # clear the display surface first
        self.small_dot.draw()
        pygame.draw.rect(self.surface, self.rect_color, self.lrect_params)
        pygame.draw.rect(self.surface, self.rect_color, self.rrect_params)        
        
        self.draw_lscore()
        self.draw_rscore()
        
        pygame.display.update() # make the updated surface appear on the display
    
    def collides(self):
        # want to make a border where collides applies (only between 135<x<375)
        # while ball bounces in this border - bouncing back happens when colliding
        # while ball bounces outside of this border, bounce thru when colliding        
        center = self.small_dot.center
        self.velocity = self.small_dot.velocity
                
        if self.rrect_params.collidepoint(center) and self.velocity[0] > 0:
            self.velocity[0] = -self.velocity[0]
          
        
        if self.lrect_params.collidepoint(center) and self.velocity[0] < 0:
            self.velocity[0] = -self.velocity[0]
    
    def get_scorel(self):
        width = self.small_dot.surface.get_width()
        if self.small_dot.center[0] < self.small_dot.radius:
            self.score1 = self.score1 + 1/2
        return self.score1

    def get_scorer(self):
        width = self.small_dot.surface.get_width()
        if self.small_dot.center[0] > width - self.small_dot.radius:
            self.score2 = self.score2 + 1/2
        return self.score2      
    
    def draw_lscore(self):
    # render text to screen
        self.score1 = self.get_scorel() 
        text_string = str(int(self.score1))
        text_color = pygame.Color('white')        
        text_font = pygame.font.SysFont('', 72)
        text_image = text_font.render(text_string, True, text_color)
        text_pos = (0, 0)
        self.surface.blit(text_image, text_pos)
    
    def draw_rscore(self):
    # render text to screen
        self.score2 = self.get_scorer()
        text_string = str(int(self.score2))          
        text_color = pygame.Color('white')        
        text_font = pygame.font.SysFont('', 72)
        text_image = text_font.render(text_string, True, text_color)
        text_pos = (self.surface.get_width() - text_image.get_width(), 0)
        self.surface.blit(text_image, text_pos)    

    def update(self):
        # Update the game objects for the next frame.
        # - self is the Game to update

        self.small_dot.move() 
        self.collides()
    
        self.frame_counter = self.frame_counter + 1
        self.score1 = self.get_scorel()
        self.score2 = self.get_scorer()
        

    def decide_continue(self):
        # Check and remember if the game should continue
        # - self is the Game to check

        self_continue = True
        while self.score1 >= 11 or self.score2 >= 11:
            self.continue_game = False        

class Dot:
    # An object in this class represents a Dot/Ball that moves 

    def __init__(self, obj_color, dot_radius, dot_center, dot_velocity, surface):
        # Initialize a Dot.
        # - self is the Dot to initialize
        # - color is the pygame.Color of the dot
        # - center is a list containing the x and y int
        #   coords of the center of the dot
        # - radius is the int pixel radius of the dot
        # - velocity is a list containing the x and y components
        # - surface is the window's pygame.Surface object

        self.color = pygame.Color(obj_color)
        self.radius = dot_radius
        self.center = dot_center
        self.velocity = dot_velocity
        self.surface = surface
         
           

    def move(self):
        # Change the location of the Dot by adding the corresponding 
        # speed values to the x and y coordinate of its center
        # - self is the Dot

        size = self.surface.get_size()
        for index in range(0,len(size)):
            self.center[index] = (self.center[index] + self.velocity[index])
            if self.center[index] < self.radius \
                or self.center[index] > size[index] - self.radius:   
                self.velocity[index] = -self.velocity[index]        

    def draw(self):
        # Draw the dot on the surface - self is the Dot

        pygame.draw.circle(self.surface, self.color, self.center, self.radius)
        #pygame.draw.rect(self.surface, self.color, self.params)
    
    

main()
