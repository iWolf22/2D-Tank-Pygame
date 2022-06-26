# Importing all the essential python libraries

import pygame
pygame.init()
from pygame import *
init()

# Parent tank class

class GameSprite(sprite.Sprite):

	# Getting all the changable variables link to the tank

	def __init__(self,player_image,player_x,player_y,player_size,player_speed,player_health,player_direction):
		sprite.Sprite.__init__(self)
		self.image = transform.scale(image.load(player_image),(player_size,player_size))
		self.player_size = player_size

		self.player_speed = player_speed
		self.player_health = player_health
		self.player_direction = player_direction
		self.rect = self.image.get_rect()
		self.rect.y = player_y
		self.rect.x = player_x
		self.time = time.get_ticks()

		self.movement = "none"

	# Printing the tank to the screen

	def reset(self):
		window.blit(self.image,(self.rect.x,self.rect.y))

# Sub tank class

class Player(GameSprite):

	# Player movement function

	def update(self):

		# Bring in all the global varibles we would like to change

		global event
		global pause_button
		global back_button
		global game_loop
		global massive_pause_image
		global massive_pause_button

		# Checking if a button has been pressed

		for event in pygame.event.get():
			if(event.type == KEYDOWN):

				# If left arrow is pushed down

				if(event.key == K_LEFT and self.rect.x > 0):
					self.image = transform.scale(image.load("images/TankBlueLeft.png"),(self.player_size,self.player_size))
					self.player_direction = "left"
					self.movement = "left"

				# If right arrow is pushed down

				if(event.key == K_RIGHT and self.rect.x < 750):
					self.image = transform.scale(image.load("images/TankBlue.png"),(self.player_size,self.player_size))
					self.player_direction = "right"
					self.movement = "right"
				
				# If up arrow is pushed down

				if(event.key == K_UP and self.rect.y > 0):
					self.image = transform.scale(image.load("images/TankBlueUp.png"),(self.player_size,self.player_size))
					self.player_direction = "up"
					self.movement = "up"

				# If down arrow is pushed down

				if(event.key == K_DOWN and self.rect.y < 550):
					self.image = transform.scale(image.load("images/TankBlueDown.png"),(self.player_size,self.player_size))
					self.player_direction = "down"
					self.movement = "down"

				# If 'a' button is pushed down

				if(event.key == K_a and player2.rect.x > 0):
					player2.image = transform.scale(image.load("images/TankRedLeft.png"),(self.player_size,player2.player_size))
					player2.player_direction = "left"
					player2.movement = "left"

				# If 'd' button is pushed down

				if(event.key == K_d and player2.rect.x < 750):
					player2.image = transform.scale(image.load("images/TankRedRight.png"),(self.player_size,player2.player_size))
					player2.player_direction = "right" 
					player2.movement = "right"

				# If 'w' button is pushed down

				if(event.key == K_w and player2.rect.y > 0):
					player2.image = transform.scale(image.load("images/TankRedUp.png"),(self.player_size,player2.player_size))
					player2.player_direction = "up"
					player2.movement = "up"

				# If 's' button is pushed down

				if(event.key == K_s and player2.rect.y < 550):
					player2.image = transform.scale(image.load("images/TankRedDown.png"),(self.player_size,player2.player_size))
					player2.player_direction = "down"
					player2.movement = "down"

				# If right shift has been pressed and it has been 2 seconds, launch projectile in the direction that the tank is pointed.

				if event.key == K_RSHIFT and time.get_ticks() >= self.time:
					self.time = time.get_ticks() + 2000
					if self.player_direction == "right":
						player1_bullet_list.append(Bullet("images/RocketRight.png", self.rect.x, self.rect.y + 12, 25, 25, 5, self.player_direction,20))
					elif self.player_direction == "left":
						player1_bullet_list.append(Bullet("images/RocketLeft.png", self.rect.x, self.rect.y + 10, 25, 25, 5, self.player_direction,20))
					elif self.player_direction == "up":
						player1_bullet_list.append(Bullet("images/RocketUp.png", self.rect.x - 7, self.rect.y, 25, 25, 5, self.player_direction,20))
					else:
						player1_bullet_list.append(Bullet("images/RocketDown.png", self.rect.x - 7.5, self.rect.y + 5, 25, 25, 5, self.player_direction,20))
                
                # If space has been pressed and it has been 2 seconds, launch projectile in the direction that the tank is pointed.
                
				if event.key == K_SPACE and time.get_ticks() >= player2.time:
					player2.time = time.get_ticks() + 2000
					if player2.player_direction == "right":
						player2_bullet_list.append(Bullet("images/RocketRight.png", player2.rect.x, player2.rect.y + 12, 25, 25, 5, player2.player_direction,20))
					elif player2.player_direction == "left":
						player2_bullet_list.append(Bullet("images/RocketLeft.png", player2.rect.x, player2.rect.y + 12, 25, 25, 5, player2.player_direction,20))
					elif player2.player_direction == "up":
						player2_bullet_list.append(Bullet("images/RocketUp.png", player2.rect.x - 7, player2.rect.y, 25, 25, 5, player2.player_direction,20))
					else:
						player2_bullet_list.append(Bullet("images/RocketDown.png", player2.rect.x - 7.5, player2.rect.y + 5, 25, 25, 5, player2.player_direction,20))

			# For buttons, if the mouse has clicked

			if event.type == MOUSEBUTTONDOWN:

				# If the pause button has been clicked

				if pause_button.button_press(event) == True:
					pause = True
					while pause == True:
						for e in pygame.event.get():
							if e.type == MOUSEBUTTONDOWN:
								if massive_pause_button.button_press(e) == True:
									pause = False
						massive_pause_image.create_image()
						display.update()

				# If the back button has been clicked
									
				if back_button.button_press(event) == True:
					game_loop = False

			# Button up so create smooth player movement

			if event.type == KEYUP:
				if event.key == K_LEFT or event.key == K_RIGHT or event.key == K_UP or event.key == K_DOWN:
					self.movement = "none"

				if event.key == K_w or event.key == K_a or event.key == K_s or event.key == K_d:
					player2.movement = "none"

		
        # If the direction is in said direction, move the player in that direction at the given speed.
		
		if self.movement == "left":
			self.rect.x -= self.player_speed
            
			# Box collider so that player can't go through walls or other players

			if box_collider(player1):
				self.rect.x += self.player_speed
		if self.movement == "right":
			self.rect.x += self.player_speed
			if box_collider(player1):
				self.rect.x -= self.player_speed
		if self.movement == "down":
			self.rect.y += self.player_speed
			if box_collider(player1):
				self.rect.y -= self.player_speed
		if self.movement == "up":
			self.rect.y -= self.player_speed
			if box_collider(player1):
				self.rect.y += self.player_speed

		# Same thing but for player2

		if player2.movement == "left":
			player2.rect.x -= player2.player_speed
			if box_collider(player2):
				player2.rect.x += player2.player_speed
		if player2.movement == "right":
			player2.rect.x += player2.player_speed
			if box_collider(player2):
				player2.rect.x -= player2.player_speed
		if player2.movement == "down":
			player2.rect.y += player2.player_speed
			if box_collider(player2):
				player2.rect.y -= player2.player_speed
		if player2.movement == "up":
			player2.rect.y -= player2.player_speed
			if box_collider(player2):
				player2.rect.y += player2.player_speed

