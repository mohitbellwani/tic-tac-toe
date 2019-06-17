import pygame


pygame.init()
clock = pygame.time.Clock()


player_one_colour = (255, 255, 255)
player_two_colour = (0, 0, 0)
background_colour = (63, 102, 255)
lines_colour = (216, 211, 192)
highlight_colour = (169, 165, 135)

font = pygame.font.Font('game_font.ttf', 15)
symbol_font = pygame.font.Font('game_font.ttf', 30)

display_width = 800
display_height = 600

game_fps = 30


game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tic Tac Toe')


field_locations = {'1': {'x': 175, 'y': 50}, '2': {'x': 345, 'y': 50}, '3': {'x': 515, 'y': 50},
                   '4': {'x': 175, 'y': 195}, '5': {'x': 345, 'y': 195}, '6': {'x': 515, 'y': 195},
                   '7': {'x': 175, 'y': 340}, '8': {'x': 345, 'y': 340}, '9': {'x': 515, 'y': 340}}

current_player_name = 'ONE'
field_dict = {'1':None, '2':None, '3':None, '4':None, '5':None, '6':None, '7':None, '8':None, '9':None}

def reset_game_variables():
    global current_player_name
    global field_dict

    current_player_name = 'ONE'
    field_dict = {'1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None}



def symbol_to_field(text, color, button_x, button_y, button_width, button_height):
    text_surface = symbol_font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (button_x+(button_width/2), button_y+(button_height/2))
    game_display.blit(text_surface, text_rect)

def win_conditions():
    global field_dict

    if (field_dict['1'] == field_dict['2'] == field_dict['3'] != None or
        field_dict['4'] == field_dict['5'] == field_dict['6'] != None or
        field_dict['7'] == field_dict['8'] == field_dict['9'] != None or
        field_dict['1'] == field_dict['4'] == field_dict['7'] != None or
        field_dict['2'] == field_dict['5'] == field_dict['8'] != None or
        field_dict['3'] == field_dict['6'] == field_dict['9'] != None or
        field_dict['1'] == field_dict['5'] == field_dict['9'] != None or
        field_dict['3'] == field_dict['5'] == field_dict['7'] != None):
        game_over_screen(current_player_name)
    elif None not in field_dict.values():
        game_over_screen('')

def field(text, color, highlight, text_color, x, y, width, height, key):
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global current_player_name
    global field_dict

    if text == '':
        if x+width > cursor[0] > x and y+height > cursor[1] > y:
            if click[0] == 1:
                if current_player_name == 'ONE':
                    field_dict[key] = 'X'
                    win_conditions()
                    current_player_name = 'TWO'
                else:
                    field_dict[key] = 'O'
                    win_conditions()
                    current_player_name = 'ONE'

            pygame.draw.rect(game_display, highlight, (x, y, width, height))
    else:
        pygame.draw.rect(game_display, color, (x, y, width, height))

    symbol_to_field(text, text_color, x, y, width, height)

def draw_fields(field_dict):
    for key, value in field_dict.items():
        if value == None:
            field('', background_colour, highlight_colour, lines_colour, field_locations[key]['x'], field_locations[key]['y'], 110, 110, key)
        elif value == 'X':
            field('X', background_colour, highlight_colour, player_one_colour, field_locations[key]['x'], field_locations[key]['y'], 110, 110, key)
        else:
            field('O', background_colour, highlight_colour, player_two_colour, field_locations[key]['x'], field_locations[key]['y'], 110, 110, key)


def message_to_screen(msg, color, y_displace=0):
    text_surface = font.render(msg, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (display_width/2), (display_height/2)+y_displace
    game_display.blit(text_surface, text_rect)

def game_over_screen(winner):
    game_over = True

    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    reset_game_variables()
                    game_loop()

        game_display.fill(background_colour)

        message_to_screen('GAME OVER!', lines_colour, -50)
        if winner == '':
            message_to_screen('A DRAW!', lines_colour, 0)
        else:
            message_to_screen('PLAYER {} WINS!'.format(winner), lines_colour, 0)
        message_to_screen('PRESS ENTER TO PLAY AGAIN', lines_colour, 50)

        pygame.display.update()
        clock.tick(game_fps)

def draw_game_board():
    pygame.draw.line(game_display, lines_colour, (150,175), (650, 175), 5)
    pygame.draw.line(game_display, lines_colour, (150, 325), (650, 325), 5)
    pygame.draw.line(game_display, lines_colour, (300, 50), (300, 450), 5)
    pygame.draw.line(game_display, lines_colour, (500, 50), (500, 450), 5)

def game_loop():
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

        game_display.fill(background_colour)
        draw_game_board()
        draw_fields(field_dict)

        if current_player_name == 'ONE':
            message_to_screen('PLAYER {} TURN'.format(current_player_name), player_one_colour, 220)
        else:
            message_to_screen('PLAYER {} TURN'.format(current_player_name), player_two_colour, 220)

        pygame.display.update()
        clock.tick(game_fps)

    pygame.quit()
    quit()

game_loop()
