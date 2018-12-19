import random
import pygame

pygame.init()

display_w, display_h = 800, 600
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

screen = pygame.display.set_mode((display_w, display_h))
pygame.display.set_caption('1A2B')
clock= pygame.time.Clock()

def message_display(text_str, center_x, center_y):  # Pass in text_str and where to set the text's center
    font = pygame.font.SysFont('arial bold', 100)  # create a font object
    text_block = font.render(text_str, False, black)  # render text_str with the font
    text_rect = text_block.get_rect(center=(center_x, center_y))  # Get rect from text_block then center it
    screen.blit(text_block, text_rect)  # blit our text_block to that rect
    pygame.display.update()

def gameIntro():

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        message_display('Welcome to 1A2B', 400, 300)

        # Set up some rect surface to represent the buttons
        pygame.draw.rect(screen, green, (150, 450, 120, 100))
        pygame.draw.rect(screen, red, (550, 450, 120, 100))

        pygame.display.update()
        clock.tick(15)


def gameLoop():

    gameExit = False
    inp = []  # Take four number as input from the user

    # Generate random ans
    def gen_ans():
        ans = []
        while len(ans) != 4:
            n = random.randrange(0, 10)
            if not n in ans:
                ans.append(n)
        print(ans)
        return ans

    # Check usr_inp and the ans
    def check_answer(ans, nums):
        a, b = 0, 0
        for n in nums:
            if n in ans:
                if nums.index(n) == ans.index(n):
                    a += 1
                else:
                    b += 1
        return a, b

    # Checking Logic
    def main(user_input, ans):
        print(ans)
        logicExit = False
        while not logicExit:
            a, b = check_answer(ans, user_input)
            print("\n%dA%dB" % (a, b))
            if a == 4:
                logicExit = True
            else:
                return False
        return True

    # Main gameLoop
    answer = gen_ans()
    while not gameExit:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if len(inp) < 4:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        inp.append(0)
                    if event.key == pygame.K_1:
                        inp.append(1)
                    if event.key == pygame.K_2:
                        inp.append(2)
                    if event.key == pygame.K_3:
                        inp.append(3)
                    if event.key == pygame.K_4:
                        inp.append(4)
                    if event.key == pygame.K_5:
                        inp.append(5)
                    if event.key == pygame.K_6:
                        inp.append(6)
                    if event.key == pygame.K_7:
                        inp.append(7)
                    if event.key == pygame.K_8:
                        inp.append(8)
                    if event.key == pygame.K_9:
                        inp.append(9)
            elif len(inp) == 4:
                if main(inp, answer) == True:
                    message_display("Great!", 400, 300)
                    pygame.display.update()
                    pygame.time.delay(2000)
                    pygame.quit()
                    quit()
                else:
                    message_display("Keep trying!", 400, 300)
                    pygame.display.update()
                    pygame.time.delay(2000)
                    gameLoop()


        screen.fill(white)  # Set the background
        pygame.display.update()  # Update our display
        clock.tick(60)  # Setting fps


gameIntro()
gameLoop()
pygame.quit()
quit()
