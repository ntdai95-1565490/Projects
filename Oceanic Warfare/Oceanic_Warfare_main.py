import sys
from os import path
import pygame as pg
import random
import time
import pickle
from Oceanic_Warfare_settings import *
from Oceanic_Warfare_sprites import *

class Main:
    def __init__(self):
        pg.init()
        #pg.mixer.music.load(path.join(path.join(path.dirname(__file__), "Music"), "background_music.wav"))
        #pg.mixer.music.set_volume(0.2)
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.first_background = pg.image.load(path.join(path.join(path.dirname(__file__), "Images"), "first_background.png")).convert()
        self.main_battle_background = pg.image.load(path.join(path.join(path.dirname(__file__), "Images"), "main_battle_background.png")).convert()
        self.main_setup_background = pg.image.load(path.join(path.join(path.dirname(__file__), "Images"), "main_setup_background.png")).convert()
        self.main_battle_background_x = 0
        self.main_battle_background_x_2 = self.main_battle_background.get_width()
        self.game_over_background = pg.image.load(path.join(path.join(path.dirname(__file__), "Images"), "game_over_background.png")).convert()
        self.game_win_background = pg.image.load(path.join(path.join(path.dirname(__file__), "Images"), "game_win_background.png")).convert()
        pg.display.set_caption(TITLE)
        self.icon = pg.image.load(path.join(path.join(path.dirname(__file__), "Images"), "icon.png")).convert()
        self.icon.set_colorkey(BLACK)
        pg.display.set_icon(self.icon)
        self.clock = pg.time.Clock()
        self.reset()

    def reset(self):
        self.game_open = True
        self.game_setup_running = False
        self.game_battle_running = False
        self.game_ending_lose = False
        self.game_ending_win = False
        self.computer_turn = False
        self.mouse_position = None
        self.list_of_button_texts = ["START GAME", "INSTRUCTIONS", "HIGHSCORES", "MUSIC ON/OFF", "SOUND ON/OFF", "EXIT GAME"]
        self.list_of_button_positions_x = None
        self.list_of_button_positions_y = None
        self.buttons_size_x = None
        self.buttons_size_y = None
        self.refresh_button_size_x = 100
        self.refresh_button_size_y = 90
        self.list_of_ships = ["cruiser", "submarine", "destroyer", "frigate", "aircraftcarrier"]
        self.selected_ship = None
        self.rotate_ship = None
        self.selected_cell = None
        self.selected_cell_main_battle = None
        self.selected_cell_main_battle_computer_turn = None
        self.player_grid = [[0 for _ in range(11)] for _ in range(11)]
        self.computer_grid = [[0 for _ in range(11)] for _ in range(11)]
        self.player_entered_grid = [[0 for _ in range(11)] for _ in range(11)]
        self.computer_entered_grid = [[0 for _ in range(11)] for _ in range(11)]
        self.missile_on = False
        self.missile_x_border = 0
        self.missile_position_y = 0
        self.player_ships_sunk = 0
        self.computer_ships_sunk = []
        self.player_score = 0

