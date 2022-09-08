gameboard = [[" "] * 3 for i in range(3)]
player=None

def win_or_loose():
    win_combination = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                       ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                       ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    
    for a, b, c in win_combination:
        if gameboard[a[0]][a[1]] == gameboard[b[0]][b[1]] == gameboard[c[0]][c[1]] != ' ':
            print(f'Выиграл {gameboard[a[0]][a[1]]}!')
            return True
    return False

def gameboard_print (gameboard):
  print ('   0-1-2')
  for row in range (len(gameboard)):
    print (str(row)+']', *gameboard[row])
    
    
def select_player (gameboard,player):
  while True:
    gameboard_print(gameboard)
    print(f'Ход игрока [{player}]!')
    choise = input (f'Выберите клетку [путем ввода двух координат [0..2 0..2]: ').split()
    print("\033[H\033[J") #очистить консоль для новой отрисовки игровой доски
    if len(choise) != 2:
      print ('Введите 2 координаты[0..2 0..2]: ')
      continue
    if not choise[0].isdigit() or not choise[1].isdigit():
      print('Неверный выбор. Нужны числа. ')
      continue
    x, y = map(int, choise)
    if x not in [0,1, 2] or y not in [0, 1, 2]:
      print('Таких координат не существует! Введите координаты от 0 до 2: ')
      continue
    if gameboard[x][y] != ' ':
      print('Эта клетка уже занята')
      continue
    return x,y

def game (gameboard,player):
  count=0
  while True:
    count += 1
    win_or_loose();
    if count % 2 == 0:
      player = 'x'
    else:
      player = 'o'
    x, y = select_player(gameboard, player)
    if count == 9:
      print('Ничья! Достигнуто максимальное количество ходов!')
      break
    gameboard[x][y] = player
    
game (gameboard,player)