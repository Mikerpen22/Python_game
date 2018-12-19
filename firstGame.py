import pygame
import time
import random
pygame.init()

# Display size and color/ Color settings
display_width = 800
display_height = 600
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Basic stuff for setting up the GUI and the clock
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Test')
run_time = pygame.time.Clock()

# Load the image and log the width and height
avatar_img = pygame.image.load('mario_8bit.png')
avatar_img_width = avatar_img.get_rect().size[0]
avatar_img_height = avatar_img.get_rect().size[1]

# Deal with Positioning the image or text
class Position:

    @staticmethod  # For images
    def alignWithPoint(surface, x, y):
        screen.blit(surface, (x, y))
        pygame.display.update()  # Since blit is working in background, Update the display to let it show

    @staticmethod  # For messages
    def alignWithRect(surface, rect):
        screen.blit(surface, rect)
        pygame.display.update()
setPosition = Position()

class Obstacles:
    def __init__(self, obs_x, obs_y, obs_w, obs_h, color):
        self.obs_x = obs_x
        self.obs_y = obs_y
        self.obs_w = obs_w
        self.obs_h = obs_h
        self.color = color
        self.speed = -5

    def draw_obstacles(self):
        pygame.draw.rect(screen, self.color, [self.obs_x, self.obs_y, self.obs_w, self.obs_h])  # [x, y, w, h] to define the rect to be drawn
        pygame.display.update([self.obs_x, self.obs_y, self.obs_w, self.obs_h])  # Update this block's position every time we create it(Prevent flicker)


def message_display(text_str, center_x, center_y):  # Pass in text_str and where to set the text's center
    font = pygame.font.SysFont('arial bold', 100)  # create a font object
    text_block = font.render(text_str, False, (0, 0, 0))  # render text_str with the font
    text_rect = text_block.get_rect(center=(center_x, center_y))  # Get rect from text_block then center it
    setPosition.alignWithRect(text_block, text_rect)  # blit our text_block to that rect


def crash():
    # Display the message that we crash the wall
    message_display('Crash!', display_width*1/2, display_height*1/2)
    time.sleep(2)  # let the message display for 2 seconds
    gameLoop()


def gameLoop():

    x = display_width * 0.45  # Initial position of the mario
    y = display_height * 0.5
    obs_1 = Obstacles(display_width + 300, random.randrange(0, 200), 50, 50, black)
    obs_2 = Obstacles(display_width + 300, random.randrange(200, 550), 50, 50, (0, 255, 0))
    obs_lst = [obs_1, obs_2]

    x_change = 0
    y_change = 0

    game_exit = False
    while not game_exit:
        for event in pygame.event.get():  # list of event happened per frame per second
            if event.type == pygame.QUIT:  # ex.你按叉叉的時候
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:  # 偵測有沒有按下鍵盤
                if event.key == pygame.K_LEFT:  # change the location of the mario
                    x_change = -10
                elif event.key == pygame.K_RIGHT:
                    x_change = 10
                elif event.key == pygame.K_UP:
                    y_change = -10
                elif event.key == pygame.K_DOWN:
                    y_change = 10

            if event.type == pygame.KEYUP:  # 手離開鍵盤就不要動
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

            print(event)  # Log the user's action

        x += x_change  # Apply the change of position
        y += y_change

        screen.fill(white)  # Set the background
        setPosition.alignWithPoint(avatar_img, x, y)  # Set the position of mario

        # draw obstacles and make it fly in
        for obs in obs_lst:
            obs.draw_obstacles()
            obs.obs_x += obs.speed

        # check whether avatar is still in our display (x,y is measured by the top left corner of the image)
        if y > (display_height - avatar_img_height) or y < 0:
            crash()  # 呼叫撞牆

        # Check whether the obstacles fly 'out' the screen, if so then reset coordinates
        for index, obs in enumerate(obs_lst):
            obs_y_used = []
            if obs.obs_x + avatar_img_width < 0:
                obs.obs_x = display_width + 10
                y_random = random.randrange(1, display_height - 50)
                obs.obs_y = y_random+50 if y_random not in obs_y_used else (display_height - y_random)
                obs_y_used.append(obs.obs_y)

        # Check if Mario hits the obstacle
        for obs in obs_lst:
            if (y + avatar_img_height > obs.obs_y > y) or (y < obs.obs_y + obs.obs_h < y + avatar_img_height):
                if x < obs.obs_x <= x + avatar_img_width:
                    crash()

        pygame.display.update()  # Update our display
        run_time.tick(60)  # Setting fps


gameLoop()
pygame.quit()
quit()
