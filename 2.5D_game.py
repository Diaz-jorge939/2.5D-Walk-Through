import pygame
import sys
import json

# Initialize Pygame
pygame.init()

#getting the screen width and height of device currently running the program
device_screen_info = pygame.display.Info()
screen_width, screen_height = device_screen.current_w-100, device_screen.current_h-100

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# scale the loaded image to the screen size
img = pygame.transform.scale(pygame.image.load('New folder/assets/0,0.png'), (screen_width,screen_height))


MAP_LOGIC = {}

with open('map.json', 'r') as read_file:
    MAP_LOGIC = json.loads(read_file.read())

# put the image onto the screen
screen.blit(img, (0, 0))

# Update the display
pygame.display.update()


class player():

    def __init__(self):
        self.current_pos = "(0,0)"
        self.orientation = "north"

    def update_position(self, key_pressed):
        if self.orientation == "north" and key_pressed == "north":
            self.current_pos = MAP_LOGIC[str(self.current_pos)][self.orientation]["next_pos"]       # updating current position to next position

        elif key_pressed == "backward":
            self.current_pos = MAP_LOGIC[self.current_pos][self.orientation]["next_pos"]
        elif key_pressed == "left":
            self.orientation = MAP_LOGIC[self.current_pos][self.orientation]
        elif key_pressed == "right":
            self.orientation = MAP_LOGIC[self.current_pos][self.orientation]



def get_img(img_path):
    return pygame.transform.scale(pygame.image.load(img_path), (screen_width,screen_height))

# Main loop
while True:

    player = player()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.update_position("north")
            elif event.key == pygame.K_DOWN:
                player.update_position("south")
            elif event.key == pygame.K_LEFT:
                player.update_position("west")
            elif event.key == pygame.K_RIGHT:
                player.update_position("east")

    img_on_screen = get_img(map[player.current_pos][img])
    screen.fill((255,255,255))
    screen.blit(new_img,(0,0))

    pygame.display.update()




