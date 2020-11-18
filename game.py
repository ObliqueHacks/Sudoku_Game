
def NewGame(alpha):
  for x in range(9):
    for y in range(9):
      alpha[x][y] = 0
  return True


def constraints(alpha, pos_x, pos_y):
  for i in range (1, 9, 1):
    if (pos_x+i < 9):
      if (alpha[pos_x+i][pos_y] == alpha[pos_x][pos_y]):
        return False

    if (pos_x-i > -1):
      if (alpha[pos_x-i][pos_y] == alpha[pos_x][pos_y]):
        return False 

    if (pos_y-i > -1):
      if (alpha[pos_x][pos_y-i] == alpha[pos_x][pos_y]):
        return False

    if (pos_y+i < 9):
      if (alpha[pos_x][pos_y+i] == alpha[pos_x][pos_y]):
        return False 

  if (pos_x < 3):
    if (pos_y  < 3):
      for x in range (3):
        for y in range (3):
          if (pos_x == x and pos_y == y):
            continue
          elif (alpha[x][y] == alpha[pos_x][pos_y]):
            return False

    if (pos_y > 2 and pos_y < 6):
      for x in range (3):
        for y in range (3,6,1):
          if (pos_x == x and pos_y == y):
            continue
          elif (alpha[x][y] == alpha[pos_x][pos_y]):
            return False
    
    if (pos_y > 5 and pos_y < 9):
      for x in range (3):
        for y in range (6,9,1):
          if (pos_x == x and pos_y == y):
            continue
          elif (alpha[x][y] == alpha[pos_x][pos_y]):
            return False

  if (pos_x > 3 and pos_x < 6):
    if (pos_y  < 3):
      for x in range (3,6,1):
        for y in range (3):
          if (pos_x == x and pos_y == y):
            continue
          elif (alpha[x][y] == alpha[pos_x][pos_y]):
            return False

    if (pos_y > 2 and pos_y < 6):
      for x in range (3,6,1):
        for y in range (3,6,1):
          if (pos_x == x and pos_y == y):
            continue
          elif (alpha[x][y] == alpha[pos_x][pos_y]):
            return False
    
    if (pos_y > 5 and pos_y < 9):
      for x in range (3,6,1):
        for y in range (6,9,1):
          if (pos_x == x and pos_y == y):
            continue
          elif (alpha[x][y] == alpha[pos_x][pos_y]):
            return False


  if (pos_x > 5 and pos_x < 9):
    if (pos_y  < 3):
      for x in range (6,9,1):
        for y in range (3):
          if (pos_x == x and pos_y == y):
            continue
          elif (alpha[x][y] == alpha[pos_x][pos_y]):
            return False

    if (pos_y > 2 and pos_y < 6):
      for x in range (6,9,1):
        for y in range (3,6,1):
          if (pos_x == x and pos_y == y):
            continue
          elif (alpha[x][y] == alpha[pos_x][pos_y]):
            return False
    
    if (pos_y > 5 and pos_y < 9):
      for x in range (6,9,1):
        for y in range (6,9,1):
          if (pos_x == x and pos_y == y):
            continue
          elif (alpha[x][y] == alpha[pos_x][pos_y]):
            return False
  return True 

def solve (alpha, pos_x, pos_y):

  global var
  var = 0

  if (var == 1):
    return 0
  
  if (alpha[pos_x][pos_y] == 0):
    for x in range (1, 10, 1):

      alpha[pos_x][pos_y] = x

      if (constraints(alpha, pos_x, pos_y) == False):
        alpha[pos_x][pos_y] = 0
        continue 

      elif (pos_y + 1 < 9):
        solve(alpha, pos_x, pos_y + 1)


      elif (pos_x + 1 < 9):
        solve(alpha, pos_x + 1, 0)
      
      elif (pos_x == 8  and pos_y == 8):
        var = 1

      if (var == 1):
        return 0

  
  elif (alpha[pos_x][pos_y] != 0):
    if (pos_y + 1 < 9):
      solve(alpha, pos_x, pos_y + 1)
    elif (pos_x + 1 < 9):
      solve(alpha, pos_x+1, 0)

  return 0


import pygame
pygame.init()

#creates the screen 
screen = pygame.display.set_mode((500,500))

#title and icon
pygame.display.set_caption("Sudoku")


alpha = [
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0]
        ]

def int_finder(alpha, pos_x, pos_y):
  font = pygame.font.Font('freesansbold.ttf', 35)
  display = font.render(str(alpha[pos_x][pos_y]), True, (31,28,28))
  return screen.blit(display, (60+(x*44), 34+(i*44)))

#controls tab
font = pygame.font.Font('freesansbold.ttf', 20)
controls = font.render("Press 's' to Solve", True, (31,28,28))
controls2 = font.render("Press 'n' for New Game", True, (31,28,28))


#positions
pos_x = 0
pos_y = 0

#runs program through loop
runner = True
while runner:
  screen.fill((102, 138, 149))
  screen.blit(controls, (45,450))
  screen.blit(controls2, (250, 450))

  color = (148, 95, 224)
  x_value = (52+(44*pos_y))
  y_value = (27+(44*pos_x))
  pygame.draw.rect(screen, color, pygame.Rect(x_value, y_value, 43, 43))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      runner = False

    if (event.type == pygame.KEYDOWN):

      if (event.key == pygame.K_RIGHT):
        if (pos_y < 8):
          pos_y+=1
          print(pos_y)
        
      elif (event.key == pygame.K_LEFT):
        if pos_y > 0:
          pos_y-=1
          print(pos_y)
    
      elif (event.key == pygame.K_UP):
        if pos_x > 0:
          pos_x-=1
          print(pos_x)
    
      elif (event.key == pygame.K_DOWN):
        if pos_x < 8:
          pos_x+=1
          print(pos_x)

      elif (event.key == pygame.K_s):
        solve(alpha, 0,0)
        print("Yessir Input is Correct")

      elif (event.key == pygame.K_1):
        alpha[pos_x][pos_y] = 1

      elif (event.key == pygame.K_2):
        alpha[pos_x][pos_y] = 2

      elif (event.key == pygame.K_3):
        alpha[pos_x][pos_y] = 3

      elif (event.key == pygame.K_4):
        alpha[pos_x][pos_y] = 4

      elif (event.key == pygame.K_5):
        alpha[pos_x][pos_y] = 5
      
      elif (event.key == pygame.K_6):
        alpha[pos_x][pos_y] = 6

      elif (event.key == pygame.K_7):
        alpha[pos_x][pos_y] = 7

      elif (event.key == pygame.K_8):
        alpha[pos_x][pos_y] = 8
      
      elif (event.key == pygame.K_9):
        alpha[pos_x][pos_y] = 9

      elif (event.key == pygame.K_n):
        NewGame(alpha) 

  for i in range (9):
    for x in range (9):
      int_finder(alpha, i, x)

  pygame.display.update()