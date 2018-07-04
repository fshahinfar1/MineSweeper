from random import randrange

Empty=0
Bomb=1
DefuseFlag = 'f'
Hide = 'x'


class GameBoard:
    def __init__(self, world_size, mine_count):
        self.world_size = world_size
        self.mine_count = mine_count
        self.grid = [[Empty]*world_size for i in range(world_size)]
        self.is_game_over_flag = False
        self.grid_view = [[Hide]*world_size for i in range(world_size)]
        self.cell_values = [[0]*world_size for i in range(world_size)]
        self.unexplored_cells = world_size*world_size
        self.left_mines = mine_count
        self.defuse_flags = mine_count
        rows = [0]*mine_count
        cols = [0]*mine_count
        for i in range(mine_count):
            rows[i] = randrange(world_size)
            cols[i] = randrange(world_size)
        for row,col in zip(rows, cols):
            self.grid[row][col] = Bomb
        for i in range(world_size):
            for j in range(world_size):
                value=0
                for r in (-1, 0, 1):
                    if (i+r < 0) or (i+r>=world_size):
                        continue
                    for c in (-1, 0, 1):
                        if (j+c < 0) or (j+c>=world_size):
                            continue
                        if self.grid[i+r][j+c] == Bomb:
                            value += 1
                self.cell_values[i][j] = value

    def is_game_over(self):
        return self.is_game_over_flag

    def explore(self, row, col):
        if self.is_out_of_board(row, col):
            return
        if self.grid[row][col] == Bomb:
            self.grid_view[row][col] = 'b'
            self.explode()
        elif self.grid_view[row][col] == Hide:
            self.grid_view[row][col] = str(self.cell_values[row][col])
            self.unexplored_cells -= 1
            if self.unexplored_cells <= 0:
                self.is_game_over_flag = True

    def defuse(self, row, col):
        if self.is_out_of_board(row, col):
            return
        if self.grid_view[row][col] != DefuseFlag:
            if self.defuse_flags > 0 :
                self.grid_view[row][col] = DefuseFlag
                self.defuse_flags -= 1
                if self.grid[row][col] == Bomb:
                    self.left_mines -= 1
                    if self.left_mines <= 0:
                        self.is_game_over_flag = True
        else:
            self.grid_view[row][col] = Hide
            self.defuse_flags += 1
            if self.grid[row][col] == Bomb:
                self.left_mines += 1

    def explode(self):
        self.is_game_over_flag = True
        print("You have lost it was a bomb")

    def show(self):
        for i in range(self.world_size):
            for j in range(self.world_size):
                if j == 0:
                    print(i, end=' ')
                print(self.grid_view[i][j], end=' ')
            print()
        print('  ', end='')
        for i in range(self.world_size):
            print(i, end=' ')
        print()

    def is_out_of_board(self, row, col):
        if row > self.world_size or row < 0:
            return True
        if col > self.world_size or col < 0:
            return True
        return False
