#
# Poke the Dots v2
#
# Poke the dots is a game where two dots move around on screen, bouncing off
# edges, until the dots collide with each other and the game ends. Players earn
# a score based on how long the game goes without the two dots colliding. The
# player can click on the screen at any time to teleport the two dots to random
# locations on screen.
#
# Version 1 Implements:
#  * title of game window is set to Poke the Dots
#  * two dots moving, with different visual appearances
#  * dots bouncing off edge of walls
#  * dot starting locations are randomized
#
# Version 2 Implements:
#  * detection of game over conditions
#  * display of player score
#  * game over message
#
# Version 3 implements:
#  * User interaction
import pygame
import random


# User-defined functions

def main():
   # initialize all pygame modules (some need initialization)
   pygame.init()
   # create a pygame display window
   pygame.display.set_mode((500, 400))
   # set the title of the display window
   pygame.display.set_caption('Poke the Dots v3')   
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
      self.small_dot = Dot('red', 30, [0,0], [1, 2], surface)
      self.big_dot = Dot('blue', 40, [0,0], [2, 1], surface)      
      while self.big_dot.collides(self.small_dot):
         self.small_dot.randomize()
         self.big_dot.randomize()
      
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
         if event.type == pygame.MOUSEBUTTONUP and self.continue_game : # Has there been a mouse click?
            self.handle_mouse_up()   
         if event.type == pygame.KEYDOWN:
            self.handle_key_down(event.key)
         if event.type == pygame.KEYUP:
            self.handle_key_up(event.key)
   def handle_key_down(self, key):
      # when 'a' key is pressed the dots change color 
      if key == pygame.K_a:
         self.small_dot.change_color('magenta')
         self.big_dot.change_color('orange')
   def handle_key_up(self, key):
      # when 'a' key is released the dots change color again
      if key == pygame.K_a:
         self.small_dot.change_color('red')
         self.big_dot.change_color('blue')
         
   def handle_mouse_up(self):
         self.small_dot.randomize()
         self.big_dot.randomize()

   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      
      self.surface.fill(self.bg_color) # clear the display surface first
      self.small_dot.draw()
      self.big_dot.draw()
      self.draw_score()
      if self.continue_game == False:
         self.draw_game_over()      
      pygame.display.flip() # make the updated surface appear on the display

   def draw_score(self):
      # render text to screen
      text_string = "Score: " + str(int(self.frame_counter / self.FPS))
      text_color = pygame.Color('white')        
      text_font = pygame.font.SysFont('', 72)
      text_image = text_font.render(text_string, True, text_color)
      text_pos = (0, 0)
      self.surface.blit(text_image, text_pos)

   def draw_game_over(self):
      # draws the game over text to screen
      font_size = 72
      text_string = "Game Over"
      text_color = pygame.Color('red') 
      bg_color = pygame.Color('blue')
      text_font = pygame.font.SysFont('', font_size)
      text_image = text_font.render(text_string, True, text_color, bg_color)
      text_pos = (0, self.surface.get_height() - text_image.get_height())
      self.surface.blit(text_image, text_pos)
      
   def update(self):
      # Update the game objects for the next frame.
      # - self is the Game to update
      
      self.small_dot.move()
      self.big_dot.move()
      self.frame_counter = self.frame_counter + 1

   def decide_continue(self):
      # Check and remember if the game should continue
      # - self is the Game to check
      
      if self.small_dot.collides(self.big_dot):
         self.continue_game = False


class Dot:
   # An object in this class represents a Dot that moves 
   
   def __init__(self, dot_color, dot_radius, dot_center, dot_velocity, surface):
      # Initialize a Dot.
      # - self is the Dot to initialize
      # - color is the pygame.Color of the dot
      # - center is a list containing the x and y int
      #   coords of the center of the dot
      # - radius is the int pixel radius of the dot
      # - velocity is a list containing the x and y components
      # - surface is the window's pygame.Surface object

      self.color = pygame.Color(dot_color)
      self.radius = dot_radius
      self.center = dot_center
      self.velocity = dot_velocity
      self.surface = surface
      
   def move(self):
      # Change the location of the Dot by adding the corresponding 
      # speed values to the x and y coordinate of its center
      # - self is the Dot

      # move our dot based on its velocity. If it comes in contact
      # with any of the four walls, reverse its direction of motion.
      size = self.surface.get_size()
      for index in range(0, len(size)):
         self.center[index] = (self.center[index] + self.velocity[index])
         if (self.center[index] < self.radius \
             or self.center[index] > size[index] - self.radius):
            self.velocity[index] = -self.velocity[index]
           
      '''
      # our first attempt at bouncing dots off the screen's borders.
      # left in so students can compare the two ways of doing this task
      #
      width = self.surface.get_width()
      height = self.surface.get_height()
      # left wall   
      if self.center[0] < self.radius:
         self.velocity[0] = -self.velocity[0]         
      # top wall
      if self.center[1] < self.radius:
         self.velocity[1] = -self.velocity[1]     
      # right wall
      if self.center[0] > width - self.radius:
         self.velocity[0] = -self.velocity[0]     
      # bottom wall
      if self.center[1] > height - self.radius:
         self.velocity[1] = -self.velocity[1]   
      '''
            
   def draw(self):
      # Draw the dot on the surface
      # - self is the Dot
      
      pygame.draw.circle(self.surface, self.color, self.center, self.radius)

   def distance(self, other):
      # Returns the distance (in pixels) between two dots. Uses the pythagorean theorem
      # to calculate distance between two points.
      #  self refers to the ference dot that the call is being made for
      #  other refers to the comparison dot
      a = self.center[0] - other.center[0]
      b = self.center[1] - other.center[1]
      c = (a ** 2 + b ** 2) ** (0.5)
      return c

   def collides(self, other):
      # Detects if two dots have collided with each other. Returns True if they have
      # and false otherwise
      #  self refers to the reference dot that the call is being made for
      #  other refers to the comparison dot
      
      # two dots collide if the sum of their radii is greater than their distance      
      distance = self.distance(other)
      radii_sum = self.radius + other.radius
      if radii_sum > distance:
         return True
      else:
         return False

   def randomize(self):
      # Change the dot's location to a new random position that is valid (i.e.,
      # the entire dot is visible on the screen)
      #  - self is the Dot whose location is being randomize
            
      # generate new random x and y locations
      #x = random.randint(0 + self.radius, self.surface.get_width() - self.radius)
      #y = random.randint(0 + self.radius, self.surface.get_height() - self.radius)
      #new_center = [ x, y ]
      #self.center = new_center
      
      size = self.surface.get_size()
      for index in range(0, len(size)):
         self.center[index] = random.randint(0 + self.radius, size[index] - self.radius) 
   
   def change_color(self, new_color):
      self.color = pygame.Color(new_color)
      


main()
