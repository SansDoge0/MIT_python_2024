## Je potreba mit tento soubor otevreny v GUI i s obrazkami, jinak je soubor neuvidi. 
## Nejlepe kdyz se otevre pomoci File -> Open Folder...
import turtle

# Vytvor pozadi
screen = turtle.Screen()
screen.title("Turtle Maze")

# Vytvor zelvu
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()

# Prepinac
picture = 'square'

# 'square'
# 'star'
# 'open_picture'
# 'multi_uhelnik'
# 'maze'
# 'round_maze'

if picture == 'square':    
    screen.bgpic("01/pics/turtle_square.png")  # Nastav obrazek na pozadi
    player.goto(-30, 215)  # Nastav pocatecni souradnice

if picture == 'star':
    screen.bgpic("01/pics/turtle_star.png")  # Nastav obrazek na pozadi
    player.goto(-30, 215)  # Nastav pocatecni souradnice   

if picture == 'open_picture':
    screen.bgpic("01/pics/turtle_openpicture.png")  # Nastav obrazek na pozadi
    player.goto(-30, 215)  # Nastav pocatecni souradnice    

if picture == 'multi_uhelnik':
    screen.bgpic("01/pics/turtle_multi_uhelnik.png")  # Nastav obrazek na pozadi
    player.goto(-30, 215)  # Nastav pocatecni souradnice            

if picture == 'maze':
    screen.bgpic("01/pics/turtle_maze.png")  # Nastav obrazek na pozadi
    player.goto(-30, 215)  # Nastav pocatecni souradnice

if picture == 'round_maze':
    screen.bgpic("01/pics/turtle_round_maze.png")  # Nastav obrazek na pozadi
    player.goto(-30, 215)  # Nastav pocatecni souradnice    


# TODO: SEM PRIDEJ SVUJ KOD 
    
''' Pro pohyb pouzij funkce ''' 
#  player.forward(int) 
#  player.backward(int)

#player.forward(50) 

'''  Pro otaceni pouzij funkce: ''' 
#  player.left(int)
#  player.right(int)

''' Pokud zrovna nechces kreslit, napis toto:'''
#  player.penup()
#  pak kresleni znovu vratis takto:
#  player.pendown()

''' Pokud chces zmenit barvu, napis toho:'''
#  player.color('nazev barvy v anglictine')

''' Vlastni promennou definujes takto:'''
#  tvoje_promenna = hodnota

''' Pokud chces vyuzit cykly(loopy), napis je takto: ''' 
#  for i in range(pocet_opakovani):
#       tvuj kod

''' Pokud chces vyuzit podminky(conditions), napis je takto: ''' 
#  if tvoje_podminka:
#       tvuj kod
#  elif tvoje_druha_podminka:
#       tvuj kod
#  else:
#       tvuj kod

''' Pokud chces napsat vlastni funkci, napis ji takto:'''
#  def jmeno_tve_funkce(parametry):
#       tvuj kod 

# Nechej screen zapnuty
screen.mainloop()