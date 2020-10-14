# By Isaac Wilkey
# achived initial capabilities on Febuary 22, 2020 at 1:15 p.m. UTC -6h/MST
# "It brought tears to my eyes. I was full of joy and satisfaction due to the 
# initial functionality of my snake"-Isaac Wilkey, making fun of Sean Shin

#NEED TO DO
#   implement wall and self collision
#   figure out the double apple error and fix it
#   potetially fix the error where multiple snakes does not work
################---I_SNAKE---##################

#Normal pygame stuff
import pygame, random, time
from pygame.locals import *
pygame.init()

# colors
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)

# screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Making the screen
WINDOW_SURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('I_SNAKE')

# Directions
# Will be used to store the direction the head is going
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# Snake width and height, it sticks to a grid of 
# 20*20 squares
SNAKE_HEIGHT = 20
SNAKE_WIDTH= 20

# the speed that the snake moves each frame, for it to stick to a grid it
# should be the same as SNAKE_HEIGHT and SNAKE_WIDTH
SNAKE_SPEED = 20

# List of all the constants so it is easily imported into the class
CONSTANT_LIST = (BLACK, GREEN, RED, SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_SURFACE, UP, DOWN, LEFT, RIGHT, SNAKE_HEIGHT, SNAKE_WIDTH, SNAKE_SPEED)