# Creates the background, defines the image (file), the dimensions, and the position

class Background():

	# Initializing all the important stuff

    def __init__(self,background_image,background_x,background_y,background_width,background_height):
        self.image = transform.scale(image.load(background_image),(background_width,background_height))
        self.background_x = background_x
        self.background_y = background_y

	# Printing the background on the screen
	
    def create_background(self):
        window.blit(self.image,(self.background_x,self.background_y))

# Creates the image for the rocket, defines the image (file), the dimensions, location, direction, and damage

class Bullet(): 

	# Initializing all the important stuff

	def __init__(self,bullet_image,bullet_x,bullet_y,bullet_size_x,bullet_size_y,bullet_speed,bullet_direction,bullet_damage):
		self.image = transform.scale(image.load(bullet_image),(bullet_size_x,bullet_size_y))
		self.bullet_direction = bullet_direction
		self.bullet_speed = bullet_speed
		self.rect = self.image.get_rect()
		self.rect.y = bullet_y
		self.rect.x = bullet_x + 20
		self.bullet_damage = bullet_damage

	# Printing the image onto the screen

	def reset(self):
		window.blit(self.image,(self.rect.x,self.rect.y))

	# Moving the bullet across the screen

	def update(self):
		if self.bullet_direction == "up":
			self.rect.y -= self.bullet_speed
		elif self.bullet_direction == "down":
			self.rect.y += self.bullet_speed
		elif self.bullet_direction == "left":
			self.rect.x -= self.bullet_speed
		else:
			self.rect.x += self.bullet_speed

