import pygame
import sys
import requests
from bs4 import BeautifulSoup
from sudoku_details import *

class Main:
    def __init__(self):
        pygame.init()
        self.reset()

    def reset(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.first_background = pygame.image.load("first_background.png")
        self.program_opening = True
        self.game_running = False
        self.solver_running = False
        self.game_status = "ON"
        self.is_checking = "OFF"
        self.difficulty = None
        self.font = pygame.font.Font('freesansbold.ttf', 40)
        self.list_of_button_texts = ["EASY", "MEDIUM", "HARD", "EXPERT", "FIND A", "SOLUTION", "SOUND", "ON/OFF", "EXIT", "GAME"]
        self.list_of_button_positions_x = None
        self.list_of_button_positions_y = None
        self.buttons_size_x = None
        self.buttons_size_y_one_line = None
        self.buttons_size_y_two_lines = None
        self.check_button_size_x = None
        self.check_button_size_y = None
        self.given_numbers = [[0 for _ in range(9)] for _ in range(9)]
        self.entered_numbers_for_game_solution = [[0 for _ in range(9)] for _ in range(9)]
        self.entered_numbers_for_game = [[0 for _ in range(9)] for _ in range(9)]
        self.entered_numbers_for_solver = [[0 for _ in range(9)] for _ in range(9)]
        self.current_result = None
        self.mouse_position = None
        self.selected_cell = None
        self.selected_number = None
        self.starting_time = pygame.time.get_ticks()

### Loading the main page related functions only ###

    def main(self):
        while self.program_opening:
            self.screen.blit(self.first_background, (0, 0))
            self.initial_message_to_screen(self.screen)
            self.loading_buttons_on_first_page(self.screen, self.font)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.program_opening = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(10):
                        if i < 4 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y_one_line: 
                            self.difficulty = str(i + 1)
                            self.sudoku_table_getter(self.difficulty, self.given_numbers, self.entered_numbers_for_game_solution)
                            self.game_running = True
                        elif i == 4 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y_one_line:
                            self.solver_running = True
                        elif i == 6 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y_one_line:
                            # Sound on/off
                            pass
                        elif i == 8 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y_one_line:
                            self.program_opening = False
            
            self.game_run()
            self.solve_run()

            pygame.display.update()
        pygame.quit()
        sys.exit()

    def sudoku_table_getter(self, difficulty, given_numbers, entered_numbers_for_game_solution):
        sudoku_file = requests.get("https://nine.websudoku.com/?level={}".format(self.difficulty)).content
        soup = BeautifulSoup(sudoku_file, features = "html.parser")
        identifiers = ["f00", "f01", "f02", "f03", "f04", "f05", "f06", "f07", "f08", 
                       "f10", "f11", "f12", "f13", "f14", "f15", "f16", "f17", "f18",
                       "f20", "f21", "f22", "f23", "f24", "f25", "f26", "f27", "f28",
                       "f30", "f31", "f32", "f33", "f34", "f35", "f36", "f37", "f38",
                       "f40", "f41", "f42", "f43", "f44", "f45", "f46", "f47", "f48",
                       "f50", "f51", "f52", "f53", "f54", "f55", "f56", "f57", "f58",
                       "f60", "f61", "f62", "f63", "f64", "f65", "f66", "f67", "f68",
                       "f70", "f71", "f72", "f73", "f74", "f75", "f76", "f77", "f78",
                       "f80", "f81", "f82", "f83", "f84", "f85", "f86", "f87", "f88"]

        data = [soup.find("input", id = column_identifier) for column_identifier in identifiers]

        for index, value in enumerate(data):
            try:
                self.given_numbers[index // 9][index % 9] = int(value["value"])
                self.entered_numbers_for_game_solution[index // 9][index % 9] = int(value["value"])
            except:
                pass

    def loading_buttons_on_first_page(self, screen, font):
        self.mouse_position = pygame.mouse.get_pos()
        self.list_of_button_positions_x = [50, 315, 585, 850, 50, 50, 450, 450, 850, 850]
        self.list_of_button_positions_y = [400, 400, 400, 400, 600, 650, 600, 650, 600, 650]
        self.buttons_size_x = 250
        self.buttons_size_y_one_line = 100
        self.buttons_size_y_two_lines = 150

        # Button Texts
        for i in range(10):
            if i < 4 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y_one_line: 
                pygame.draw.rect(self.screen, RED, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y_one_line])
                pygame.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y_one_line], 5)
            elif i >= 4 and i % 2 == 0 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y_one_line: 
                pygame.draw.rect(self.screen, RED, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y_two_lines])
                pygame.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y_two_lines], 5)
            elif i < 4: 
                pygame.draw.rect(self.screen, GREEN, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y_one_line])
                pygame.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y_one_line], 5)
            elif i >= 4 and i % 2 == 0:
                pygame.draw.rect(self.screen, GREEN, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y_two_lines])
                pygame.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y_two_lines], 5)

            text_font = self.font.render(self.list_of_button_texts[i], True, BLACK)
            text_font_width = text_font.get_width()
            text_font_height = text_font.get_height()
            screen.blit(text_font, (self.list_of_button_positions_x[i] + (self.buttons_size_x - text_font_width) // 2, self.list_of_button_positions_y[i] + (self.buttons_size_y_one_line - text_font_height) // 2))

    def initial_message_to_screen(self, screen):
        first_status_font = pygame.font.Font('freesansbold.ttf', 60)

        lines = ["Welcome to Sudoku Game & Solver!", "To play a game of sudoku, please click", "on one of the difficulty levels below:"]
        for index, value in enumerate(lines):
            line = first_status_font.render(value, True, (BLACK)) if index == 0 else self.font.render(value, True, (BLACK))
            line_surface = pygame.Surface(line.get_size())
            line_surface.fill((YELLOW))
            line_surface.blit(line, (0, 0))
            screen.blit(line_surface, (50, 50)) if index == 0 else screen.blit(line_surface, (50, 200 + index * 50))

### Running the solver related functions only ###

    def solve_run(self):
        while self.solver_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.solver_running = False
                    self.program_opening = False

                # User clicks
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.selected_cell = [(self.mouse_position[0] - TABLE_POSITION_X) // CELL_SIZE, (self.mouse_position[1] - TABLE_POSITION_Y) // CELL_SIZE]
                    if TABLE_POSITION_X > self.mouse_position[0] or self.mouse_position[0] > TABLE_POSITION_X + TABLE_SIZE or TABLE_POSITION_Y > self.mouse_position[1] or self.mouse_position[1] > TABLE_POSITION_Y + TABLE_SIZE:
                        self.selected_cell = None

                    for i in range(7):
                        if i == 0 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y_one_line: 
                            self.current_result = self.sudoku_solver(self.entered_numbers_for_solver)
                        elif i == 1 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y_one_line: 
                            # Sound on/off
                            pass
                        elif i == 3 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y_one_line: 
                            self.solver_running = False
                        elif i == 5 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y_one_line: 
                            self.solver_running = False
                            self.program_opening = False
            
                # User types a key
                if event.type == pygame.KEYDOWN:
                    if event.unicode.isnumeric():
                        if self.selected_cell != None:
                            self.entered_numbers_for_solver[self.selected_cell[1]][self.selected_cell[0]] = int(event.unicode)
                            self.selected_cell = None

            self.sudoku_check_solver(self.screen, self.entered_numbers_for_solver)
            self.solver_screen_draw(self.screen, self.entered_numbers_for_solver)
            self.loading_buttons_on_solver_page(self.screen, self.font)

            if self.solver_running == False and self.program_opening:
                self.reset()

            pygame.display.update()

    def loading_buttons_on_solver_page(self, screen, font):
        self.mouse_position = pygame.mouse.get_pos()
        self.list_of_button_texts = ["SOLVE!", "SOUND", "ON/OFF", "MAIN", "PAGE", "EXIT", "GAME"]
        self.list_of_button_positions_x = [700, 920, 920, 700, 700, 920, 920]
        self.list_of_button_positions_y = [485, 470, 520, 620, 660, 620, 660]
        self.buttons_size_x = 200
        self.buttons_size_y_one_line = 100
        self.buttons_size_y_two_lines = 130

        # Button Texts
        for i in range(7):
            if i == 0 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y_one_line: 
                pygame.draw.rect(self.screen, RED, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y_one_line])
                pygame.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y_one_line], 5)
            elif i % 2 == 1 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y_one_line: 
                pygame.draw.rect(self.screen, RED, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y_two_lines])
                pygame.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y_two_lines], 5)
            elif i == 0: 
                pygame.draw.rect(self.screen, GREEN, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y_one_line])
                pygame.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y_one_line], 5)
            elif i % 2 == 1:
                pygame.draw.rect(self.screen, GREEN, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y_two_lines])
                pygame.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y_two_lines], 5)

            text_font = self.font.render(self.list_of_button_texts[i], True, BLACK)
            text_font_width = text_font.get_width()
            text_font_height = text_font.get_height()
            screen.blit(text_font, (self.list_of_button_positions_x[i] + (self.buttons_size_x - text_font_width) // 2, self.list_of_button_positions_y[i] + (self.buttons_size_y_one_line - text_font_height) // 2)) 

    def sudoku_check_solver(self, screen, entered_numbers_for_solver):
        row, column = self.find_empty_cell(self.entered_numbers_for_solver)
        if row == None and self.is_sudoku_valid(self.entered_numbers_for_solver):
            self.current_result = True
            self.selected_cell = None
        elif self.is_sudoku_valid(self.entered_numbers_for_solver) == False:
            self.current_result = "Incorrect!"
        else:
            self.current_result = None

    def solver_screen_draw(self, screen, entered_numbers_for_solver):
        self.screen.fill(WHITE)
        self.table_cell_draw(self.screen)
        self.selected_cell_fill(self.screen, self.mouse_position, self.selected_cell)
        self.entered_numbers_for_solver_draw(self.screen, self.entered_numbers_for_solver)

        if self.current_result == True:
            final_message = "Completed!"
        elif self.current_result == False:
            final_message = "Impossible to solve!"
        elif self.current_result == "Incorrect!":
            final_message = "Incorrect!"
        else:
            final_message = "Unsolved!"

        self.message_to_screen(final_message)

    def entered_numbers_for_solver_draw(self, screen, entered_numbers_for_solver):
        for number_y, row in enumerate(self.entered_numbers_for_solver):
            for number_x, number in enumerate(row):
                if number != 0:
                    entered_number_position_x = number_x * CELL_SIZE + TABLE_POSITION_X
                    entered_number_position_y = number_y * CELL_SIZE + TABLE_POSITION_Y

                    self.showing_number_on_screen(self.screen, str(number), entered_number_position_x, entered_number_position_y)

### Running the game related functions only ###

    def game_run(self):
        while self.game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False
                    self.program_opening = False

                # User clicks
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.is_checking = "OFF"
                    self.selected_cell = [(self.mouse_position[0] - TABLE_POSITION_X) // CELL_SIZE, (self.mouse_position[1] - TABLE_POSITION_Y) // CELL_SIZE]
                    if TABLE_POSITION_X > self.mouse_position[0] or self.mouse_position[0] > TABLE_POSITION_X + TABLE_SIZE or TABLE_POSITION_Y > self.mouse_position[1] or self.mouse_position[1] > TABLE_POSITION_Y + TABLE_SIZE:
                        self.selected_cell = None
                    # If the user selected the given cell, then set the mouse position and selected cell back to None
                    elif self.given_numbers[self.selected_cell[1]][self.selected_cell[0]] != 0:
                        self.selected_cell = None

                    for i in range(7):
                        if i == 0 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y_one_line: 
                            self.current_result = self.sudoku_solver(self.given_numbers)
                        elif i == 1 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.check_button_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.check_button_size_y: 
                            self.is_checking = "ON"
                            self.sudoku_solver(self.entered_numbers_for_game_solution)
                        elif i == 2 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y_one_line: 
                            # Sound on/off
                            pass
                        elif i == 4 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y_one_line: 
                            self.game_running = False
                        elif i == 6 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y_one_line: 
                            self.game_running = False
                            self.program_opening = False

                # User types a key
                if event.type == pygame.KEYDOWN:
                    if event.unicode.isnumeric():
                        if self.selected_cell != None:
                            self.entered_numbers_for_game[self.selected_cell[1]][self.selected_cell[0]] = int(event.unicode)
                            self.selected_cell = None

            if self.game_status == "ON":
                self.sudoku_final_check_game(self.screen, self.given_numbers, self.entered_numbers_for_game)
                self.game_screen_draw(self.screen, self.starting_time)
            self.loading_buttons_on_game_page(self.screen, self.font)

            if self.game_running == False and self.program_opening:
                self.reset()

            pygame.display.update()

    def sudoku_final_check_game(self, screen, given_numbers, entered_numbers_for_game):
        total_numbers = []
        for row_given_numbers, row_seleted_numbers in zip(self.given_numbers, self.entered_numbers_for_game):
            row_total_numbers = []
            for column_given_numbers, column_seleted_numbers in zip(row_given_numbers, row_seleted_numbers):
                total_number = column_given_numbers + column_seleted_numbers
                row_total_numbers.append(total_number)
            total_numbers.append(row_total_numbers)

        row, column = self.find_empty_cell(total_numbers)
        if row == None and self.current_result != True:
            self.current_result = "Correct!" if self.is_sudoku_valid(total_numbers) else "Incorrect!"
    
    def game_screen_draw(self, screen, starting_time):
        self.screen.fill(WHITE)
        self.given_numbers_draw(self.screen, self.given_numbers)
        self.table_cell_draw(self.screen)
        self.selected_cell_fill(self.screen, self.mouse_position, self.selected_cell)

        if self.current_result == True:
            final_message = "Game Over!"
            self.game_status = "OFF"
        elif self.current_result == "Correct!":
            self.entered_numbers_for_game_draw(self.screen, self.entered_numbers_for_game)
            final_message = "Excellent!"
            self.game_status = "OFF"
        elif self.current_result == "Incorrect!":
            self.entered_numbers_for_game_draw(self.screen, self.entered_numbers_for_game)
            final_message = "Incorrect!"
        else:
            self.entered_numbers_for_game_draw(self.screen, self.entered_numbers_for_game)
            final_message = "Incomplete!"

        self.message_to_screen(final_message)
        self.time_counter(self.starting_time)

    def given_numbers_draw(self, screen, given_numbers):
        for number_y, row in enumerate(self.given_numbers):
            for number_x, number in enumerate(row):
                if number != 0:
                    number_position_x = number_x * CELL_SIZE + TABLE_POSITION_X
                    given_cell_x = (number_position_x - TABLE_POSITION_X) // CELL_SIZE
                    number_position_y = number_y * CELL_SIZE + TABLE_POSITION_Y
                    given_cell_y = (number_position_y - TABLE_POSITION_Y) // CELL_SIZE

                    pygame.draw.rect(self.screen, GREY, (given_cell_x * CELL_SIZE + TABLE_POSITION_X, given_cell_y * CELL_SIZE + TABLE_POSITION_Y, CELL_SIZE, CELL_SIZE))
                    self.showing_number_on_screen(self.screen, str(number), number_position_x, number_position_y)

    def time_counter(self, starting_time):
        pygame.draw.rect(self.screen, BLUE, (540, 10, 140, 100))
        pygame.draw.rect(self.screen, BLACK, (540, 10, 140, 100), 5)
        time_string = "Time:"
        time_count = pygame.time.get_ticks() - self.starting_time
        time_count_string = "%s:%s" % (str(int(time_count / 60000)), str(int((time_count % 60000) / 1000)))
        time_font = pygame.font.Font('freesansbold.ttf', 35)
        time_text = time_font.render(time_string, True, (BLACK))
        self.screen.blit(time_text, (565, 25))
        time_count_text = time_font.render(time_count_string, True, (BLACK))
        self.screen.blit(time_count_text, (585, 65))

    def loading_buttons_on_game_page(self, screen, font):
        self.mouse_position = pygame.mouse.get_pos()
        self.list_of_button_texts = ["SOLVE!", "CHECK!", "SOUND", "ON/OFF", "MAIN", "PAGE", "EXIT", "GAME"]
        self.list_of_button_positions_x = [700, 20, 920, 920, 700, 700, 920, 920]
        self.list_of_button_positions_y = [485, 10, 470, 520, 620, 660, 620, 660]
        self.check_button_size_x = 180
        self.check_button_size_y = 100
        self.buttons_size_x = 200
        self.buttons_size_y_one_line = 100
        self.buttons_size_y_two_lines = 130

        # Button Texts
        for i in range(8):
            if i == 0 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y_one_line: 
                pygame.draw.rect(self.screen, RED, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y_one_line])
                pygame.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y_one_line], 5)
            elif i == 1 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.check_button_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.check_button_size_y: 
                pygame.draw.rect(self.screen, RED, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.check_button_size_x, self.check_button_size_y])
                pygame.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.check_button_size_x, self.check_button_size_y], 5)
            elif i % 2 == 0 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y_one_line: 
                pygame.draw.rect(self.screen, RED, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y_two_lines])
                pygame.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y_two_lines], 5)
            elif i == 0:
                pygame.draw.rect(self.screen, GREEN, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y_one_line])
                pygame.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y_one_line], 5)
            elif i == 1: 
                pygame.draw.rect(self.screen, GREEN, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.check_button_size_x, self.check_button_size_y])
                pygame.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.check_button_size_x, self.check_button_size_y], 5) 
            elif i % 2 == 0:
                pygame.draw.rect(self.screen, GREEN, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y_two_lines])
                pygame.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y_two_lines], 5)

            text_font = self.font.render(self.list_of_button_texts[i], True, BLACK)
            text_font_width = text_font.get_width()
            text_font_height = text_font.get_height()

            if i == 1:
                screen.blit(text_font, (self.list_of_button_positions_x[i] + (self.check_button_size_x - text_font_width) // 2, self.list_of_button_positions_y[i] + (self.check_button_size_y - text_font_height) // 2))
            else:
                screen.blit(text_font, (self.list_of_button_positions_x[i] + (self.buttons_size_x - text_font_width) // 2, self.list_of_button_positions_y[i] + (self.buttons_size_y_one_line - text_font_height) // 2))

### Helper functions for both of the game and the solver ###

    def selected_cell_fill(self, screen, mouse_position, selected_cell):
        if self.selected_cell != None:
            pygame.draw.rect(self.screen, PINK, (self.selected_cell[0] * CELL_SIZE + TABLE_POSITION_X, self.selected_cell[1] * CELL_SIZE + TABLE_POSITION_Y, CELL_SIZE, CELL_SIZE))

    def table_cell_draw(self, screen):
        pygame.draw.rect(self.screen, BLACK, (TABLE_POSITION_X, TABLE_POSITION_Y, TABLE_SIZE, TABLE_SIZE), 5)
        for i in range(1, 9):
            pygame.draw.line(self.screen, BLACK, (TABLE_POSITION_X + i * CELL_SIZE, TABLE_POSITION_Y), (TABLE_POSITION_X + i * CELL_SIZE, TABLE_POSITION_Y + TABLE_SIZE), 5 if i % 3 == 0 else 1)
            pygame.draw.line(self.screen, BLACK, (TABLE_POSITION_X, TABLE_POSITION_Y + i * CELL_SIZE), (TABLE_POSITION_X + TABLE_SIZE, TABLE_POSITION_Y + i * CELL_SIZE), 5 if i % 3 == 0 else 1)

    def entered_numbers_for_game_draw(self, screen, entered_numbers_for_game):
        for number_y, row in enumerate(self.entered_numbers_for_game):
            for number_x, number in enumerate(row):
                if number != 0:
                    selected_number_position_x = number_x * CELL_SIZE + TABLE_POSITION_X
                    selected_cell_x = (selected_number_position_x - TABLE_POSITION_X) // CELL_SIZE
                    selected_number_position_y = number_y * CELL_SIZE + TABLE_POSITION_Y
                    selected_cell_y = (selected_number_position_y - TABLE_POSITION_Y) // CELL_SIZE

                    if self.is_checking == "ON":
                        pygame.draw.rect(self.screen, GREEN if number == self.entered_numbers_for_game_solution[number_y][number_x] else RED, (selected_cell_x * CELL_SIZE + TABLE_POSITION_X, selected_cell_y * CELL_SIZE + TABLE_POSITION_Y, CELL_SIZE, CELL_SIZE))

                    self.showing_number_on_screen(self.screen, str(number), selected_number_position_x, selected_number_position_y)

    def showing_number_on_screen(self, screen, number, number_position_x, number_position_y):
        number_font = pygame.font.Font('freesansbold.ttf', CELL_SIZE // 2).render(number, False, BLACK)
        number_position_x += (CELL_SIZE - number_font.get_width()) // 2
        number_position_y += (CELL_SIZE - number_font.get_height()) // 2
        self.screen.blit(number_font, (number_position_x, number_position_y))

    def message_to_screen(self, final_message):
        pygame.draw.rect(self.screen, YELLOW, (700, 10, 420, 450))
        pygame.draw.rect(self.screen, BLACK, (700, 10, 420, 450), 5)

        status_font = pygame.font.Font('freesansbold.ttf', 50)
        guide_font = pygame.font.Font('freesansbold.ttf', 30)
        lines = [final_message, "Instructions:", u"\u2022" + "   To enter a number,","click on the cell and", "type in your number.", u"\u2022" + "   Type 0 to delete a", "number in the selected", "cell."]

        for index, value in enumerate(lines):
            if (index == 0 and final_message == "Completed!") or (index == 0 and final_message == "Excellent!"):
                line = status_font.render(value, True, (GREEN))
            elif (index == 0 and final_message == "Impossible to solve!") or (index == 0 and final_message == "Game Over!") or (index == 0 and final_message == "Incorrect!"):
                line = status_font.render(value, True, (RED))
            elif (index == 0 and final_message == "Unsolved!") or (index == 0 and final_message == "Incomplete!"):
                line = status_font.render(value, True, (BROWN))
            elif index == 1:
                line = self.font.render(value, True, (BLACK))
            else:
                line = guide_font.render(value, True, (BLACK))

            if index == 0:
                line_surface = pygame.Surface(line.get_size())
                line_surface.fill((LIGHTGREY))
                line_surface.blit(line, (0, 0))

            if (index == 0 and final_message == "Completed!") or (index == 0 and final_message == "Game Over!") or (index == 0 and final_message == "Incomplete!"):
                self.screen.blit(line_surface, (225, 40))
            elif (index == 0 and final_message == "Impossible to solve!"):
                self.screen.blit(line_surface, (125, 40))
            elif (index == 0 and final_message == "Excellent!") or (index == 0 and final_message == "Unsolved!") or (index == 0 and final_message == "Incorrect!"):
                self.screen.blit(line_surface, (245, 40))
            elif index == 1:
                self.screen.blit(line, (780, 40))
            else:
                self.screen.blit(line, (745, 40 + index * 50))

### Sudoku solver related functions ###

    def sudoku_solver(self, nested_lists_of_numbers):
        if self.is_sudoku_valid(nested_lists_of_numbers) == False:
            return False

        row, column = self.find_empty_cell(nested_lists_of_numbers)
        if row == None:
            return True

        for guess in range(1, 10):
            if self.check_empty_cell(nested_lists_of_numbers, guess, row, column):
                nested_lists_of_numbers[row][column] = guess
                if self.sudoku_solver(nested_lists_of_numbers):
                    return True         
            nested_lists_of_numbers[row][column] = 0
        return False

    def is_sudoku_valid(self, nested_lists_of_numbers):
        numbers_list = []
        for row in nested_lists_of_numbers:
            for number in row:
                if number != 0:
                    numbers_list.append(number)
            if len(numbers_list) != len(set(numbers_list)):
                return False
            else:
                numbers_list = []

        for c in range(9):
            for r in range(9):
                if nested_lists_of_numbers[r][c] != 0:
                    numbers_list.append(nested_lists_of_numbers[r][c])
            if len(numbers_list) != len(set(numbers_list)):
                return False
            else:
                numbers_list = []

        for top_row_of_box in range(0, 9, 3):
            for left_column_of_box in range(0, 9, 3):
                for r in range(top_row_of_box, top_row_of_box + 3):
                    for c in range(left_column_of_box, left_column_of_box + 3):
                        if nested_lists_of_numbers[r][c] != 0:
                            numbers_list.append(nested_lists_of_numbers[r][c])
                if len(numbers_list) != len(set(numbers_list)):
                    return False
                else:
                    numbers_list = []
        return True

    def find_empty_cell(self, nested_lists_of_numbers):
        for row in range(9):
            for column in range(9):
                if nested_lists_of_numbers[row][column] == 0:
                    return row, column
        return None, None

    def check_empty_cell(self, nested_lists_of_numbers, guess, row, column):
        if guess in nested_lists_of_numbers[row]:
            return False

        for i in range(9):
            if guess == nested_lists_of_numbers[i][column]:
                return False

        top_row_of_box = (row // 3) * 3
        left_column_of_box = (column // 3) * 3
        for r in range(top_row_of_box, top_row_of_box + 3):
            for c in range(left_column_of_box, left_column_of_box + 3):
                if nested_lists_of_numbers[r][c] == guess:
                    return False
        return True

if __name__ == '__main__':
    instance_of_Main = Main()
    instance_of_Main.main()