# This is the class that has all the functions of snake, and is the snake
# It take a bunch of arguments to init and creates the snake, and it 
# creates a bunch of green squares and keeps track of them.
# Every frame it puts a new block in the front and covers up the on at the back
class Snake():
	
	
	#the init function, it mostly just takes the arguments and puts them into self
	def __init__(self, snake_x, snake_y, snake_start_direction, CONSTANT_LIST):
				
		# defines the head position as the starting position, 
		# it will work out that it is the same thing in the start
		self.snake_head_x = snake_x
		self.snake_head_y = snake_y
		
		# the head direction is set to starting direction
		self.head_direction = snake_start_direction
		
		# the lists that tracks positionsfor the snake body
		self.body_cord_x = [self.snake_head_x]
		self.body_cord_y = [self.snake_head_y]
		
		# the length of the snake, starts at 3
		self.snake_length = 3
		
		# CONSTANT_LIST stuff
		# it is really stupid but I cant figure out a better way to do it
		self.BLACK = CONSTANT_LIST[0]
		self.GREEN = CONSTANT_LIST[1]
		self.RED = CONSTANT_LIST[2]
		self.SCREEN_WIDTH = CONSTANT_LIST[3]
		self.SCREEN_HEIGHT = CONSTANT_LIST[4]
		self.WINDOW_SURFACE = CONSTANT_LIST[5]
		self.UP = CONSTANT_LIST[6]
		self.DOWN = CONSTANT_LIST[7]
		self.LEFT = CONSTANT_LIST[8]
		self.RIGHT = CONSTANT_LIST[9]
		self.SNAKE_HEIGHT = CONSTANT_LIST[10]
		self.SNAKE_WIDTH = CONSTANT_LIST[11]
		self.SNAKE_SPEED = CONSTANT_LIST[12]
		   
		# HUGE if web that determines were the tail spawns, which is snake_length+1 spaces behind
		# the snake, but it depends on the starting direction
		if self.head_direction == self.DOWN:
			self.snake_tail_y = self.snake_head_y + (self.SNAKE_HEIGHT * (self.snake_length+1)) 
			self.snake_tail_x = self.snake_head_x
		elif self.head_direction == UP:
			self.snake_tail_y = self.snake_head_y - (self.SNAKE_HEIGHT * (self.snake_length+1)) 
			self.snake_tail_x = self.snake_head_x			
		elif self.head_direction == LEFT:
			self.snake_tail_x = self.snake_head_x + (self.SNAKE_WIDTH * (self.snake_length+1)) 
			self.snake_tail_y = self.snake_head_y			
		else: 
			self.snake_tail_x = self.snake_head_x - (self.SNAKE_WIDTH * (self.snake_length+1)) 
			self.snake_tail_y = self.snake_head_y		 
	
	
	# Does the calculations and draws the new square for the head every
	# frame, then it adds the new head x and y to the front of the cord
	# lists, I might change it later to the back of the list, if its
	# lighter on the RAM
	def update_head(self):
		
		
		# A buch of if statements that use the direction to dictate were
		# to put the new head, copied from Josh's original Jsnake and 
		# adapted to my code, dont try reading it, its death
		if self.head_direction == self.DOWN:
			self.snake_head_y += self.SNAKE_SPEED			
		elif self.head_direction == UP:
			self.snake_head_y -= self.SNAKE_SPEED			
		elif self.head_direction == LEFT:
			self.snake_head_x -= self.SNAKE_SPEED			
		else:
			self.snake_head_x += self.SNAKE_SPEED
		
		#draws the new snake head
		pygame.draw.rect(self.WINDOW_SURFACE, self.GREEN, pygame.Rect(self.snake_head_x, self.snake_head_y, self.SNAKE_HEIGHT, self.SNAKE_WIDTH))
		
		#adds the new head cordinates to body_cord_x/y to the front of the list
		self.body_cord_x.insert(0, self.snake_head_x)
		self.body_cord_y.insert(0, self.snake_head_y)
		
	
	# The function that detects whether the snake is eating an apple, it takes
	# the apple x and y, which will be given in the main loop to the update
	# function, that is called in the main loop
	def eat_apple(self, apple_x, apple_y):
		
		
		# the if statement that decides whaether the snake is eating an apple.
		if (self.snake_head_x == apple_x) and (self.snake_head_y == apple_y):
			return True
		else:
			return False
	
	
	# The function that deals with making the new tail every frame, has the 
	# parameter is_eating_apple, that will be passed in when the function is
	# called in the main update function
	def tail_update(self, is_eating_apple):
		
		
		# The if statement that decides whether to delet the last body segment
		# make a new square for the tail or not, depending on whether is_eating_apple
		# is true
		if not is_eating_apple:
			
			# Creates the new tail cordinates to later make into a square
			if len(self.body_cord_x)>1:
				self.snake_tail_x = self.body_cord_x[-1]
				self.snake_tail_y = self.body_cord_y[-1]
			
			# Removes the last index of body_cord_x/y using the pop() method
			# without an argument it will automaticly remove the last index
			if len(self.body_cord_x)>1:
				self.body_cord_x.pop()
				self.body_cord_y.pop()
			
			# Draws the snake tail
			pygame.draw.rect(self.WINDOW_SURFACE, self.BLACK, pygame.Rect(self.snake_tail_x, self.snake_tail_y, self.SNAKE_HEIGHT, self.SNAKE_WIDTH))
			
		# Adds one to the length if is_eating_apple is true
		else:
			
			self.snake_length += 1
			
		# Returns is_eating_apple
		return is_eating_apple
			
				
	# The function that detects whether the snake head is hitting somewhere on 
	# body_cord_x/y, not including the first index because that is always where 
	# the head is
	def is_self_colliding(self):
		
		
		# Uses a for loop with range of length of body_cord_x-1, as to not include the head
		# which is the first index, then it will compare body_cord_x/y to the snake_head_x/y
		# but the index will be i +1 for body_cord_x/y, if there is a colision then it returns 
		# true or false
		for i in range(len(self.body_cord_x)-1):
			
			# If statements that compare the snake_head_x/y to the body_cord_x/y
			if (self.snake_head_x == self.body_cord_x[i+1]) and (self.snake_head_y == self.body_cord_y[i+1]):
				
				# returns true if is coliding
				return True
			
			# else it returns false
			else:
				return False
	
	
	# The function that detects any wall collisions, will eb added into the main_update
	# function under is_dead = is_self_colliding or is_wall_colliding and returns true if it 
	# is colliding and false if not
	def is_wall_colliding(self):
		return False
	
	
	# the function that does the detection for buttons ,I may add the buttons used as part
	# of the __init__ function, but not now
	def button_detection(self):
		
		
		# Baisicly copied this code from Jsnake
		# If they click the 'x' in the corner
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				# Change the keyboard variables.
				if event.key == K_LEFT or event.key == K_a:
					self.head_direction = LEFT
				if event.key == K_RIGHT or event.key == K_d:
					self.head_direction = RIGHT
				if event.key == K_UP or event.key == K_w:
					self.head_direction = UP
				if event.key == K_DOWN or event.key == K_s:
					self.head_direction = DOWN
				if event.key == K_g:
					self.snake_length +=1
				if event.key == K_t:
					self.snake_length -=1
	
	# The main update function, it runs all the other functions in it, it take the 
	# arguements of the apples current x and y from the main game loop where it will be 
	# called in a loop of all the snake objects that have been created.
	def main_update(self, apple_x, apple_y):
		
		
		# The order of running functions goes: update_head, tail_update using eat_apple 
		# as a parameter, is_self_colliding, then when I add it, is_wall_colliding, if 
		# I add it, then the button stuff, I may latter add custom buttons as a parameter 
		# in the __init__ function.
		
		
		# update_head
		self.update_head()
		
		# tail_update with eat_apple as a parameter
		is_eating_apple = self.tail_update(self.eat_apple(apple_x, apple_y))
		
		# The variable that traks if the snake is dead
		# will add 'or wall_collision' later
		self.is_dead = self.is_self_colliding() or self.is_wall_colliding()
		
		# the button detection function, dont touch the actual code its unreadable
		self.button_detection()
		
		# Returnts to the main loop the is_eating_apple
		return is_eating_apple, self.is_self_colliding()
		
		# NEED TO MAKE THE REST OF THIS STUFF:
		#   is_wall_colliding needs to be writen
		#   whatever the button function will be called
		#   need to possibly return the is_dead to the main loop
		


