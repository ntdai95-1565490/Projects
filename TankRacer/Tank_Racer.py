# The program uses third-party icons, which are credited to:

# Icons made by <a href="https://www.flaticon.com/authors/creaticca-creative-agency" title="Creaticca Creative Agency">Creaticca Creative Agency</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
# Icons made by <a href="https://www.flaticon.com/free-icon/airplane_2646745?related_item_id=2646727&term=airplane%20military" title="ultimatearm">ultimatearm</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
# Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
# Icons made by <a href="https://www.flaticon.com/free-icon/missile_2809728?related_item_id=2762183&term=missile" title="smalllikeart">smalllikeart</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
# Icons made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
# Icons made by <a href="https://www.flaticon.com/authors/nhor-phai" title="Nhor Phai">Nhor Phai</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
# Icons made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
# Icons made by <a href="https://www.flaticon.com/authors/smalllikeart" title="smalllikeart">smalllikeart</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
# Icons made by <a href="http://www.freepik.com/" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>

# The creator of the following program does not own any of the icons used below. All of the copyrights of the icons below belongs to the 
# creators mentioned above.

import pygame
import sys
import random
import math

def player_positioning(x, y):
    screen.blit(player_image, (x, y))

def bullet_positioning(x, y):
    screen.blit(bullet_image, (x, y))

def medal_positioning(x, y, m):
    screen.blit(medal_image[m], (x, y))

def landmine_positioning(x, y, l):
    screen.blit(landmine_image[l], (x, y))

def airplane_positioning(x, y, a):
    screen.blit(airplane_image[a], (x, y))

def bomb_positioning(x, y, b):
    screen.blit(bomb_image[b], (x, y))

def headquarter_positioning(x, y, h):
    screen.blit(headquarter_image[h], (x, y))

def rocket_positioning(x, y):
    screen.blit(rocket_image, (x, y))

# Collision
def collision(object1_x, object1_y, object2_x, object2_y):
    distance = math.sqrt((object1_x - object2_x)**2 + (object1_y - object2_y)**2)
    if distance < 50:
        return True
    else:
        return False

# Showing welcome, end, and score texts on the screen
def game_start_text():
    first_line_font = pygame.font.Font('freesansbold.ttf', 50)
    font = pygame.font.Font('freesansbold.ttf', 30)
    last_line_font = pygame.font.Font('freesansbold.ttf', 40)

    lines = ["Welcome to Tank Racer!", "Use the up, down, left, and right arrow", "keys to move around with the tank.", "To shoot down airplanes, and military", "bases, press space to shoot bullets.", "Press s to start the game."]
    for index, value in enumerate(lines):
        if index == 0:
            line = first_line_font.render(value, True, (0, 0, 128))
        elif index == 5:
            line = last_line_font.render(value, True, (0, 0, 128))
        else:
            line = font.render(value, True, (0, 0, 128))

        line_surface = pygame.Surface(line.get_size())
        line_surface.fill((255, 255, 255))
        line_surface.blit(line, (0, 0))

        if index == 0:
            screen.blit(line_surface, (210, 150))
        elif index == 5:
            screen.blit(line_surface, (260, 600))
        else:
            screen.blit(line_surface, (225, 250 + index * 50))

def game_over_text(score_value, game_result):
    first_line_font = pygame.font.Font('freesansbold.ttf', 60)
    font = pygame.font.Font('freesansbold.ttf', 35)

    lines = [game_result, f"Your score is {score_value}", "Press p if you want to play again, otherwise", " close the window or press e to exit."]
    for index, value in enumerate(lines):
        if index >= 2:
            line = font.render(value, True, (0, 0, 128))
        else:
            line = first_line_font.render(value, True, (0, 0, 128))

        line_surface = pygame.Surface(line.get_size())
        line_surface.fill((255, 255, 255))
        line_surface.blit(line, (0, 0))

        if index >= 2:
            screen.blit(line_surface, (125, 550 + (index - 2) * 50))
        else:
            screen.blit(line_surface, (275, 150 + index * 200))