### GAME START SCREEN ###

    def game_start_screen(self):
        while self.game_open:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game_open = False

                if event.type == pg.MOUSEBUTTONDOWN:
                    for i in range(6):
                        if i == 0 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y: 
                            self.game_setup_running = True
                        elif i == 1 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y:
                            # Instructions here
                            pass
                        elif i == 2 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y:
                            # High scores
                            pass
                        elif i == 3 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y:
                            # Music on/off
                            pass
                        elif i == 4 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y:
                            # Sound on/off
                            pass
                        elif i == 5 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y:
                            self.game_open = False

            self.run_main_setup()
            self.screen.blit(self.first_background, (0, 0))
            self.initial_message_to_screen(self.screen)
            self.loading_buttons_on_first_page(self.screen, self.mouse_position, self.list_of_button_texts)

            pg.display.update()
            self.clock.tick(FPS)

        pg.quit()
        sys.exit()

    def initial_message_to_screen(self, screen):
        line_font = pg.font.Font('freesansbold.ttf', 60)
        line = line_font.render("Welcome to Oceanic Warfare!", True, YELLOW)
        line_surface = pg.Surface(line.get_size())
        line_surface.fill(BLACK)
        line_surface.blit(line, (0, 0))
        self.screen.blit(line_surface, (325, 150))

    def loading_buttons_on_first_page(self, screen, mouse_position, list_of_button_texts):
        self.mouse_position = pg.mouse.get_pos()
        self.list_of_button_positions_x = [100, 575, 1050, 100, 575, 1050]
        self.list_of_button_positions_y = [350, 350, 350, 550, 550, 550]
        self.buttons_size_x = 350
        self.buttons_size_y = 100

        # Button Texts
        for i in range(6):
            if self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y: 
                pg.draw.rect(self.screen, RED, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y])
                pg.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y], 5)
            else: 
                pg.draw.rect(self.screen, GREEN, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y])
                pg.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y], 5)

            font = pg.font.Font('freesansbold.ttf', 40)
            text_font = font.render(self.list_of_button_texts[i], True, BLACK)
            text_font_width = text_font.get_width()
            text_font_height = text_font.get_height()
            self.screen.blit(text_font, (self.list_of_button_positions_x[i] + (self.buttons_size_x - text_font_width) // 2, self.list_of_button_positions_y[i] + (self.buttons_size_y - text_font_height) // 2))

    def instructions_screen(self):
        pass

### GAME MAIN SETUP SCREEN ###

    def loading_sprites_main_setup(self, screen):
        self.all_sprites_group = pg.sprite.Group()
        self.frigate = Frigate()
        self.all_sprites_group.add(self.frigate)
        self.aircraftcarrier = AircraftCarrier()
        self.all_sprites_group.add(self.aircraftcarrier)
        self.cruiser = Cruiser()
        self.all_sprites_group.add(self.cruiser)
        self.destroyer = Destroyer()
        self.all_sprites_group.add(self.destroyer)
        self.submarine = Submarine()
        self.all_sprites_group.add(self.submarine)
        self.rotation_sign = []
        for i in range(5):
            self.rotation_sign.append(RotationSign(i))
            self.all_sprites_group.add(self.rotation_sign[i])

    def run_main_setup(self):
        self.loading_sprites_main_setup(self.screen)
        while self.game_setup_running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game_setup_running = False
                    self.game_open = False

                if event.type == pg.MOUSEBUTTONDOWN:
                    for i in range(13):
                        if i == 0 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y \
                        and any(5 in row for row in self.player_grid) and any(4 in row for row in self.player_grid) and any(3 in row for row in self.player_grid) and any(2 in row for row in self.player_grid) and any(1 in row for row in self.player_grid): 
                            self.generating_computer_ships(self.player_entered_grid)
                            self.game_battle_running = True
                        elif i == 2 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y:
                            # Sound on/off
                            pass
                        elif i == 4 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y:
                            self.game_setup_running = False
                        elif i == 6 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y:
                            self.game_setup_running = False
                            self.game_open = False
                        elif i >= 8 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.refresh_button_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.refresh_button_size_y:
                            self.rotate_ship = self.list_of_ships[i - 8]
                    
                    for ship in self.all_sprites_group:
                        if ship == self.cruiser and ship.rect.collidepoint(event.pos):
                            self.selected_ship = self.list_of_ships[0]
                            if any(5 in row for row in self.player_grid):
                                for row_index in range(11):
                                    for column_index in range(11):
                                        if self.player_grid[row_index][column_index] == 5:
                                            self.player_grid[row_index][column_index] = 0
                        elif ship == self.submarine and ship.rect.collidepoint(event.pos):
                            self.selected_ship = self.list_of_ships[1]
                            if any(1 in row for row in self.player_grid):
                                for row_index in range(11):
                                    for column_index in range(11):
                                        if self.player_grid[row_index][column_index] == 1:
                                            self.player_grid[row_index][column_index] = 0
                        elif ship == self.destroyer and ship.rect.collidepoint(event.pos):
                            self.selected_ship = self.list_of_ships[2]
                            if any(3 in row for row in self.player_grid):
                                for row_index in range(11):
                                    for column_index in range(11):
                                        if self.player_grid[row_index][column_index] == 3:
                                            self.player_grid[row_index][column_index] = 0
                        elif ship == self.frigate and ship.rect.collidepoint(event.pos):
                            self.selected_ship = self.list_of_ships[3]
                            if any(2 in row for row in self.player_grid):
                                for row_index in range(11):
                                    for column_index in range(11):
                                        if self.player_grid[row_index][column_index] == 2:
                                            self.player_grid[row_index][column_index] = 0
                        elif ship == self.aircraftcarrier and ship.rect.collidepoint(event.pos):
                            self.selected_ship = self.list_of_ships[4]
                            if any(4 in row for row in self.player_grid):
                                for row_index in range(11):
                                    for column_index in range(11):
                                        if self.player_grid[row_index][column_index] == 4:
                                            self.player_grid[row_index][column_index] = 0
            
                if event.type == pg.MOUSEBUTTONUP and self.selected_ship != None:
                    if self.selected_ship == "cruiser" and self.cruiser.position == "horizontal" and 1 < self.selected_cell[0] < 9 and self.player_grid[self.selected_cell[1]][self.selected_cell[0] - 2] == 0 \
                    and self.player_grid[self.selected_cell[1]][self.selected_cell[0] - 1] == 0 and self.player_grid[self.selected_cell[1]][self.selected_cell[0]] == 0 \
                    and self.player_grid[self.selected_cell[1]][self.selected_cell[0] + 1] == 0 and self.player_grid[self.selected_cell[1]][self.selected_cell[0] + 2] == 0:
                        for i in range(5):
                            self.player_grid[self.selected_cell[1]][self.selected_cell[0] - 2 + i] = 5
                    elif self.selected_ship == "cruiser" and self.cruiser.position == "vertical" and 1 < self.selected_cell[1] < 9 and self.player_grid[self.selected_cell[1] - 2][self.selected_cell[0]] == 0 \
                    and self.player_grid[self.selected_cell[1] - 1][self.selected_cell[0]] == 0 and self.player_grid[self.selected_cell[1]][self.selected_cell[0]] == 0 \
                    and self.player_grid[self.selected_cell[1] + 1][self.selected_cell[0]] == 0 and self.player_grid[self.selected_cell[1] + 2][self.selected_cell[0]] == 0:
                        for i in range(5):
                            self.player_grid[self.selected_cell[1] - 2 + i][self.selected_cell[0]] = 5
                    elif self.selected_ship == "aircraftcarrier" and self.aircraftcarrier.position == "horizontal" and 1 < self.selected_cell[0] < 10 and self.selected_cell[1] < 10 \
                    and self.player_grid[self.selected_cell[1]][self.selected_cell[0] - 2] == 0 and self.player_grid[self.selected_cell[1]][self.selected_cell[0] - 1] == 0 \
                    and self.player_grid[self.selected_cell[1]][self.selected_cell[0]] == 0 and self.player_grid[self.selected_cell[1]][self.selected_cell[0] + 1] == 0 \
                    and self.player_grid[self.selected_cell[1] + 1][self.selected_cell[0] - 2] == 0 and self.player_grid[self.selected_cell[1] + 1][self.selected_cell[0] - 1] == 0 \
                    and self.player_grid[self.selected_cell[1] + 1][self.selected_cell[0]] == 0 and self.player_grid[self.selected_cell[1] + 1][self.selected_cell[0] + 1] == 0:
                        for i in range(4):
                            self.player_grid[self.selected_cell[1]][self.selected_cell[0] - 2 + i] = 4
                            self.player_grid[self.selected_cell[1] + 1][self.selected_cell[0] - 2 + i] = 4
                    elif self.selected_ship == "aircraftcarrier" and self.aircraftcarrier.position == "vertical" and self.selected_cell[0] < 10 and 0 < self.selected_cell[1] < 9 \
                    and self.player_grid[self.selected_cell[1] - 1][self.selected_cell[0] + 1] == 0 and self.player_grid[self.selected_cell[1] - 1][self.selected_cell[0]] == 0 \
                    and self.player_grid[self.selected_cell[1]][self.selected_cell[0] + 1] == 0 and self.player_grid[self.selected_cell[1]][self.selected_cell[0]] == 0 \
                    and self.player_grid[self.selected_cell[1] + 1][self.selected_cell[0] + 1] == 0 and self.player_grid[self.selected_cell[1] + 1][self.selected_cell[0]] == 0 \
                    and self.player_grid[self.selected_cell[1] + 2][self.selected_cell[0] + 1] == 0 and self.player_grid[self.selected_cell[1] + 2][self.selected_cell[0]] == 0:
                        for i in range(4):
                            self.player_grid[self.selected_cell[1] - 1 + i][self.selected_cell[0]] = 4
                            self.player_grid[self.selected_cell[1] - 1 + i][self.selected_cell[0] + 1] = 4
                    elif self.selected_ship == "destroyer" and self.destroyer.position == "horizontal" and 1 < self.selected_cell[0] < 10 \
                    and self.player_grid[self.selected_cell[1]][self.selected_cell[0] - 2] == 0 and self.player_grid[self.selected_cell[1]][self.selected_cell[0] - 1] == 0 \
                    and self.player_grid[self.selected_cell[1]][self.selected_cell[0]] == 0 and self.player_grid[self.selected_cell[1]][self.selected_cell[0] + 1] == 0:
                        for i in range(4):
                            self.player_grid[self.selected_cell[1]][self.selected_cell[0] - 2 + i] = 3
                    elif self.selected_ship == "destroyer" and self.destroyer.position == "vertical" and 0 < self.selected_cell[1] < 9 \
                    and self.player_grid[self.selected_cell[1] - 1][self.selected_cell[0]] == 0 and self.player_grid[self.selected_cell[1]][self.selected_cell[0]] == 0 \
                    and self.player_grid[self.selected_cell[1] + 1][self.selected_cell[0]] == 0 and self.player_grid[self.selected_cell[1] + 2][self.selected_cell[0]] == 0:
                        for i in range(4):
                            self.player_grid[self.selected_cell[1] - 1 + i][self.selected_cell[0]] = 3
                    elif self.selected_ship == "frigate" and self.frigate.position == "horizontal" and 0 < self.selected_cell[0] < 10 and self.player_grid[self.selected_cell[1]][self.selected_cell[0] - 1] == 0 \
                    and self.player_grid[self.selected_cell[1]][self.selected_cell[0]] == 0 and self.player_grid[self.selected_cell[1]][self.selected_cell[0] + 1] == 0:
                        for i in range(3):
                            self.player_grid[self.selected_cell[1]][self.selected_cell[0] - 1 + i] = 2
                    elif self.selected_ship == "frigate" and self.frigate.position == "vertical" and 0 < self.selected_cell[1] < 10 and self.player_grid[self.selected_cell[1] - 1][self.selected_cell[0]] == 0 \
                    and self.player_grid[self.selected_cell[1]][self.selected_cell[0]] == 0 and self.player_grid[self.selected_cell[1] + 1][self.selected_cell[0]] == 0:
                        for i in range(3):
                            self.player_grid[self.selected_cell[1] - 1 + i][self.selected_cell[0]] = 2
                    elif self.selected_ship == "submarine" and self.submarine.position == "horizontal" and 0 < self.selected_cell[0] < 10 and self.player_grid[self.selected_cell[1]][self.selected_cell[0] - 1] == 0 \
                    and self.player_grid[self.selected_cell[1]][self.selected_cell[0]] == 0 and self.player_grid[self.selected_cell[1]][self.selected_cell[0] + 1] == 0:
                        for i in range(3):
                            self.player_grid[self.selected_cell[1]][self.selected_cell[0] - 1 + i] = 1
                    elif self.selected_ship == "submarine" and self.submarine.position == "vertical" and 0 < self.selected_cell[1] < 10 and self.player_grid[self.selected_cell[1] - 1][self.selected_cell[0]] == 0 \
                    and self.player_grid[self.selected_cell[1]][self.selected_cell[0]] == 0 and self.player_grid[self.selected_cell[1] + 1][self.selected_cell[0]] == 0:
                        for i in range(3):
                            self.player_grid[self.selected_cell[1] - 1 + i][self.selected_cell[0]] = 1

                    self.selected_ship = None

            if TABLE_POSITION_X <= self.mouse_position[0] <= TABLE_POSITION_X + TABLE_SIZE and TABLE_POSITION_Y <= self.mouse_position[1] <= TABLE_POSITION_Y + TABLE_SIZE:
                self.selected_cell = [(self.mouse_position[0] - TABLE_POSITION_X) // CELL_SIZE, (self.mouse_position[1] - TABLE_POSITION_Y) // CELL_SIZE]
            
            self.run_main_battle()
            self.update_main_setup(self.rotate_ship, self.selected_ship, self.mouse_position, self.player_grid, self.game_battle_running, self.computer_turn, self.missile_position_y, self.missile_on)
            self.draw_main_setup()

            if self.game_setup_running == False and self.game_open:
                self.reset()

            pg.display.update()
            self.clock.tick(FPS)

    def generating_computer_ships(self, player_entered_grid):
        computer_ship_sizes = [[3, 1], [3, 1], [4, 1], [4, 2], [5, 1]]
        for index, computer_ship_size in enumerate(computer_ship_sizes):
            valid = False
            while not valid:
                computer_ship_x = random.randint(0, 10)
                computer_ship_y = random.randint(0, 10)
                computer_ship_position = random.choice(["horizontal", "vertical"])
                valid = self.validate(self.player_entered_grid, computer_ship_size, computer_ship_x, computer_ship_y, computer_ship_position)

            if computer_ship_position == "horizontal":
                for j in range(computer_ship_size[1]):
                    for i in range(computer_ship_size[0]):
                        self.player_entered_grid[computer_ship_y + j][computer_ship_x + i] = index + 1
            else:
                for j in range(computer_ship_size[1]):
                    for i in range(computer_ship_size[0]):
                        self.player_entered_grid[computer_ship_y + i][computer_ship_x + j] = index + 1

    def validate(self, player_entered_grid, computer_ship_size, computer_ship_x, computer_ship_y, computer_ship_position):
        if computer_ship_position == "horizontal" and (computer_ship_x + computer_ship_size[0] > 10 or computer_ship_y + computer_ship_size[1] > 10):
            return False
        elif computer_ship_position == "vertical" and (computer_ship_x + computer_ship_size[1] > 10 or computer_ship_y + computer_ship_size[0] > 10):
            return False
        elif computer_ship_position == "horizontal":
            for j in range(computer_ship_size[1]):
                for i in range(computer_ship_size[0]):
                    if self.player_entered_grid[computer_ship_y + j][computer_ship_x + i] != 0:
                        return False
        elif computer_ship_position == "vertical":
            for j in range(computer_ship_size[1]):
                for i in range(computer_ship_size[0]):
                    if self.player_entered_grid[computer_ship_y + i][computer_ship_x + j] != 0:
                        return False
        return True

    def update_main_setup(self, rotate_ship, selected_ship, mouse_position, player_grid, game_battle_running, computer_turn, missile_position_y, missile_on):
        self.all_sprites_group.update(self.rotate_ship, self.selected_ship, self.mouse_position, self.player_grid, self.game_battle_running, self.computer_turn, self.missile_position_y, self.missile_on, self.computer_grid, self.computer_ships_sunk)
        self.rotate_ship = False

    def draw_main_setup(self):
        self.screen.blit(self.main_setup_background, (0, 0))
        self.message_to_screen_main_setup(self.screen)
        self.loading_buttons_on_main_setup(self.screen, self.mouse_position, self.list_of_button_texts, self.buttons_size_x, self.buttons_size_y)
        self.selected_cell_fill(self.screen)
        self.table_cell_draw_main_setup(self.screen)
        self.all_sprites_group.draw(self.screen)

    def selected_cell_fill(self, screen):
        for row_index in range(11):
            for column_index in range(11):
                if self.player_grid[row_index][column_index] != 0:
                    pg.draw.rect(self.screen, PINK, (column_index * CELL_SIZE + TABLE_POSITION_X, row_index * CELL_SIZE + TABLE_POSITION_Y, CELL_SIZE, CELL_SIZE))

        if self.selected_ship == "cruiser" and self.cruiser.position == "horizontal" and TABLE_POSITION_X + 2 * CELL_SIZE < self.mouse_position[0] < TABLE_POSITION_X - 2 * CELL_SIZE + TABLE_SIZE and TABLE_POSITION_Y < self.mouse_position[1] < TABLE_POSITION_Y + TABLE_SIZE:
            pg.draw.rect(self.screen, PINK, ((self.selected_cell[0] - 2) * CELL_SIZE + TABLE_POSITION_X, self.selected_cell[1] * CELL_SIZE + TABLE_POSITION_Y, 5 * CELL_SIZE, CELL_SIZE))
        elif self.selected_ship == "cruiser" and self.cruiser.position == "vertical" and TABLE_POSITION_X < self.mouse_position[0] < TABLE_POSITION_X + TABLE_SIZE and TABLE_POSITION_Y + 2 * CELL_SIZE < self.mouse_position[1] < TABLE_POSITION_Y - 2 * CELL_SIZE + TABLE_SIZE:
            pg.draw.rect(self.screen, PINK, (self.selected_cell[0] * CELL_SIZE + TABLE_POSITION_X, (self.selected_cell[1] - 2) * CELL_SIZE + TABLE_POSITION_Y, CELL_SIZE, 5 * CELL_SIZE))
        elif self.selected_ship == "aircraftcarrier" and self.aircraftcarrier.position == "horizontal" and TABLE_POSITION_X + 2 * CELL_SIZE < self.mouse_position[0] < TABLE_POSITION_X - CELL_SIZE + TABLE_SIZE and TABLE_POSITION_Y < self.mouse_position[1] < TABLE_POSITION_Y - CELL_SIZE + TABLE_SIZE:
            pg.draw.rect(self.screen, PINK, ((self.selected_cell[0] - 2) * CELL_SIZE + TABLE_POSITION_X, self.selected_cell[1] * CELL_SIZE + TABLE_POSITION_Y, 4 * CELL_SIZE, 2 * CELL_SIZE))
        elif self.selected_ship == "aircraftcarrier" and self.aircraftcarrier.position == "vertical" and TABLE_POSITION_X < self.mouse_position[0] < TABLE_POSITION_X - CELL_SIZE + TABLE_SIZE and TABLE_POSITION_Y + CELL_SIZE < self.mouse_position[1] < TABLE_POSITION_Y - 2 * CELL_SIZE + TABLE_SIZE:
            pg.draw.rect(self.screen, PINK, (self.selected_cell[0] * CELL_SIZE + TABLE_POSITION_X, (self.selected_cell[1] - 1) * CELL_SIZE + TABLE_POSITION_Y, 2 * CELL_SIZE, 4 * CELL_SIZE))
        elif self.selected_ship == "destroyer" and self.destroyer.position == "horizontal" and TABLE_POSITION_X + 2 * CELL_SIZE < self.mouse_position[0] < TABLE_POSITION_X - CELL_SIZE + TABLE_SIZE and TABLE_POSITION_Y < self.mouse_position[1] < TABLE_POSITION_Y + TABLE_SIZE:
            pg.draw.rect(self.screen, PINK, ((self.selected_cell[0] - 2) * CELL_SIZE + TABLE_POSITION_X, self.selected_cell[1] * CELL_SIZE + TABLE_POSITION_Y, 4 * CELL_SIZE, CELL_SIZE))
        elif self.selected_ship == "destroyer" and self.destroyer.position == "vertical" and TABLE_POSITION_X < self.mouse_position[0] < TABLE_POSITION_X + TABLE_SIZE and TABLE_POSITION_Y + 2 * CELL_SIZE < self.mouse_position[1] < TABLE_POSITION_Y - CELL_SIZE + TABLE_SIZE:
            pg.draw.rect(self.screen, PINK, (self.selected_cell[0] * CELL_SIZE + TABLE_POSITION_X, (self.selected_cell[1] - 1) * CELL_SIZE + TABLE_POSITION_Y, CELL_SIZE, 4 * CELL_SIZE))
        elif self.selected_ship == "frigate" and self.frigate.position == "horizontal" and TABLE_POSITION_X + CELL_SIZE < self.mouse_position[0] < TABLE_POSITION_X - CELL_SIZE + TABLE_SIZE and TABLE_POSITION_Y < self.mouse_position[1] < TABLE_POSITION_Y + TABLE_SIZE:
            pg.draw.rect(self.screen, PINK, ((self.selected_cell[0] - 1) * CELL_SIZE + TABLE_POSITION_X, self.selected_cell[1] * CELL_SIZE + TABLE_POSITION_Y, 3 * CELL_SIZE, CELL_SIZE))
        elif self.selected_ship == "frigate" and self.frigate.position == "vertical" and TABLE_POSITION_X < self.mouse_position[0] < TABLE_POSITION_X + TABLE_SIZE and TABLE_POSITION_Y + CELL_SIZE < self.mouse_position[1] < TABLE_POSITION_Y - CELL_SIZE + TABLE_SIZE:
            pg.draw.rect(self.screen, PINK, (self.selected_cell[0] * CELL_SIZE + TABLE_POSITION_X, (self.selected_cell[1] - 1) * CELL_SIZE + TABLE_POSITION_Y, CELL_SIZE, 3 * CELL_SIZE))
        elif self.selected_ship == "submarine" and self.submarine.position == "horizontal" and TABLE_POSITION_X + CELL_SIZE < self.mouse_position[0] < TABLE_POSITION_X - CELL_SIZE + TABLE_SIZE and TABLE_POSITION_Y < self.mouse_position[1] < TABLE_POSITION_Y + TABLE_SIZE:
            pg.draw.rect(self.screen, PINK, ((self.selected_cell[0] - 1) * CELL_SIZE + TABLE_POSITION_X, self.selected_cell[1] * CELL_SIZE + TABLE_POSITION_Y, 3 * CELL_SIZE, CELL_SIZE))
        elif self.selected_ship == "submarine" and self.submarine.position == "vertical" and TABLE_POSITION_X < self.mouse_position[0] < TABLE_POSITION_X + TABLE_SIZE and TABLE_POSITION_Y + CELL_SIZE < self.mouse_position[1] < TABLE_POSITION_Y - CELL_SIZE + TABLE_SIZE:
            pg.draw.rect(self.screen, PINK, (self.selected_cell[0] * CELL_SIZE + TABLE_POSITION_X, (self.selected_cell[1] - 1) * CELL_SIZE + TABLE_POSITION_Y, CELL_SIZE, 3 * CELL_SIZE))

    def message_to_screen_main_setup(self, screen):
        line_font = pg.font.Font('freesansbold.ttf', 60)
        line = line_font.render("Battleship formation!", True, YELLOW)
        line_surface = pg.Surface(line.get_size())
        line_surface.fill(BLACK)
        line_surface.blit(line, (0, 0))
        self.screen.blit(line_surface, (825, 5))

    def table_cell_draw_main_setup(self, screen):
        pg.draw.rect(self.screen, BLACK, (TABLE_POSITION_X, TABLE_POSITION_Y, TABLE_SIZE, TABLE_SIZE), 5)
        for i in range(1, 11):
            pg.draw.line(self.screen, BLACK, (TABLE_POSITION_X + i * CELL_SIZE, TABLE_POSITION_Y), (TABLE_POSITION_X + i * CELL_SIZE, TABLE_POSITION_Y + TABLE_SIZE), 5)
            pg.draw.line(self.screen, BLACK, (TABLE_POSITION_X, TABLE_POSITION_Y + i * CELL_SIZE), (TABLE_POSITION_X + TABLE_SIZE, TABLE_POSITION_Y + i * CELL_SIZE), 5)

    def loading_buttons_on_main_setup(self, screen, mouse_position, list_of_button_texts, buttons_size_x, buttons_size_y):
        self.mouse_position = pg.mouse.get_pos()
        self.list_of_button_texts = ["START", "GAME", "SOUND", "ON/OFF", "MAIN", "PAGE", "EXIT", "GAME"]
        self.list_of_button_positions_x = [785, 785, 965, 965, 1145, 1145, 1325, 1325, 800, 800, 800, 800, 800]
        self.list_of_button_positions_y = [665, 705, 665, 705, 665, 705, 665, 705, 90, 205, 320, 435, 550]
        self.buttons_size_x = 170
        self.buttons_size_y = 110

        # Button Texts
        for i in range(13):
            if i < 8 and i % 2 == 0 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y: 
                pg.draw.rect(self.screen, RED, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y])
                pg.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y], 5)
            elif i >= 8 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.refresh_button_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.refresh_button_size_y:
                pg.draw.rect(self.screen, GREEN, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.refresh_button_size_x, self.refresh_button_size_y])
                pg.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.refresh_button_size_x, self.refresh_button_size_y], 5)
            elif i < 8 and i % 2 == 0: 
                pg.draw.rect(self.screen, GREEN, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y])
                pg.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y], 5)
            elif i >= 8:
                pg.draw.rect(self.screen, YELLOW, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.refresh_button_size_x, self.refresh_button_size_y])
                pg.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.refresh_button_size_x, self.refresh_button_size_y], 5)
            
        for i in range(8):
            font = pg.font.Font('freesansbold.ttf', 40)
            text_font = font.render(self.list_of_button_texts[i], True, BLACK)
            text_font_width = text_font.get_width()
            text_font_height = text_font.get_height()
            self.screen.blit(text_font, (self.list_of_button_positions_x[i] + (self.buttons_size_x - text_font_width) // 2, self.list_of_button_positions_y[i] + (self.buttons_size_y - text_font_height) // 4))

### GAME MAIN BATTLE SCREEN ###
    
    def game_ending_win_check(self):
        self.computer_ships_sunk = []
        for i in range(5):
            if sum(ship_type.count(i + 1) for ship_type in self.player_entered_grid) == 0:
                self.computer_ships_sunk.append(i + 1)

    def run_main_battle(self):
        self.missile = Missile()
        self.all_sprites_group.add(self.missile)
        for row_index, row in enumerate(self.player_grid):
            for column_index, column in enumerate(row):
                self.computer_entered_grid[row_index][column_index] = column

        for row_index, row in enumerate(self.player_entered_grid):
            for column_index, column in enumerate(row):
                self.computer_grid[row_index][column_index] = column

        while self.game_battle_running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game_battle_running = False
                    self.game_setup_running = False
                    self.game_open = False

                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.missile_on == False:
                        self.selected_cell_main_battle = [(self.mouse_position[0] - TABLE_POSITION_X_MAIN_BATTLE) // CELL_SIZE, (self.mouse_position[1] - TABLE_POSITION_Y) // CELL_SIZE]
                    if TABLE_POSITION_X_MAIN_BATTLE > self.mouse_position[0] or self.mouse_position[0] > TABLE_POSITION_X_MAIN_BATTLE + TABLE_SIZE or TABLE_POSITION_Y > self.mouse_position[1] or self.mouse_position[1] > TABLE_POSITION_Y + TABLE_SIZE or \
                    self.player_entered_grid[self.selected_cell_main_battle[0]][self.selected_cell_main_battle[1]] ==  "miss" or self.player_entered_grid[self.selected_cell_main_battle[0]][self.selected_cell_main_battle[1]] ==  "hit":
                        self.selected_cell_main_battle = None
                    
                    for i in range(6):
                        if i == 0 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y:
                            # Sound on/off
                            pass
                        elif i == 2 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y:
                            self.game_battle_running = False
                            self.game_setup_running = False
                        elif i == 4 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y:
                            self.game_battle_running = False
                            self.game_setup_running = False
                            self.game_open = False

            self.update_main_battle(self.rotate_ship, self.selected_ship, self.mouse_position, self.player_grid, self.game_battle_running, self.computer_turn, self.missile_position_y, self.missile_on)
            self.draw_main_battle()

            self.game_ending_win_check()
            if len(self.computer_ships_sunk) == 5:
                self.game_ending_win = True
                self.game_win_screen()

            if self.game_battle_running == False and self.game_setup_running == False and self.game_open:
                self.reset()

            pg.display.update()

            if self.missile_x_border != 0 and self.missile_on == False:
                time.sleep(1)
                self.computer_turn = True
                self.missile_x_border = 0
                self.run_main_battle_computer_turn()

            self.clock.tick(FPS)

    def update_main_battle(self, rotate_ship, selected_ship, mouse_position, player_grid, game_battle_running, computer_turn, missile_position_y, missile_on):
        if self.selected_cell_main_battle:
            self.missile_on = True
            self.missile_x_border = self.selected_cell_main_battle[0] * CELL_SIZE + TABLE_POSITION_X_MAIN_BATTLE + 1/2 * CELL_SIZE
            self.missile_position_y = self.selected_cell_main_battle[1] * CELL_SIZE + TABLE_POSITION_Y + 1/2 * CELL_SIZE

        if self.missile.rect.center[0] == self.missile_x_border and self.missile_on:
            self.missile_on = False
            self.selected_cell_main_battle = None
        
        self.all_sprites_group.update(self.rotate_ship, self.selected_ship, self.mouse_position, self.player_grid, self.game_battle_running, self.computer_turn, self.missile_position_y, self.missile_on, self.computer_grid, self.computer_ships_sunk)

    def draw_main_battle(self):
        self.main_battle_background_x += 0.5
        self.main_battle_background_x_2 += 0.5

        if self.main_battle_background_x > self.main_battle_background.get_width():
            self.main_battle_background_x = -self.main_battle_background.get_width()
        if self.main_battle_background_x_2 > self.main_battle_background.get_width():
            self.main_battle_background_x_2 = -self.main_battle_background.get_width()

        self.screen.blit(self.main_battle_background, (self.main_battle_background_x, 0))
        self.screen.blit(self.main_battle_background, (self.main_battle_background_x_2, 0))

        self.message_to_screen_main_battle(self.screen)
        self.selected_cell_fill_main_battle(self.screen, self.selected_cell_main_battle)
        self.table_cell_draw_main_battle(self.screen)
        self.loading_buttons_on_main_battle(self.screen, self.mouse_position, self.list_of_button_texts, self.buttons_size_x, self.buttons_size_y)
        self.all_sprites_group.draw(self.screen)

    def selected_cell_fill_main_battle(self, screen, selected_cell_main_battle):
        if self.missile.rect.center[0] == self.missile_x_border and self.selected_cell_main_battle != None and (self.player_entered_grid[self.selected_cell_main_battle[0]][self.selected_cell_main_battle[1]] != 0 and self.player_entered_grid[self.selected_cell_main_battle[0]][self.selected_cell_main_battle[1]] != "miss"):
            self.player_entered_grid[self.selected_cell_main_battle[0]][self.selected_cell_main_battle[1]] = "hit"
            self.player_score += 30
        elif self.missile.rect.center[0] == self.missile_x_border and self.selected_cell_main_battle != None and self.player_entered_grid[self.selected_cell_main_battle[0]][self.selected_cell_main_battle[1]] == 0:
            self.player_entered_grid[self.selected_cell_main_battle[0]][self.selected_cell_main_battle[1]] = "miss"
            self.player_score -= 5

        for row_index, row in enumerate(self.player_entered_grid):
            for column_index, column in enumerate(row):
                if column == "hit":
                    pg.draw.rect(self.screen, RED, (row_index * CELL_SIZE + TABLE_POSITION_X_MAIN_BATTLE, column_index * CELL_SIZE + TABLE_POSITION_Y, CELL_SIZE, CELL_SIZE))
                elif column == "miss":
                    pg.draw.rect(self.screen, GREY, (row_index * CELL_SIZE + TABLE_POSITION_X_MAIN_BATTLE, column_index * CELL_SIZE + TABLE_POSITION_Y, CELL_SIZE, CELL_SIZE))

    def message_to_screen_main_battle(self, screen):
        line_font = pg.font.Font('freesansbold.ttf', 60)
        list_of_messages = ["Your turn!", f"Your score: {len(self.computer_ships_sunk) * 50 - self.player_ships_sunk * 30 + self.player_score}", "Computer's ships", f"sunk: {len(self.computer_ships_sunk)}/5"]
        for index, message in enumerate(list_of_messages):
            line = line_font.render(message, True, YELLOW)
            line_surface = pg.Surface(line.get_size())
            line_surface.fill(BLACK)
            line_surface.blit(line, (0, 0))
            if index == 0:
                self.screen.blit(line_surface, (1090, 5))
            elif index == 1:
                self.screen.blit(line_surface, (1010, 200))
            elif index == 2:
                self.screen.blit(line_surface, (970, 400))
            else:
                self.screen.blit(line_surface, (1100, 470))

    def table_cell_draw_main_battle(self, screen):
        pg.draw.rect(self.screen, BLACK, (TABLE_POSITION_X_MAIN_BATTLE, TABLE_POSITION_Y, TABLE_SIZE, TABLE_SIZE), 5)
        for i in range(1, 11):
            pg.draw.line(self.screen, BLACK, (TABLE_POSITION_X_MAIN_BATTLE + i * CELL_SIZE, TABLE_POSITION_Y), (TABLE_POSITION_X_MAIN_BATTLE + i * CELL_SIZE, TABLE_POSITION_Y + TABLE_SIZE), 5)
            pg.draw.line(self.screen, BLACK, (TABLE_POSITION_X_MAIN_BATTLE, TABLE_POSITION_Y + i * CELL_SIZE), (TABLE_POSITION_X_MAIN_BATTLE + TABLE_SIZE, TABLE_POSITION_Y + i * CELL_SIZE), 5)

    def loading_buttons_on_main_battle(self, screen, mouse_position, list_of_button_texts, buttons_size_x, buttons_size_y):
        self.mouse_position = pg.mouse.get_pos()
        self.list_of_button_texts = ["SOUND", "ON/OFF", "MAIN", "PAGE", "EXIT", "GAME"]
        self.list_of_button_positions_x = [965, 965, 1145, 1145, 1325, 1325]
        self.list_of_button_positions_y = [665, 705, 665, 705, 665, 705]
        self.buttons_size_x = 170
        self.buttons_size_y = 110

        # Button Texts
        for i in range(6):
            if i % 2 == 0 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y: 
                pg.draw.rect(self.screen, RED, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y])
                pg.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y], 5)
            elif i % 2 == 0: 
                pg.draw.rect(self.screen, GREEN, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y])
                pg.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y], 5)

            font = pg.font.Font('freesansbold.ttf', 40)
            text_font = font.render(self.list_of_button_texts[i], True, BLACK)
            text_font_width = text_font.get_width()
            text_font_height = text_font.get_height()
            self.screen.blit(text_font, (self.list_of_button_positions_x[i] + (self.buttons_size_x - text_font_width) // 2, self.list_of_button_positions_y[i] + (self.buttons_size_y - text_font_height) // 4))

        if self.selected_cell_main_battle == None and TABLE_POSITION_X_MAIN_BATTLE < self.mouse_position[0] < TABLE_POSITION_X_MAIN_BATTLE + TABLE_SIZE and TABLE_POSITION_Y < self.mouse_position[1] < TABLE_POSITION_Y + TABLE_SIZE:
            hovered_cell = [(self.mouse_position[0] - TABLE_POSITION_X_MAIN_BATTLE) // CELL_SIZE, (self.mouse_position[1] - TABLE_POSITION_Y) // CELL_SIZE]
            if isinstance(self.player_entered_grid[hovered_cell[0]][hovered_cell[1]], int):
                pg.draw.rect(self.screen, YELLOW, (hovered_cell[0] * CELL_SIZE + TABLE_POSITION_X_MAIN_BATTLE, hovered_cell[1] * CELL_SIZE + TABLE_POSITION_Y, CELL_SIZE, CELL_SIZE))

### GAME MAIN BATTLE COMPUTER TURN SCREEN ###

    def game_ending_lose_check(self):
        self.player_ships_sunk = 0
        for i in range(5):
            if sum(ship_type.count(i + 1) for ship_type in self.computer_entered_grid) == 0:
                self.player_ships_sunk += 1

    def computer_select_cell(self):
        ship_hit_but_not_sunk, next_cell_target = self.checking_ship_hit_but_not_sunk()

        if ship_hit_but_not_sunk:
            if self.computer_entered_grid[next_cell_target[0]][next_cell_target[1]] == 0:
                self.computer_entered_grid[next_cell_target[0]][next_cell_target[1]] = "miss"
            else:
                self.computer_entered_grid[next_cell_target[0]][next_cell_target[1]] = "hit"
                self.player_score -= 10

            self.selected_cell_main_battle_computer_turn = [next_cell_target[1], next_cell_target[0]] 

        elif self.game_ending_lose == False:
            computer_selecting_cell = True
            while computer_selecting_cell:
                computer_select_row = random.randrange(11)
                if computer_select_row % 3 == 0:
                    computer_select_column = random.randrange(3) * 3 + 2 + computer_select_row % 3
                else:
                    computer_select_column = random.randrange(-1, 3) * 3 + 2 + computer_select_row % 3

                if isinstance(self.computer_entered_grid[computer_select_row][computer_select_column], int):
                    if self.computer_entered_grid[computer_select_row][computer_select_column] == 0:
                        self.computer_entered_grid[computer_select_row][computer_select_column] = "miss"
                        computer_selecting_cell = False
                    else:
                        self.computer_entered_grid[computer_select_row][computer_select_column] = "hit"
                        computer_selecting_cell = False
                        self.player_score -= 10

            self.selected_cell_main_battle_computer_turn = [computer_select_column, computer_select_row]


    def checking_ship_hit_but_not_sunk(self):
        for row_index, row in enumerate(self.computer_entered_grid):
            for column_index, column in enumerate(row):
                if column == "hit" and sum(ship_type.count(self.player_grid[row_index][column_index]) for ship_type in self.computer_entered_grid) > 0:
                    if self.player_grid[row_index][column_index] in [1, 2, 3, 5]:
                        row_check_index_right = 1
                        if self.computer_entered_grid[row_check_index_right + row_index][column_index] == "hit":
                            while row_check_index_right + row_index <= 10:
                                if isinstance(self.computer_entered_grid[row_check_index_right + row_index][column_index], int):
                                    return True, [row_check_index_right + row_index, column_index]
                                elif self.computer_entered_grid[row_check_index_right + row_index][column_index] == "miss":
                                    break                                
                                row_check_index_right += 1

                            if row_index - 1 >= 0 and isinstance(self.computer_entered_grid[row_index - 1][column_index], int):
                                return True, [row_index - 1, column_index]

                        column_check_index_up = 1
                        if self.computer_entered_grid[row_index][column_index + column_check_index_up] == "hit":
                            while column_check_index_up + column_index <= 10:
                                if isinstance(self.computer_entered_grid[row_index][column_index + column_check_index_up], int):
                                    return True, [row_index, column_index + column_check_index_up]
                                elif self.computer_entered_grid[row_index][column_index + column_check_index_up] == "miss":
                                    break
                                column_check_index_up += 1

                            if column_index - 1 >= 0 and isinstance(self.computer_entered_grid[row_index][column_index - 1], int):
                                return True, [row_index, column_index - 1]

                    if row_index < 10:
                        if isinstance(self.computer_entered_grid[row_index + 1][column_index], int) and self.computer_entered_grid[row_index][column_index] == "hit":
                            return True, [row_index + 1, column_index]
                    if row_index > 0:
                        if isinstance(self.computer_entered_grid[row_index - 1][column_index], int) and self.computer_entered_grid[row_index][column_index] == "hit":
                            return True, [row_index - 1, column_index]
                    if column_index < 10:
                        if isinstance(self.computer_entered_grid[row_index][column_index + 1], int) and self.computer_entered_grid[row_index][column_index] == "hit":
                            return True, [row_index, column_index + 1]
                    if column_index > 0:
                        if isinstance(self.computer_entered_grid[row_index][column_index - 1], int) and self.computer_entered_grid[row_index][column_index] == "hit":
                            return True, [row_index, column_index - 1]
        return False, None


    def run_main_battle_computer_turn(self):
        self.computer_select_cell()
        while self.computer_turn:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game_battle_running = False
                    self.game_setup_running = False
                    self.game_open = False
                    self.computer_turn = False

                if event.type == pg.MOUSEBUTTONDOWN:
                    for i in range(6):
                        if i == 0 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y:
                            # Sound on/off
                            pass
                        elif i == 2 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y:
                            self.game_battle_running = False
                            self.game_setup_running = False
                            self.computer_turn = False
                        elif i == 4 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y:
                            self.game_battle_running = False
                            self.game_setup_running = False
                            self.game_open = False
                            self.computer_turn = False
            
            self.update_main_battle_computer_turn(self.rotate_ship, self.selected_ship, self.mouse_position, self.player_grid, self.game_battle_running, self.computer_turn, self.missile_position_y, self.missile_on)
            self.draw_main_battle_computer_turn()

            self.game_ending_lose_check()
            if self.player_ships_sunk == 5 and self.missile.rect.center[0] == self.missile_x_border:
                self.game_ending_lose = True
                self.game_lose_screen()

            if self.game_battle_running == False and self.game_setup_running == False and self.computer_turn == False and self.game_open:
                self.reset()

            pg.display.update()

            if self.missile_x_border != 0 and self.missile_on == False:
                time.sleep(1)
                self.computer_turn = False
                self.missile_x_border = 0

            self.clock.tick(FPS)


    def update_main_battle_computer_turn(self, rotate_ship, selected_ship, mouse_position, player_grid, game_battle_running, computer_turn, missile_position_y, missile_on):
        if self.missile.rect.center[0] == self.missile_x_border and self.missile_on:
            self.missile_on = False
            self.selected_cell_main_battle_computer_turn = None

        self.all_sprites_group.update(self.rotate_ship, self.selected_ship, self.mouse_position, self.player_grid, self.game_battle_running, self.computer_turn, self.missile_position_y, self.missile_on, self.computer_grid, self.computer_ships_sunk)
        
        if self.selected_cell_main_battle_computer_turn:
            self.missile_on = True
            self.missile_x_border = self.selected_cell_main_battle_computer_turn[0] * CELL_SIZE + TABLE_POSITION_X_MAIN_BATTLE_COMPUTER_TURN + 1/2 * CELL_SIZE
            self.missile_position_y = self.selected_cell_main_battle_computer_turn[1] * CELL_SIZE + TABLE_POSITION_Y + 1/2 * CELL_SIZE


    def draw_main_battle_computer_turn(self):
        self.main_battle_background_x += 0.5
        self.main_battle_background_x_2 += 0.5

        if self.main_battle_background_x > self.main_battle_background.get_width():
            self.main_battle_background_x = -self.main_battle_background.get_width()
        if self.main_battle_background_x_2 > self.main_battle_background.get_width():
            self.main_battle_background_x_2 = -self.main_battle_background.get_width()
        self.screen.blit(self.main_battle_background, (self.main_battle_background_x, 0))
        self.screen.blit(self.main_battle_background, (self.main_battle_background_x_2, 0))

        self.selected_cell_fill_main_battle_computer_turn(self.screen)
        self.message_to_screen_main_battle_computer_turn(self.screen)
        self.table_cell_draw_main_battle_computer_turn(self.screen)
        self.loading_buttons_on_main_battle_computer_turn(self.screen, self.mouse_position, self.list_of_button_texts, self.buttons_size_x, self.buttons_size_y)
        self.all_sprites_group.draw(self.screen)


    def selected_cell_fill_main_battle_computer_turn(self, screen):
        for row_index, row in enumerate(self.computer_entered_grid):
            for column_index, column in enumerate(row):
                if column == "hit" and ([column_index, row_index] != self.selected_cell_main_battle_computer_turn or (self.missile.rect.center[0] == self.missile_x_border and [column_index, row_index] == self.selected_cell_main_battle_computer_turn)):
                    pg.draw.rect(self.screen, RED, (column_index * CELL_SIZE + TABLE_POSITION_X_MAIN_BATTLE_COMPUTER_TURN, row_index * CELL_SIZE + TABLE_POSITION_Y, CELL_SIZE, CELL_SIZE))
                elif column == "miss" and ([column_index, row_index] != self.selected_cell_main_battle_computer_turn or (self.missile.rect.center[0] == self.missile_x_border and [column_index, row_index] == self.selected_cell_main_battle_computer_turn)):
                    pg.draw.rect(self.screen, GREY, (column_index * CELL_SIZE + TABLE_POSITION_X_MAIN_BATTLE_COMPUTER_TURN, row_index * CELL_SIZE + TABLE_POSITION_Y, CELL_SIZE, CELL_SIZE))
                elif self.missile.rect.center[0] != self.missile_x_border and [column_index, row_index] == self.selected_cell_main_battle_computer_turn:
                    pg.draw.rect(self.screen, YELLOW, (column_index * CELL_SIZE + TABLE_POSITION_X_MAIN_BATTLE_COMPUTER_TURN, row_index * CELL_SIZE + TABLE_POSITION_Y, CELL_SIZE, CELL_SIZE))


    def message_to_screen_main_battle_computer_turn(self, screen):
        line_font = pg.font.Font('freesansbold.ttf', 60)
        list_of_messages = ["Computer's turn!", "Player's ships", f"sunk: {self.player_ships_sunk}/5"]
        for index, message in enumerate(list_of_messages):
            line = line_font.render(message, True, YELLOW)
            line_surface = pg.Surface(line.get_size())
            line_surface.fill(BLACK)
            line_surface.blit(line, (0, 0))
            if index == 0:
                self.screen.blit(line_surface, (15, 5))
            elif index == 1:
                self.screen.blit(line_surface, (60, 310))
            else:
                self.screen.blit(line_surface, (130, 380))


    def table_cell_draw_main_battle_computer_turn(self, screen):
        pg.draw.rect(self.screen, BLACK, (TABLE_POSITION_X_MAIN_BATTLE_COMPUTER_TURN, TABLE_POSITION_Y, TABLE_SIZE, TABLE_SIZE), 5)
        for i in range(1, 11):
            pg.draw.line(self.screen, BLACK, (TABLE_POSITION_X_MAIN_BATTLE_COMPUTER_TURN + i * CELL_SIZE, TABLE_POSITION_Y), (TABLE_POSITION_X_MAIN_BATTLE_COMPUTER_TURN + i * CELL_SIZE, TABLE_POSITION_Y + TABLE_SIZE), 5)
            pg.draw.line(self.screen, BLACK, (TABLE_POSITION_X_MAIN_BATTLE_COMPUTER_TURN, TABLE_POSITION_Y + i * CELL_SIZE), (TABLE_POSITION_X_MAIN_BATTLE_COMPUTER_TURN + TABLE_SIZE, TABLE_POSITION_Y + i * CELL_SIZE), 5)


    def loading_buttons_on_main_battle_computer_turn(self, screen, mouse_position, list_of_button_texts, buttons_size_x, buttons_size_y):
        self.mouse_position = pg.mouse.get_pos()
        self.list_of_button_texts = ["SOUND", "ON/OFF", "MAIN", "PAGE", "EXIT", "GAME"]
        self.list_of_button_positions_x = [5, 5, 185, 185, 365, 365]
        self.list_of_button_positions_y = [665, 705, 665, 705, 665, 705]
        self.buttons_size_x = 170
        self.buttons_size_y = 110

        # Button Texts
        for i in range(6):
            if i % 2 == 0 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y: 
                pg.draw.rect(self.screen, RED, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y])
                pg.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y], 5)
            elif i % 2 == 0: 
                pg.draw.rect(self.screen, GREEN, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y])
                pg.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y], 5)

            font = pg.font.Font('freesansbold.ttf', 40)
            text_font = font.render(self.list_of_button_texts[i], True, BLACK)
            text_font_width = text_font.get_width()
            text_font_height = text_font.get_height()
            self.screen.blit(text_font, (self.list_of_button_positions_x[i] + (self.buttons_size_x - text_font_width) // 2, self.list_of_button_positions_y[i] + (self.buttons_size_y - text_font_height) // 4))

### GAME ENDING SCREENS ###

    def game_lose_screen(self):
        while self.game_ending_lose:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game_battle_running = False
                    self.game_setup_running = False
                    self.game_open = False
                    self.computer_turn = False
                    self.game_ending_lose = False

            self.draw_game_lose(self.screen)

            pg.display.update()
            self.clock.tick(FPS)


    def draw_game_lose(self, screen):
        self.screen.blit(self.game_over_background, (0, 0))
        self.message_to_screen_game_lose(self.screen)
        self.loading_buttons_on_game_lose_screen(self.screen, self.mouse_position, self.list_of_button_texts, self.buttons_size_x, self.buttons_size_y)


    def message_to_screen_game_lose(self, screen):
        pass


    def loading_buttons_on_game_lose_screen(self, screen, mouse_position, list_of_button_texts, buttons_size_x, buttons_size_y):
        pass


    def game_win_screen(self):
        while self.game_ending_win:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game_battle_running = False
                    self.game_setup_running = False
                    self.game_open = False
                    self.game_ending_win = False

            self.draw_game_win(self.screen)

            pg.display.update()
            self.clock.tick(FPS)


    def draw_game_win(self, screen):
        self.screen.blit(self.game_win_background, (0, 0))
        self.message_to_screen_game_win(self.screen)
        self.loading_buttons_on_game_win_screen(self.screen, self.mouse_position, self.list_of_button_texts, self.buttons_size_x, self.buttons_size_y)


    def message_to_screen_game_win(self, screen):
        pass


    def loading_buttons_on_game_win_screen(self, screen, mouse_position, list_of_button_texts, buttons_size_x, buttons_size_y):
        pass


if __name__ == "__main__":
    instance_of_Main = Main()
    instance_of_Main.game_start_screen()