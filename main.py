import os
from gameboard import GameBoard


Defuse = 0
Explore = 1
Exit = 2
command_dict = {'e': Explore, 'd': Defuse, 'q': Exit}


def initialize():
    world_size = 0
    mine_count = 0
    while(True):
        try:
            world_size = int(input('size: '))
            break
        except:
            print('wrong input type')
    while(True):
        try:
            mine_count = int(input('mines: '))
            if mine_count <= world_size * world_size:
                break
            print(f'mines should be less than number of cells ({world_size*world_size})')
        except:
            print('wrong input type')
    return GameBoard(world_size, mine_count)


def take_cell(max_row, max_col):
    row=0
    col=0
    print('Enter your move:')
    while(True):
        try:
            row = int(input('row: '))
            if row < max_row:
                break
            print(f'row should be less than {max_row}. counting from zero.')
        except:
            print('wrong input type')
    while(True):
        try:
            col = int(input('col: '))
            if col < max_col:
                break
            print(f'column should be less than {max_col}. counting from zero.')
        except:
            print('wrong input type')
    return row, col


def take_command():
    command=0
    while(True):
        try:
            command = input('Defuse(d)/Explore(e): ')
            if command in ('e', 'd', 'q'):
                command = command_dict[command]
                break
            print('please enter `e` or `d`')
        except:
            print('wrong input type')
    return command


def clear_console():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def run():
    gameboard = initialize()
    size = gameboard.world_size
    while not gameboard.is_game_over():
        clear_console()
        gameboard.show()
        command = take_command()
        if command == Exit:
            break
        row, col = take_cell(size, size)
        if command == Explore:
            gameboard.explore(row, col)
        elif command == Defuse:
            gameboard.defuse(row, col)
    clear_console()
    gameboard.show()


if __name__ == '__main__':
    run()
