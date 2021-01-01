# The program uses third-party icons, which are credited to:

# <div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
# <div>Icons made by <a href="http://www.freepik.com/" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
# <div>Icons made by <a href="https://www.flaticon.com/authors/flat-icons" title="Flat Icons">Flat Icons</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
# <div>Icons made by <a href="https://www.flaticon.com/authors/ultimatearm" title="ultimatearm">ultimatearm</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

# The creator of the following program does not own any of the icons used below. All of the copyrights of the icons below belongs to the 
# creators mentioned above.

import pygame
import random
import math

# Initializing the game
pygame.init()

def player_positioning(x, y):
    screen.blit(player_image, (x, y))

def fence_positioning(x, y, f):
    screen.blit(fence_image[f], (x, y))

def bat_positioning(x, y, b):
    screen.blit(bat_image[b], (x, y))

def arrow_positioning(x, y):
    screen.blit(arrow_image, (x, y + 10))

def dragon_positioning(x, y):
    screen.blit(dragon_image, (x, y))

def fire_positioning(x, y):
    screen.blit(fire_image, (x, y + 10))

def octopus_positioning(x, y):
    screen.blit(octopus_image, (x, y))

def waterdrop_positioning(x, y, w):
    screen.blit(waterdrop_image[w], (x, y + 10))

# Collision
# Enemy killer collisions
# Enemies includes bat, fence, waterdrop and fire
def enemy_arrow_collision(bat_x, bat_y, arrow_x, arrow_y):
    distance = math.sqrt((bat_x - arrow_x)**2 + (bat_y - arrow_y)**2)
    if distance < 75:
        return True
    else:
        return False

# Boss includes dragon and octopus
def boss_arrow_collision(boss_x, boss_y, arrow_x, arrow_y):
    distance = math.sqrt((boss_x - arrow_x)**2 + (boss_y - arrow_y)**2)
    if distance < 300:
        return True
    else:
        return False

# Game Over collisions:
# Enemies includes bat, fence, waterdrop and fire
def enemy_player_collision(enemy_x, enemy_y, player_x, player_y):
    distance = math.sqrt((enemy_x - player_x)**2 + (enemy_y - player_y)**2)
    if distance < 75:
        return True
    else:
        return False

# Boss includes dragon and octopus
def boss_player_collision(boss_x, boss_y, player_x, player_y):
    distance = math.sqrt((boss_x - player_x)**2 + (boss_y - player_y)**2)
    if distance < 100:
        return True
    else:
        return False

# Showing welcome, end, and score texts on the screen
def game_start_text():
    first_line_font = pygame.font.Font('freesansbold.ttf', 60)
    font = pygame.font.Font('freesansbold.ttf', 35)
    first_line = first_line_font.render("Welcome to Horse Racer!", True, (0, 0, 0))
    second_line = font.render("Use the up, left, and right arrow keys to jump, move left and move right.", True, (0, 0, 0))
    third_line = font.render("To shoot down bats, dragons, and octopus, press space to shoot arrows.", True, (0, 0, 0))
    fourth_line = font.render("Press s to start the game.", True, (0, 0, 0))
    screen.blit(first_line, (400, 150))
    screen.blit(second_line, (150, 350))
    screen.blit(third_line, (150, 400))
    screen.blit(fourth_line, (550, 550))

def game_over_text(score_value, game_result):
    first_line_font = pygame.font.Font('freesansbold.ttf', 60)
    font = pygame.font.Font('freesansbold.ttf', 35)
    first_line = first_line_font.render(game_result, True, (0, 0, 0))
    second_line = first_line_font.render(f"Your score is {score_value}", True, (0, 0, 0))
    third_line = font.render("Press p if you want to play again, otherwise close the window or press e to exit.", True, (0, 0, 0))
    screen.blit(first_line, (525, 150))
    screen.blit(second_line, (525, 350))
    screen.blit(third_line, (100, 550))