def show_score(score_value):
    font = pygame.font.Font('freesansbold.ttf', 45)
    score = font.render("Score : " + str(score_value), True, (127, 255, 0))
    score_surface = pygame.Surface(score.get_size())
    score_surface.fill((101, 67, 33))
    score_surface.blit(score, (0, 0))
    screen.blit(score_surface, (10, 10))

# Main Game Loop
def game_loop():
    # Initializing the game
    pygame.init()

    game_open = True
    game_running = False
    game_over = False

    # Screen
    global screen
    screen = pygame.display.set_mode((1000, 780))
    # Backgrounds
    first_last_background = pygame.image.load("first_last_background.png").convert()
    background = pygame.image.load("background.png").convert()
    # Caption and Icon
    icon = pygame.image.load("tank_icon.png").convert()
    pygame.display.set_caption("Tank Racer")
    pygame.display.set_icon(icon)
    # Clock
    clock = pygame.time.Clock()

    # Player
    global player_image
    player_image = pygame.image.load("tank.png")
    player_x = 200
    player_y = 630
    player_x_change = 0
    player_y_change = 0

    # Bullet
    global bullet_image
    bullet_image = pygame.image.load('bullet.png')
    bullet_x = 0
    bullet_y = 0
    bullet_y_change = -15
    bullet_state = "OFF"

    # Landmine
    global landmine_image
    landmine_image = []
    landmine_x = []
    landmine_y = []
    landmine_y_change = []
    number_of_landmines = 6
    for i in range(number_of_landmines):
        landmine_image.append(pygame.image.load('landmine.png'))
        landmine_x.append(random.choice([200, 350, 500, 650]))
        landmine_y_change.append(5)
        if i <= 2:
            landmine_y.append(0 - i * 150)
        else:
            landmine_y.append(0 - (i + 1) * 150)

    # Medal
    global medal_image
    medal_image = []
    medal_x = []
    medal_y = []
    medal_y_change = []
    number_of_medals = 2
    for i in range(number_of_medals):
        medal_image.append(pygame.image.load('medal.png'))
        medal_x.append(random.choice([200, 350, 500, 650]))
        medal_y.append(-450 - 600 * i)
        medal_y_change.append(5)

    # Airplane
    global airplane_image
    airplane_image = []
    airplane_x = []
    airplane_y = []
    airplane_x_change = []
    airplanes_remaining = 2
    number_of_airplanes = 2
    for i in range(number_of_airplanes):
        airplane_image.append(pygame.image.load('airplane.png'))
        airplane_x.append(random.randint(200, 655))
        airplane_y.append(0)
        airplane_x_change.append(5 * (-1) ** (i + 1))

    # Bomb
    global bomb_image
    bomb_image = []
    bomb_x = []
    bomb_y = []
    bomb_y_change = []
    number_of_bombs = 2
    for _ in range(number_of_bombs):
        bomb_image.append(pygame.image.load('bomb.png'))
        bomb_x.append(random.choice([200, 350, 500, 650]))
        bomb_y.append(0)
        bomb_y_change.append(5)

    # Headquarter
    global headquarter_image
    headquarter_image = []
    headquarter_x = []
    headquarter_y = []
    headquarter_life_points = []
    number_of_headquarters = 4
    for i in range(number_of_headquarters):
        headquarter_image.append(pygame.image.load('headquarter.png'))
        headquarter_x.append(200 + i * 150)
        headquarter_y.append(0)
        headquarter_life_points.append(2)

    # Rocket
    global rocket_image
    rocket_image = pygame.image.load('rocket.png')
    rocket_x = 0
    rocket_y = random.randint(150, 630)
    rocket_x_change = 5

    # Count until next boss is coming
    count = 0
    # Player's score
    score_value = 0
    # Game result either game over if the player losses or congratulations if the player wins
    game_result = ""

    while game_open:
        # Clock
        clock.tick(60)
        # RGB
        screen.fill((50,205,50))
        # Background Image
        screen.blit(first_last_background, (0, 0))

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
            # Clock
            clock.tick(60)
            # RGB
            screen.fill((50,205,50))
            # Background Image
            screen.blit(background, (0, 0))
            
            while game_over:
                # Clock
                clock.tick(60)
                # RGB
                screen.fill((50,205,50))
                # Background Image
                screen.blit(first_last_background, (0, 0))
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
                        if player_y_change == 0:
                            player_x_change = -7
                    if event.key == pygame.K_RIGHT:
                        if player_y_change == 0:
                            player_x_change = 7
                    if event.key == pygame.K_UP:
                        if player_x_change == 0:
                            player_y_change = -7
                    if event.key == pygame.K_DOWN:
                        if player_x_change == 0:
                            player_y_change = 7
                    if event.key == pygame.K_SPACE:
                        if bullet_state == "OFF":
                            # Get the current x, y cordinate of the horse rider
                            bullet_state = "ON"
                            bullet_x = player_x
                            bullet_y = player_y
                            bullet_positioning(bullet_x, bullet_y)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        player_x_change = 0
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_y_change = 0

            # Player Movement
            player_x += player_x_change
            if player_x <= 200:
                player_x = 200
            elif player_x >= 655:
                player_x = 655

            player_y += player_y_change
            if player_y <= 0:
                player_y = 0
            elif player_y >= 630:
                player_y = 630
            player_positioning(player_x, player_y)

            # Bullet Movement
            if bullet_y <= 0:
                bullet_state = "OFF"

            if bullet_state == "ON":
                bullet_positioning(bullet_x, bullet_y)
                bullet_y += bullet_y_change

            # Showing score
            show_score(score_value)

            if count == 8 or count == 20:
                # Airplane Movement
                for a in range(number_of_airplanes):
                    airplane_x[a] += airplane_x_change[a]
                    if airplane_x[a] <= 200 or airplane_x[a] >= 655:
                        airplane_x_change[a] = -airplane_x_change[a]

                    # collision
                    is_collision = collision(airplane_x[a], airplane_y[a], bullet_x, bullet_y)
                    if is_collision and bullet_state == "ON":
                        score_value += 1
                        bullet_state = "OFF"
                        airplane_x[a] = -400
                        airplane_y[a] = -400
                        airplane_x_change[a] = 0
                        airplanes_remaining -= 1
                    
                    # Game over collision
                    is_collision = collision(airplane_x[a], airplane_y[a], player_x, player_y)
                    if is_collision:
                        game_result = "GAME OVER"
                        game_over = True

                    airplane_positioning(airplane_x[a], airplane_y[a], a)

                # Bomb Movement
                for b in range(number_of_bombs):
                    bomb_y[b] += bomb_y_change[b]
                    # Game over collision
                    is_collision = collision(bomb_x[b], bomb_y[a], player_x, player_y)
                    if is_collision:
                        game_result = "GAME OVER"
                        game_over = True
                    bomb_positioning(bomb_x[b], bomb_y[b], b)

                # Bomb Reset
                for b in range(number_of_bombs):
                    if bomb_y[b] >= 900:
                        bomb_x[b] = random.choice([200, 350, 500, 650])
                        bomb_y[b] = 0
                

                if airplanes_remaining == 0:
                    # Airplanes Reset
                    airplane_x = []
                    airplane_y = []
                    airplane_x_change = []
                    for i in range(number_of_airplanes):
                        airplane_x.append(random.randint(200, 655))
                        airplane_y.append(0)
                        airplane_x_change.append(5 * (-1) ** (i + 1))
                    airplanes_remaining = 2

                    # Landmine Reset
                    landmine_x = []
                    landmine_y = []
                    for i in range(number_of_landmines):
                        landmine_x.append(random.choice([200, 350, 500, 650]))
                        if i <= 2:
                            landmine_y.append(0 - i * 150)
                        else:
                            landmine_y.append(0 - (i + 1) * 150)

                    # Medal Reset
                    medal_x = []
                    medal_y = []
                    for i in range(number_of_medals):
                        medal_x.append(random.choice([200, 350, 500, 650]))
                        medal_y.append(-450 - 600 * i)

                    # Bomb Reset
                    bomb_x = []
                    bomb_y = []
                    for _ in range(number_of_bombs):
                        bomb_x.append(random.choice([200, 350, 500, 650]))
                        bomb_y.append(0)

                    count += 1

            elif count == 30:
                # Headquarter Movement
                for h in range(number_of_headquarters):
                    # collision
                    is_collision = collision(headquarter_x[h], headquarter_y[h], bullet_x, bullet_y)
                    if is_collision and bullet_state == "ON":
                        score_value += 1
                        headquarter_life_points[h] -= 1
                        bullet_state = "OFF"
                        if headquarter_life_points[h] == 0:
                            headquarter_x[h] = -400
                            headquarter_y[h] = -400
                    
                    # Game over collision
                    is_collision = collision(headquarter_x[h], headquarter_y[h], player_x, player_y)
                    if is_collision:
                        game_result = "GAME OVER"
                        game_over = True
                    headquarter_positioning(headquarter_x[h], headquarter_y[h], h)

                # Bomb Movement
                for b in range(number_of_bombs):
                    bomb_y[b] += bomb_y_change[b]
                    # Game over collision
                    is_collision = collision(bomb_x[b], bomb_y[b], player_x, player_y)
                    if is_collision:
                        game_result = "GAME OVER"
                        game_over = True
                    bomb_positioning(bomb_x[b], bomb_y[b], b)

                # Bomb Reset
                for b in range(number_of_bombs):
                    if bomb_y[b] >= 900:
                        bomb_x[b] = random.choice([200, 350, 500, 650])
                        bomb_y[b] = 0

                # Rocket Movement
                rocket_x += rocket_x_change
                # Game over collision
                is_collision = collision(rocket_x, rocket_y, player_x, player_y)
                if is_collision:
                    game_result = "GAME OVER"
                    game_over = True
                rocket_positioning(rocket_x, rocket_y)

                # Rocket Reset
                if rocket_x == 1000:
                    rocket_x = 0
                    rocket_y = random.randint(150, 630)

                # Destroying all bases and winning the game
                if sum(headquarter_life_points) == 0:
                    game_result = "Congratulations!"
                    game_over = True
            else:
                # Landmine Movement
                for l in range(number_of_landmines):
                    landmine_y[l] += landmine_y_change[l]
                    # Game over collision
                    is_collision = collision(landmine_x[l], landmine_y[l], player_x, player_y)
                    if is_collision:
                        game_result = "GAME OVER"
                        game_over = True
                    landmine_positioning(landmine_x[l], landmine_y[l], l)

                # Landmine Reset
                for l in range(number_of_landmines):
                    if landmine_y[l] >= 900:
                        count += 1
                        landmine_x[l] = random.choice([200, 350, 500, 650])
                        landmine_y[l] = -300

                # Medal Movement
                for m in range(number_of_medals):
                    medal_y[m] += medal_y_change[m]
                     # collision
                    is_collision = collision(medal_x[m], medal_y[m], player_x, player_y)
                    if is_collision:
                        score_value += 1
                    medal_positioning(medal_x[m], medal_y[m], m)

                # Medal Reset
                for m in range(number_of_medals):
                    if medal_y[m] >= 900:
                        medal_x[m] = random.choice([200, 350, 500, 650])
                        medal_y[m] = -300

            pygame.display.update()

        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    game_loop()