# Class for text

class Phrase():

	# Initializing all the important stuff

    def __init__(self,color1,color2,color3,font_type,text,x_pos,y_pos,font_size):
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.font_type = font_type
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.font_size = font_size

	# Drawing the text to the screen
	
    def draw_text(self):
        self.font = font.SysFont(self.font_type,self.font_size)
        screen_text = self.font.render(self.text, True,(self.color1,self.color2,self.color3))
        window.blit(screen_text, [self.x_pos,self.y_pos])

# Class for the brick boxes and wooden boxes

class Wall():

	# Initializing all the important stuff

	def __init__(self,x_loc,y_loc,size,wall_image,wall_health):
		self.image = transform.scale(image.load(wall_image),(size,size))
		self.rect = self.image.get_rect()
		self.rect.x = x_loc
		self.rect.y = y_loc
		self.wall_health = wall_health

	# Printing out the wall onto the screen
		
	def reset(self):
		window.blit(self.image,(self.rect.x,self.rect.y))

# Checks if tanks have collided with a wall (box/brick) or another tank

def box_collider(tank):

	# Importing all the variables and objects we need
	
	global player1
	global player2
	global wall_list
	global brick_wall_list

	# Checking the sprite collider between the tank and the wooden boxes
	
	for i in range(len(wall_list)):
		if sprite.collide_rect(wall_list[i],tank):
			return True

	# Checking the sprite collider between the tank and the brick boxes

	for i in range(len(brick_wall_list)):
		if sprite.collide_rect(brick_wall_list[i],tank):
			return True

	# Checking the sprite collider between the two tanks

	if sprite.collide_rect(player1,player2):
		return True
	
	return False

# Explosion class animation

class Explosion():

	# Initializing all the important stuff

	def __init__(self,x_loc,y_loc,size):
		self.size = size
		self.counter = 0

		# List of all the stages of the explosion animation

		self.image_list = ["images/Explosion1.png","images/Explosion2.png","images/Explosion3.png","images/Explosion4.png","images/Explosion5.png","images/Explosion6.png","images/Explosion7.png"]
		self.image = transform.scale(image.load(self.image_list[counter]),(self.size,self.size))
		self.rect = self.image.get_rect()
		self.rect.x = x_loc
		self.rect.y = y_loc

	# Updating the explosion animation

	def update(self):

		# If their are no more images, delete the explosion object

		if self.counter >= 13:
			return "del"
		else:
			
			# Otherwise get a new image from the image_list with the index counter
			
			self.counter += 1
			self.image = transform.scale(image.load(self.image_list[int(self.counter / 2)]),(self.size,self.size))
			return "keep"
	
	# Printing the explosion onto the screen

	def reset(self):
		window.blit(self.image,(self.rect.x,self.rect.y))