def show_score(score_value):
    font = pygame.font.Font('freesansbold.ttf', 64)
    score = font.render("Score : " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (10, 10))

# Main Game Loop
def game_loop():
    game_open = True
    game_running = False
    game_over = False

    # Screen
    global screen
    screen = pygame.display.set_mode((1500, 780))
    # Background
    background = pygame.image.load("background.png")
    # Caption and Icon
    icon = pygame.image.load("horse_icon.png")
    pygame.display.set_caption("Horse Racer")
    pygame.display.set_icon(icon)

    # Player
    global player_image
    player_image = pygame.image.load("horse.png")
    player_x = 100
    player_y = 500
    player_x_change = 0
    player_y_change = 0

    # Fence
    number_of_fences = random.randint(1, 3)
    global fence_image
    fence_image = []
    fence_x = []
    fence_y = []
    fence_x_change = []
    for _ in range(number_of_fences):
        fence_image.append(pygame.image.load('fence.png'))
        fence_x.append(random.randint(1500, 1800))
        fence_y.append(570)
        fence_x_change.append(-3)

    # Bat
    number_of_bat = random.randint(0, 2)
    global bat_image
    bat_image = []
    bat_x = []
    bat_y = []
    bat_x_change = []
    for _ in range(number_of_bat):
        bat_image.append(pygame.image.load('bat.png'))
        bat_x.append(random.randint(1500, 1800))
        bat_y.append(random.randint(100, 550))
        bat_x_change.append(-3)

    # Arrow
    global arrow_image
    arrow_image = pygame.image.load('arrow.png')
    arrow_x = 0
    arrow_y = 0
    arrow_x_change = 15
    arrow_state = "OFF"

    # Dragon
    global dragon_image
    dragon_image = pygame.image.load('dragon.png')
    dragon_x = 1200
    dragon_y = 300
    dragon_y_change = -5
    dragon_life_point = 5

    # Fire
    global fire_image
    fire_image = pygame.image.load('fire.png')
    fire_x = 1300
    fire_y = random.randint(100, 500)
    fire_x_change = -7

    # Octopus
    global octopus_image
    octopus_image = pygame.image.load('octopus.png')
    octopus_x = 1200
    octopus_y = 300
    octopus_y_change = -5
    octopus_life_point = 5

    # Waterdrop
    global waterdrop_image
    waterdrop_image = []
    waterdrop_x = []
    waterdrop_y = []
    waterdrop_y_change = []
    number_of_waterdrops = random.randint(1, 3)
    for _ in range(number_of_waterdrops):
        waterdrop_image.append(pygame.image.load('waterdrop.png'))
        waterdrop_x.append(random.randint(0, 1300))
        waterdrop_y.append(0)
        waterdrop_y_change.append(5)

    # Count until next boss is coming
    count = 0
    # Player's score
    score_value = 0
    # Game result either game over if the player losses or congratulations if the player wins
    game_result = ""

    while game_open:
        # RGB
        screen.fill((0, 0, 0))
        # Background Image
        screen.blit(background, (0, 0))
        # Show the welcome message of the game
        game_start_text()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_open = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    game_running = True
                    game_over = False

        while game_running:
            # RGB
            screen.fill((0, 0, 0))
            # Background Image
            screen.blit(background, (0, 0))
            while game_over:
                # RGB
                screen.fill((0, 0, 0))
                # Background Image
                screen.blit(background, (0, 0))
                game_over_text(score_value, game_result)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_running = False
                        game_open = False
                        game_over = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_e:
                            game_running = False
                            game_open = False
                            game_over = False
                        if event.key == pygame.K_p:
                            game_loop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False
                    game_open = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if player_y == 500:
                            player_x_change = -7
                    if event.key == pygame.K_RIGHT:
                        if player_y == 500:
                            player_x_change = 7
                    if event.key == pygame.K_UP:
                        if player_y == 500:
                            player_y_change = -7
                    if event.key == pygame.K_SPACE:
                        if arrow_state == "OFF":
                            # Get the current x, y cordinate of the horse rider
                            arrow_state = "ON"
                            arrow_x = player_x
                            arrow_y = player_y
                            arrow_positioning(arrow_x, arrow_y)
        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        player_x_change = 0
    
            # Player Movement
            player_x += player_x_change
            if player_x <= 0:
                player_x = 0
            elif player_x >= 1300:
                player_x = 1300

            player_y += player_y_change
            if player_y <= 100:
                player_y_change = 7
            elif player_y == 500:
                player_y_change = 0
            player_positioning(player_x, player_y)
            
            # Arrow Movement
            if arrow_x >= 1500:
                arrow_state = "OFF"

            if arrow_state == "ON":
                arrow_positioning(arrow_x, arrow_y)
                arrow_x += arrow_x_change

            # Showing score
            show_score(score_value)
            
            if count == 2:
                # Dragon Movement
                dragon_y += dragon_y_change
                if dragon_y == 100:
                    dragon_y_change = 5
                elif dragon_y == 500:
                    dragon_y_change = -5

                # collision
                is_collision = boss_player_collision(dragon_x, dragon_y, arrow_x, arrow_y)
                if is_collision and arrow_state == "ON":
                    dragon_life_point -= 1
                    score_value += 1
                    arrow_state = "OFF"
                if dragon_life_point == 0:
                    # Resetting the dragon and the fire statistics for the next dragon
                    dragon_image = pygame.image.load('dragon.png')
                    dragon_x = 1200
                    dragon_y = 300
                    dragon_y_change = -5
                    dragon_life_point = 5
                    fire_image = pygame.image.load('fire.png')
                    fire_x = 1300
                    fire_y = random.randint(100, 500)
                    fire_x_change = -7
                    count += 1

                # Game over collision
                is_collision = boss_player_collision(dragon_x, dragon_y, player_x, player_y)
                if is_collision:
                    game_result = "GAME OVER"
                    game_over = True
                dragon_positioning(dragon_x, dragon_y)

                # Fire Movement
                fire_x += fire_x_change
                # Game over collision
                is_collision = enemy_player_collision(fire_x, fire_y, player_x, player_y)
                if is_collision:
                    game_result = "GAME OVER"
                    game_over = True
                fire_positioning(fire_x, fire_y)

                # Fire Reset
                if fire_x <= -100:
                    fire_image = pygame.image.load('fire.png')
                    fire_x = 1300
                    fire_y = random.randint(100, 500)
                    fire_x_change = -7

            elif count == 5:
                # Dragon Movement
                dragon_y += dragon_y_change
                if dragon_y == 100:
                    dragon_y_change = 5
                elif dragon_y == 500:
                    dragon_y_change = -5

                # collision
                is_collision = boss_player_collision(dragon_x, dragon_y, arrow_x, arrow_y)
                if is_collision and arrow_state == "ON":
                    dragon_life_point -= 1
                    score_value += 1
                    arrow_state = "OFF"
                if dragon_life_point == 0:
                    count += 1

                # Game over collision
                is_collision = boss_player_collision(dragon_x, dragon_y, player_x, player_y)
                if is_collision:
                    game_result = "GAME OVER"
                    game_over = True
                dragon_positioning(dragon_x, dragon_y)

                # Fire Movement
                fire_x += fire_x_change
                # Game over collision
                is_collision = enemy_player_collision(fire_x, fire_y, player_x, player_y)
                if is_collision:
                    game_result = "GAME OVER"
                    game_over = True
                fire_positioning(fire_x, fire_y)

                # Fire Reset
                if fire_x <= 0:
                    fire_image = pygame.image.load('fire.png')
                    fire_x = 0
                    fire_y = random.randint(100, 500)
                    fire_x_change = 7
                elif fire_x >= 1300:
                    fire_image = pygame.image.load('fire.png')
                    fire_x = 1300
                    fire_y = random.randint(100, 500)
                    fire_x_change = -7
            
            elif count == 8:
                # Octopus Movement
                octopus_y += octopus_y_change
                if octopus_y == 100:
                    octopus_y_change = 5
                elif octopus_y == 500:
                    octopus_y_change = -5

                # collision
                is_collision = boss_player_collision(octopus_x, octopus_y, arrow_x, arrow_y)
                if is_collision and arrow_state == "ON":
                    octopus_life_point -= 1
                    score_value += 1
                    arrow_state = "OFF"
                if octopus_life_point == 0:
                    game_result = "Congratulations!"
                    game_over = True

                # Game over collision
                is_collision = boss_player_collision(octopus_x, octopus_y, player_x, player_y)
                if is_collision:
                    game_result = "GAME OVER"
                    game_over = True
                octopus_positioning(octopus_x, octopus_y)

                # Waterdrop Movement
                for w in range(number_of_waterdrops):
                    waterdrop_y[w] += waterdrop_y_change[w]
                    # Game over collision
                    is_collision = enemy_player_collision(waterdrop_x[w], waterdrop_y[w], player_x, player_y)
                    if is_collision:
                        game_result = "GAME OVER"
                        game_over = True
                    waterdrop_positioning(waterdrop_x[w], waterdrop_y[w], w)

                # Waterdrop Reset
                if waterdrop_y[w] >= 800:
                    waterdrop_image = []
                    waterdrop_x = []
                    waterdrop_y = []
                    waterdrop_y_change = []
                    number_of_waterdrops = random.randint(1, 3)
                    for _ in range(number_of_waterdrops):
                        waterdrop_image.append(pygame.image.load('waterdrop.png'))
                        waterdrop_x.append(random.randint(0, 1300))
                        waterdrop_y.append(0)
                        waterdrop_y_change.append(5)

            else: 
                # Fence Movement
                for f in range(number_of_fences):
                    fence_x[f] += fence_x_change[f]
                    # Game over collision
                    is_collision = enemy_player_collision(fence_x[f], fence_y[f], player_x, player_y)
                    if is_collision:
                        game_result = "GAME OVER"
                        game_over = True
                    fence_positioning(fence_x[f], fence_y[f], f)

                # Bat Movement
                for b in range(number_of_bat):
                    bat_x[b] += bat_x_change[b]
                    # collision
                    is_collision = enemy_arrow_collision(bat_x[b], bat_y[b], arrow_x, arrow_y)
                    if is_collision and arrow_state == "ON":
                        score_value += 1
                        arrow_state = "OFF"
                        bat_x[b] = -400
                        bat_y[b] = -400
                        bat_x_change[b] = 0
                    # Game over collision
                    is_collision = enemy_player_collision(bat_x[b], bat_y[b], player_x, player_y)
                    if is_collision:
                        game_result = "GAME OVER"
                        game_over = True
                    bat_positioning(bat_x[b], bat_y[b], b)

                # Fence and Bat Reset
                if fence_x[f] <= -400:
                    count += 1
                    fence_image = []
                    fence_x = []
                    fence_y = []
                    fence_x_change = []
                    number_of_fences = random.randint(1, 3)
                    for f in range(number_of_fences):
                        fence_image.append(pygame.image.load('fence.png'))
                        fence_x.append(random.randint(1500, 1800))
                        fence_y.append(570)
                        fence_x_change.append(-3)

                    bat_image = []
                    bat_x = []
                    bat_y = []
                    bat_x_change = []
                    number_of_bat = random.randint(0, 2)
                    for b in range(number_of_bat):
                        bat_image.append(pygame.image.load('bat.png'))
                        bat_x.append(random.randint(1500, 1800))
                        bat_y.append(random.randint(100, 550))
                        bat_x_change.append(-3)

            pygame.display.update()

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    game_loop()