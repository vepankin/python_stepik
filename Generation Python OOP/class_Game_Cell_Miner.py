from random import sample
from dataclasses import dataclass
from itertools import chain

@dataclass
class Cell:
    row:  int
    col:  int
    mine: bool = False
    neighbours: int = 0
    open: bool = False
    flag: bool = False
    
    def __hash__(self):
        return hash((self.row, self.col))
    
class Game:
        
    def __set_mines(self):
        mine_cells = sample(list(chain.from_iterable(self.board)), k=self.mines)

        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.board[row][col]
                if cell in mine_cells:
                    cell.mine = True
                for r,c in ((row+x, col+y) for x in range(-1,2) for y in range(-1,2)):
                    if 0<=r<self.rows and 0<=c<self.cols:
                        if self.board[r][c] in mine_cells:
                            cell.neighbours += 1
    
    def __init__(self, rows: int, cols: int, mines: int):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[Cell(row, col) for col in range(cols)] for row in range(rows)]
        self.__set_mines()
        self.over = False
        self.won = False
        self.safe_moves = rows*cols-mines
        
    def show(self, show_all=False):
        print('   ', end='') 
        for c in range(self.cols):
            print(str.center(f'{c+1}',3), end='')
        print()        
        
        for row in range(self.rows):
            print(str.center(f'{row+1}',3), end='')
            
            for col in range(self.cols):
                cell = self.board[row][col]
                if cell.open or show_all:
                    ch = '[x]' if cell.mine else f'[{cell.neighbours}]'
                else:
                    ch = '[P]' if cell.flag else '[ ]'
                print(ch, end='')
            print()    

    def move(self, row, col, flag=False):
        
        if row<0 or row>=self.rows:
            print('Ряд указан неверно!')
            return
        if col<0 or col>=self.cols:
            print('Колонка указана неверно!')
            return
            
        if self.over:
            print('Game over!')
        else:    
            cell = self.board[row][col]
            
            if flag:
                cell.flag = True
            else:
                cell.open = True
                if cell.mine:
                    self.over = True
                else:
                    self.safe_moves -= 1
                    if self.safe_moves == 0:
                        self.won = True
'''
game = Game(14, 18, 40)    # 14 строк, 18 столбцов и 40 мин

print(game.rows)           # 14
print(game.cols)           # 18
print(game.mines)          # 40

cell = game.board[0][0]

print(cell.row)            # 0; строка ячейки
print(cell.col)            # 0; столбец ячейки
print(cell.mine)           # True или False в зависимости от того, содержит ячейка мину или нет
print(cell.neighbours)     # число от 0 до 8, количество мин в соседних ячейках

game.show(True)
print()
'''

game = Game(5, 5, 5) 
#game.show(True)
print()

while not game.over and not game.won:
    game.show()
    
    try:
        r,c,*flag = input('Введите row col [P]: ').split()
        game.move(int(r)-1, int(c)-1, bool(flag))
    except:
        print('Координаты указаны неверно!')
    
    if game.over:
        game.show(True)
        print('Game over!')
        
    if game.won:
        game.show()
        print('You won!')        