# Button class

class Button():

	# Initializing all the important stuff

    def __init__(self,xLoc,yLoc,width,length):
        self.xLoc = xLoc
        self.yLoc = yLoc
        self.width = width
        self.length = length

	# Checking if the button has been pressed

    def button_press(self,e):

		# If the cordinates of the button press is inside of the area of the button

        if e.button == 1 and self.xLoc <= e.pos[0] and self.yLoc <= e.pos[1] and self.xLoc + self.width >= e.pos[0] and self.yLoc + self.length >= e.pos[1]:
            return True

# Creates an image 

class Image():

	# Initializing all the important stuff

    def __init__(self,background_image,background_x,background_y,background_width,background_height):
        self.image = transform.scale(image.load(background_image),(background_width,background_height))
        
        self.background_x = background_x
        self.background_y = background_y

	# Printing the image onto the screen

    def create_image(self):
        window.blit(self.image,(self.background_x,self.background_y))

# Lists to store mass amounts of data

button_list = []
map_name_list = []

# Buttons with their images to go along with them

pause_button = Button(350,0,50,50)
pause_image = Image("images/Pause_Button.png",350,0,50,50)
massive_pause_image = Image("images/Play.png",200,100,400,400)
massive_pause_button = Button(200,100,400,400)
back_button = Button(400,0,50,50)
back_image = Image("images/Back_Button.png",400,0,50,50)

# 5 buttons for the map selector along with 5 map names

for i in range(5):
	button_list.append(Button(150 * i + 50,450,100,100))
	map_name_list.append(Phrase(255,255,255,"Arial","Map " + str(i + 1),150 * i + 50,400,35))

# List to store all the map images

map_image_list = []

# Screenshots of all maps placed into map_image_list

map_image_list.append(Image("images/Map1.png",50,450,100,100))
map_image_list.append(Image("images/Map2.png",200,450,100,100))
map_image_list.append(Image("images/Map3.png",350,450,100,100))
map_image_list.append(Image("images/Map4.png",500,450,100,100))
map_image_list.append(Image("images/Map5.png",650,450,100,100))

# Logo image

logo_image = Image("images/Logo.png",10,10,780,200)

# The forever game loop

