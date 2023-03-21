import pygame
import sys
import json

# Initialize Pygame
pygame.init()

#getting the screen width and height of device currently running the program
device_screen = pygame.display.Info()
screen_width, screen_height = device_screen.current_w-100, device_screen.current_h-100

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# scale the loaded image to the screen size
img = pygame.transform.scale(pygame.image.load('assets/0,0 north.png'), (screen_width,screen_height))


MAP_LOGIC = {}

with open('map.json', 'r') as read_file:
    MAP_LOGIC = json.loads(read_file.read())

# put the image onto the screen
screen.blit(img, (0, 0))

# Update the display
pygame.display.update()


class Player():

    def __init__(self):
        self.current_pos = "(0,0)"
        self.orientation = "north"
        # self.previous_orientation = "north"     #north by default 
        self.visited_stack = []                 # stack data structure for back functionality

    def get_img(self):
        return pygame.transform.scale(pygame.image.load(MAP_LOGIC[self.current_pos][self.orientation]["img"]), (screen_width,screen_height))

    def update_position(self, key_pressed):
        
        # if key_pressed is back and there still is a previous position in visited queue
        # then go back to previous position  
        if key_pressed == "back" and self.visited_stack:
            previous_position = self.visited_stack.pop()                        
            self.current_pos = MAP_LOGIC[previous_position]["default"]
            self.orientation = "north"                                          #
        
        # north orientation
        elif self.orientation == "north" and key_pressed == "forward":
            if 'next_pos' in MAP_LOGIC[self.current_pos][self.orientation]:
                self.visited_stack.append(self.current_pos)
                self.current_pos = MAP_LOGIC[self.current_pos][self.orientation]["next_pos"]       # updating current position to next position
                
        elif self.orientation == "north" and key_pressed == "left":
            self.orientation = "west"

        elif self.orientation == "north" and key_pressed == "right":
            self.orientation = "east"

        #west
        elif self.orientation == "west" and key_pressed == "forward":
            if 'next_pos' in MAP_LOGIC[self.current_pos][self.orientation]:
                self.visited_stack.append(self.current_pos)
                self.current_pos = MAP_LOGIC[self.current_pos][self.orientation]["next_pos"]       # updating current position to next position
                
        elif self.orientation == "west" and key_pressed == "left":
            self.orientation = "south"

        elif self.orientation == "west" and key_pressed == "right":
            self.orientation = "north"
        
        #south
        elif self.orientation == "south" and key_pressed == "forward":
            if 'next_pos' in MAP_LOGIC[self.current_pos][self.orientation]:
                self.visited_stack.append(self.current_pos)
                self.current_pos = MAP_LOGIC[self.current_pos][self.orientation]["next_pos"]       # updating current position to next position
                

        elif self.orientation == "south" and key_pressed == "left":
            self.orientation = "east"

        elif self.orientation == "south" and key_pressed == "right":
            self.orientation = "west"

        #east
        elif self.orientation == "east" and key_pressed == "forward":
            if 'next_pos' in MAP_LOGIC[self.current_pos][self.orientation]:
                self.visited_stack.append(self.current_pos)
                self.current_pos = MAP_LOGIC[self.current_pos][self.orientation]["next_pos"]       # updating current position to next position
                
        elif self.orientation == "east" and key_pressed == "left":
            self.orientation = "north"

        elif self.orientation == "east" and key_pressed == "right":
            self.orientation = "south"

player = Player()

# Main loop
while True:

    for event in pygame.event.get():
        # checks if user quits game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        #records which direction key is pressed, if any
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.update_position("forward")
            elif event.key == pygame.K_DOWN:
                player.update_position("back")
            elif event.key == pygame.K_LEFT:
                player.update_position("left")
            elif event.key == pygame.K_RIGHT:
                player.update_position("right")

    # walk through completed 
    if player.current_pos == "(3,4)" and player.orientation == "west":
        screen.fill((255,255,255))

        img_on_screen = player.get_img()
        screen.blit(img_on_screen,(0,0))

        pygame.display.update()
        pygame.time.delay(5000)  # Delay for 5 seconds so game doesnt end abruptly
        break

    screen.fill((255,255,255))

    img_on_screen = player.get_img()
    screen.blit(img_on_screen,(0,0))

    pygame.display.update()