# The function that makes an apple
# it is run every loop and if is_apple_eaten is true, then it spawns another apple
# and returns the new apple_x, and apple_y, also it does not need to cover up the old
# apple_x/y because the snake will have already have done this. if the apple has not been
# eaten it still displays the new apple x and y, in case it spawed on top of a snake
def make_apple(is_apple_eaten, apple_x, apple_y, SCREEN_HEIGHT, SCREEN_WIDTH, SNAKE_SPEED, WINDOW_SURFACE, color):
	
	
	# the If that determins whether to spawn a new apple or to redisplay the old one
	if is_apple_eaten:
		
		# randomly make new x and y for the apple location
		apple_x = (random.randint(0, (SCREEN_WIDTH/SNAKE_SPEED))*SNAKE_SPEED)
		apple_y = (random.randint(0, (SCREEN_HEIGHT/SNAKE_SPEED))*SNAKE_SPEED)
		
		# Displays new apple on the screen
		pygame.draw.rect(WINDOW_SURFACE, color, pygame.Rect(apple_x, apple_y, SNAKE_HEIGHT, SNAKE_WIDTH))
	
	# it still draws the apple even if it is not eaten
	else:
		pygame.draw.rect(WINDOW_SURFACE, color, pygame.Rect(apple_x, apple_y, SNAKE_HEIGHT, SNAKE_WIDTH))
	
	# returns the apple_x and y
	return apple_x, apple_y


# the first snake object, may later begin with more but not now
snake_objects = [Snake(SNAKE_SPEED*5, SNAKE_SPEED*5, RIGHT, CONSTANT_LIST)]

# first spawns the apple
apple_x, apple_y = make_apple(True, 0, 0, SCREEN_HEIGHT, SCREEN_WIDTH, SNAKE_SPEED, WINDOW_SURFACE, RED)

# the main game loop 
# first it does the required snake class stuff, then the apple stuff, should be easy to adapt for multiple snakes 
# NEED TO DO
#   IMPLEMENT SELF COLISSION
#   IMPLEMENT WALL COLLISION
while True:
	
	# for loop that goes through all the snake objects
	for snake_object in snake_objects:
		 
			# does the update for the snake, and returns the is_apple_eaten
			is_apple_eaten, is_dead = snake_object.main_update(apple_x, apple_y)
			
            # removes the snake from snake list if it is dead
            if is_dead:
                snake_objects.remove(snake_object)
            
			# puts is_apple_eaten into make apple
			apple_X, apple_y = make_apple(is_apple_eaten, apple_x, apple_y, SCREEN_HEIGHT, SCREEN_WIDTH, SNAKE_SPEED, WINDOW_SURFACE, RED)
	
	# Pygame stuff
	pygame.display.update()
	time.sleep(0.2)