while True:

	# Creating the home screen

	window = display.set_mode((800, 600))
	tank_background = Background("images/Tank_Background.jpg",0,0,800,600)
	grass = Background("images/Grass.png",0,0,800,600)
	display.set_caption('Tank Battles')
	user_map = "none"
	
	starting_screen = False

	# While loop for the home screen
	
	while starting_screen == False:

		# Checking if a map has been selected to exit the start screen loop

		if user_map != "none":
			starting_screen = True

		# Calling all the functions to display all the objects, pictures, backgrounds, and buttons we created

		tank_background.create_background()
		logo_image.create_image()

		for i in range(len(map_image_list)):
			map_image_list[i].create_image()

		for i in range(len(map_name_list)):
			map_name_list[i].draw_text()
		
		# Checking if the mouse has been clicked and calling the button press functions to see which button has been pressed

		for e in pygame.event.get():
			if e.type == MOUSEBUTTONDOWN:
				for i in range(len(button_list)):
					if button_list[i].button_press(e) == True:
						user_map = i + 1

		# Updating the display

		display.update()

    # All map layouts

	if user_map == 1:

		# Using emojis to make map development easier and more visual
		# First map

		easy_map = [
			["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"],
			["⬛","🟦","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","⬛"],
			["⬛","🟩","🟫","🟫","🟫","🟩","🟩","⬛","⬛","🟩","🟩","🟫","🟫","🟫","🟩","⬛"],
			["⬛","🟩","🟫","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟫","🟩","⬛"],
			["⬛","🟩","🟫","🟩","🟩","🟩","🟩","🟫","🟫","🟩","🟩","🟩","🟩","🟫","🟩","⬛"],
			["⬛","🟩","🟩","🟩","⬛","🟩","🟫","⬛","⬛","🟫","🟩","⬛","🟩","🟩","🟩","⬛"],
			["⬛","🟩","🟩","🟩","⬛","🟩","🟫","⬛","⬛","🟫","🟩","⬛","🟩","🟩","🟩","⬛"],
			["⬛","🟩","🟫","🟩","🟩","🟩","🟩","🟫","🟫","🟩","🟩","🟩","🟩","🟫","🟩","⬛"],
			["⬛","🟩","🟫","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟫","🟩","⬛"],
			["⬛","🟩","🟫","🟫","🟫","🟩","🟩","⬛","⬛","🟩","🟩","🟫","🟫","🟫","🟩","⬛"],
			["⬛","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","❤️","⬛"],
			["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"],
			]

	elif user_map == 2:

		# Second map

		easy_map = [
			["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"],
			["⬛","🟦","🟩","🟩","🟩","🟫","🟫","🟫","🟫","🟫","🟫","🟩","🟩","🟩","🟩","⬛"],
			["⬛","🟩","🟫","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟫","🟩","⬛"],
			["⬛","🟩","🟫","🟩","🟫","🟫","🟫","🟩","🟩","🟫","🟫","🟫","🟩","🟫","🟩","⬛"],
			["⬛","🟩","🟫","⬛","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","⬛","🟫","🟩","⬛"],
			["⬛","🟩","🟩","⬛","🟩","🟫","🟩","⬛","⬛","🟩","🟫","🟩","⬛","🟩","🟩","⬛"],
			["⬛","🟩","🟩","⬛","🟩","🟫","🟩","⬛","⬛","🟩","🟫","🟩","⬛","🟩","🟩","⬛"],
			["⬛","🟩","🟫","⬛","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","⬛","🟫","🟩","⬛"],
			["⬛","🟩","🟫","🟩","🟫","🟫","🟫","🟩","🟩","🟫","🟫","🟫","🟩","🟫","🟩","⬛"],
			["⬛","🟩","🟫","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟫","🟩","⬛"],
			["⬛","🟩","🟩","🟩","🟩","🟫","🟫","🟫","🟫","🟫","🟫","🟩","🟩","🟩","❤️","⬛"],
			["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"],     
			]

	elif user_map == 3:

		# Third map

		easy_map = [
			["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"],
			["⬛","🟦","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","⬛"],
			["⬛","🟩","🟩","🟩","🟫","🟩","🟩","🟫","🟫","🟩","🟩","🟫","🟩","🟩","🟩","⬛"],
			["⬛","🟩","🟫","🟩","🟫","🟩","🟩","🟩","🟩","🟩","🟩","🟫","🟩","🟫","🟩","⬛"],
			["⬛","🟩","⬛","🟩","🟫","🟩","⬛","🟩","🟩","⬛","🟩","🟫","🟩","⬛","🟩","⬛"],
			["⬛","🟩","⬛","🟩","🟫","🟩","⬛","🟫","🟫","⬛","🟩","🟫","🟩","⬛","🟩","⬛"],
			["⬛","🟩","⬛","🟩","🟫","🟩","⬛","🟫","🟫","⬛","🟩","🟫","🟩","⬛","🟩","⬛"],
			["⬛","🟩","⬛","🟩","🟫","🟩","⬛","🟩","🟩","⬛","🟩","🟫","🟩","⬛","🟩","⬛"],
			["⬛","🟩","🟫","🟩","🟫","🟩","🟩","🟩","🟩","🟩","🟩","🟫","🟩","🟫","🟩","⬛"],
			["⬛","🟩","🟩","🟩","🟫","🟩","🟩","🟫","🟫","🟩","🟩","🟫","🟩","🟩","🟩","⬛"],
			["⬛","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","❤️","⬛"],
			["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"],     
			]

	elif user_map == 4:

		# Fourth map

		easy_map = [
			["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"],
			["⬛","🟦","🟩","🟩","🟩","🟩","🟩","🟫","🟫","🟩","🟩","🟩","🟩","🟩","🟩","⬛"],
			["⬛","🟩","🟩","⬛","🟫","⬛","🟩","🟫","🟫","🟩","⬛","🟫","⬛","🟩","🟩","⬛"],
			["⬛","🟩","🟫","⬛","🟫","⬛","🟩","🟫","🟫","🟩","⬛","🟫","⬛","🟫","🟩","⬛"],
			["⬛","🟩","🟫","🟩","🟫","🟩","🟩","🟫","🟫","🟩","🟩","🟫","🟩","🟫","🟩","⬛"],
			["⬛","🟩","🟫","🟩","⬛","🟩","🟩","🟫","🟫","🟩","🟩","⬛","🟩","🟫","🟩","⬛"],
			["⬛","🟩","🟫","🟩","⬛","🟩","🟩","🟫","🟫","🟩","🟩","⬛","🟩","🟫","🟩","⬛"],
			["⬛","🟩","🟫","🟩","🟫","🟩","🟩","🟫","🟫","🟩","🟩","🟫","🟩","🟫","🟩","⬛"],
			["⬛","🟩","🟫","⬛","🟫","⬛","🟩","🟫","🟫","🟩","⬛","🟫","⬛","🟫","🟩","⬛"],
			["⬛","🟩","🟩","⬛","🟫","⬛","🟩","🟫","🟫","🟩","⬛","🟫","⬛","🟩","🟩","⬛"],
			["⬛","🟩","🟩","🟩","🟩","🟩","🟩","🟫","🟫","🟩","🟩","🟩","🟩","🟩","❤️","⬛"],
			["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"],     
			]

	else:

		# Last map

		easy_map = [
			["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"],
			["⬛","🟦","🟫","🟩","🟩","🟩","🟫","🟩","🟩","🟫","🟩","🟩","🟩","🟫","🟩","⬛"],
			["⬛","🟩","⬛","⬛","🟫","🟩","⬛","🟩","🟩","⬛","🟩","🟫","⬛","⬛","🟩","⬛"],
			["⬛","🟩","⬛","🟩","🟩","🟩","⬛","🟫","🟫","⬛","🟩","🟩","🟩","⬛","🟩","⬛"],
			["⬛","🟩","⬛","🟩","⬛","🟩","⬛","🟩","🟩","⬛","🟩","⬛","🟩","⬛","🟩","⬛"],
			["⬛","🟩","🟫","🟩","⬛","🟩","🟫","🟩","🟩","🟫","🟩","⬛","🟩","🟫","🟩","⬛"],
			["⬛","🟩","🟫","🟩","⬛","🟩","🟫","🟩","🟩","🟫","🟩","⬛","🟩","🟫","🟩","⬛"],
			["⬛","🟩","⬛","🟩","⬛","🟩","⬛","🟩","🟩","⬛","🟩","⬛","🟩","⬛","🟩","⬛"],
			["⬛","🟩","⬛","🟩","🟩","🟩","⬛","🟫","🟫","⬛","🟩","🟩","🟩","⬛","🟩","⬛"],
			["⬛","🟩","⬛","⬛","🟫","🟩","⬛","🟩","🟩","⬛","🟩","🟫","⬛","⬛","🟩","⬛"],
			["⬛","🟩","🟫","🟩","🟩","🟩","🟫","🟩","🟩","🟫","🟩","🟩","🟩","🟫","❤️","⬛"],
			["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"],     
			]

    # Depending on the emoji we add a wooden crate, brick wall, player1 or player2 to the game in the same position as the location in the 2D array

	wall_list = []
	brick_wall_list = []
	for i in range(len(easy_map)):
		for j in range(len(easy_map[i])):

			# If the emoji is a brown square, add a wooden crate in its relative location

			if easy_map[i][j] == "🟫":
				wall_list.append(Wall(j * 50,i * 50 ,50,"images/Crate.png",100))

			# If the emoji is a black square, add a brick wall in its relative location

			if easy_map[i][j] == "⬛":
				brick_wall_list.append(Wall(j * 50,i * 50 ,50,"images/BrickWall.png",100))

			# If the emoji is a blue square, add the blue tank in its relative location

			if easy_map[i][j] == "🟦":
				player1 = Player("images/TankBlue.png",j * 50,i * 50,45,2,100,"left")

			# If the emoji is a red heart, add the red tank in its relative location

			if easy_map[i][j] == "❤️":
				player2 = Player("images/TankRedRight.png",j * 50,i * 50,45,2,100,"left")

	# Player 1 and 2 health bars

	player2_health_bar = Phrase(255,0,0,"Arial","Red HP: " + str(player2.player_health),5,30,25)
	player1_health_bar = Phrase(0,0,255,"Arial","Blue HP: " + str(player1.player_health),5,5,25)

	# Emptying the bullet lists and the explosion list

	player1_bullet_list = []
	player2_bullet_list = []
	explosion_list = []

	# Main game loop, where the game is played

	game_loop = True

	while game_loop == True:

		# Creating the grass background

		grass.create_background()

		# Checking for player movement and if a button has been pressed for both player 1 and 2

		player1.update()

		# Updating then displaying out player 1 and 2 bullets

		for i in range(len(player1_bullet_list)):
			player1_bullet_list[i].update()
			player1_bullet_list[i].reset()

		for i in range(len(player2_bullet_list)):
			player2_bullet_list[i].update()
			player2_bullet_list[i].reset()
        
		# Updating the player's health bars

		player1_health_bar = Phrase(0,0,255,"Arial","Blue HP: " + str(player1.player_health),5,5,25)
		player2_health_bar = Phrase(255,0,0,"Arial","Red HP: " + str(player2.player_health),5,30,25)
        
		# Displaying player 1 and 2 onto the screen

		player2.reset()
		player1.reset()
		
		# Displaying all the wooden crates onto the screen

		for i in range(len(wall_list)):
			wall_list[i].reset()

		# Displaying all the brick walls onto the screen

		for i in range(len(brick_wall_list)):
			brick_wall_list[i].reset()
		
		# Explsions

		counter = 0
		for i in explosion_list:

			# Displaying all the explosions

			explosion_list[counter].reset()

			# Deleting all the finished explosions

			if explosion_list[counter].update() == "del":
				del explosion_list[counter]
				counter += 1

		# Checking if player1's bullet and player2 have collided
		# If the have, minus player1's health by player2's bullet damage
		# Then create an explosion
		# Finally delete the bullet that hit player2

		counter = 0
		for i in range(len(player1_bullet_list)):
			if sprite.collide_rect(player1_bullet_list[i - counter],player2):
				player2.player_health -= player1_bullet_list[i - counter].bullet_damage
				explosion_list.append(Explosion(player2.rect.x - 25,player2.rect.y - 25,100))
				del player1_bullet_list[i - counter]
				counter += 1

		# Checking if player2's bullet and player1 have collided
		# If the have, subtract player1's bullet damage from player2's health  
		# Then create an explosion
		# Finally, delete the bullet that hit player1

		counter = 0
		for i in range(len(player2_bullet_list)):
			if sprite.collide_rect(player2_bullet_list[i - counter],player1):
				player1.player_health -= player2_bullet_list[i - counter].bullet_damage
				explosion_list.append(Explosion(player1.rect.x - 25,player1.rect.y - 25,100))
				del player2_bullet_list[i - counter]
				counter += 1

		# Checking if player2's bullet and player1's bullet have collided
		# If the have, then create an explosion
		# Finally, delete the two bullets

		counter = 0
		for i in range(len(player2_bullet_list)):
			for j in range(len(player1_bullet_list)):
				if sprite.collide_rect(player2_bullet_list[i - counter],player1_bullet_list[j - counter]):
					explosion_list.append(Explosion(player1_bullet_list[j - counter].rect.x - 38,player1_bullet_list[j - counter].rect.y - 38,100))
					del player2_bullet_list[i - counter]
					del player1_bullet_list[j - counter]
					counter += 1
					break

		# Checking if player1's bullet has hit a wooden crate
		# If they have, then create an explosion
		# Then delete both the wooden crate and the bullet

		counter = 0
		for i in range(len(wall_list)):
			for j in range(len(player1_bullet_list)):
				if sprite.collide_rect(wall_list[i - counter],player1_bullet_list[j - counter]):
					explosion_list.append(Explosion(player1_bullet_list[j - counter].rect.x - 38,player1_bullet_list[j - counter].rect.y - 38,100))
					del player1_bullet_list[j - counter]
					del wall_list[i - counter]
					counter += 1

		# Checking if player2's bullet has hit a wooden crate
		# If they have, then create an explosion
		# Then delete both the wooden crate and the bullet

		counter = 0
		for i in range(len(wall_list)):
			for j in range(len(player2_bullet_list)):
				if sprite.collide_rect(wall_list[i - counter],player2_bullet_list[j - counter]):
					explosion_list.append(Explosion(player2_bullet_list[j - counter].rect.x - 38,player2_bullet_list[j - counter].rect.y - 38,100))
					del player2_bullet_list[j - counter]
					del wall_list[i - counter]
					counter += 1

		# Checking if player1's bullet has hit a brick wall
		# If they have, then create an explosion
		# Then delete the bullet

		counter = 0
		for i in range(len(brick_wall_list)):
			for j in range(len(player1_bullet_list)):
				if sprite.collide_rect(brick_wall_list[i - counter],player1_bullet_list[j - counter]):
					explosion_list.append(Explosion(player1_bullet_list[j - counter].rect.x - 38,player1_bullet_list[j - counter].rect.y - 38,100))
					del player1_bullet_list[j - counter]
					counter += 1

		# Checking if player2's bullet has hit a brick wall
		# If they have, then create an explosion
		# Then delete the bullet

		counter = 0
		for i in range(len(brick_wall_list)):
			for j in range(len(player2_bullet_list)):
				if sprite.collide_rect(brick_wall_list[i - counter],player2_bullet_list[j - counter]):
					explosion_list.append(Explosion(player2_bullet_list[j - counter].rect.x - 38,player2_bullet_list[j - counter].rect.y - 38,100))
					del player2_bullet_list[j - counter]
					counter += 1

		# Drawing player 1 and 2 health bar

		player1_health_bar.draw_text()
		player2_health_bar.draw_text()

		# Displaying the pause button and the back button

		pause_image.create_image()
		back_image.create_image()

		# If one of the player's health is less than or equal to zero then the other player wins

		win = "none"
		if player1.player_health <= 0:
			game_loop = False
			win = "red"
		if player2.player_health <= 0:
			game_loop = False
			win = "blue"

		# If one of the players has won

		if win != "none":

			# Backrgound winning image

			background_win = Background("images/Victory.png",0,0,800,600)

			# Different winning text depending on who won

			if win == "red":
				win_logo = Image("images/RedWins.png",100,200,600,200)
			else:
				win_logo = Image("images/BlueWins.png",100,200,600,200)

			# For 5 seconds display the background image and the winning player

			temp_time = time.get_ticks() + 5000
			while temp_time > time.get_ticks():
				background_win.create_background()
				win_logo.create_image()
				
				# Update the display

				display.update()

		# Update the display

		display.update()

		pygame.time.wait(10)