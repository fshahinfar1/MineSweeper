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
            break
        except:
            print('wrong input type')
    return GameBoard(world_size, mine_count)


def take_cell():
    row=0
    col=0
    print('Enter your move:')
    while(True):
        try:
            row = int(input('row: '))
            break
        except:
            print('wrong input type')
    while(True):
        try:
            col = int(input('col: '))
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


def run():
    gameboard = initialize()
    while not gameboard.is_game_over():
        gameboard.show()
        command = take_command()
        if command == Exit:
            break
        row, col = take_cell()
        if command == Explore:
            pass
        elif command == Defuse:
            pass


if __name__ == '__main__':
    run()
