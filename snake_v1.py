"""
v1 : pareil mais au moins on peut sortir du programme
avec la touche 'q', ou avec la souris en fermant la fenêtre
"""

from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((300, 300))
clock = pg.time.Clock()
snake = [[10, 15],[11, 15],[12, 15]]    # les coordonnées du corps du serpent
red=(255,0,0)
direction = [1, 0]
WHITE=(255,255,255)
black=(0,0,0)
GREEN=(0,255,0)
pomme=[randint(0,15),randint(0,15)]
width = 15 
height = 15
SIZE = 15
running = True

#définition de fonctions
def damier():
    for i in range(20):
        for j in range(20):
            x=i*SIZE
            y=j*SIZE
            if abs(x-y) % 30==0:
                rect = pg.Rect(x, y, width, height)
                pg.draw.rect(screen, WHITE, rect)
            else : 
                rect = pg.Rect(x, y, width, height)
                pg.draw.rect(screen, black, rect)

def serpent(snake, direction):
    first_x, first_y=snake[0]
    newcell_x, newcell_y=first_x + direction[0], first_y + direction[1]
    if [newcell_x,newcell_y] in snake:
        running = False
    snake.insert(0, [newcell_x%20, newcell_y%20])

    for i in range (len(snake)):
        pg.draw.rect(screen, red, pg.Rect(15*snake[i][0], 15*snake[i][1], 15, 15))

while running:

    clock.tick(5)

    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:      #on prend les directions 
            if event.key == pg.K_q and direction != [1,0]:  #il ne faut pas pouvoir revenir sur sois-même
                direction = [-1,0]
            elif event.key == pg.K_d and direction != [-1,0]:
                direction = [1,0]
            elif event.key == pg.K_z and direction != [0,1]:
                direction = [0,-1]
            elif event.key == pg.K_s and direction != [0,-1]:
                direction = [0,1]
   
    #création du damier
    
    damier()
    
    
    
    #serpent qui bouge
    serpent(snake, direction)
    
    #création d'une pomme
    if snake[0]==pomme:
        pomme=[randint(0,15),randint(0,15)]
    else :
        snake.pop()                 #permet de ne pas enlever le dernier bloc du serpent si on mange une pomme
    pg.draw.rect(screen, GREEN, pg.Rect(pomme[0]*15,pomme[1]*15, 15, 15))

    #fin de jeu
    #for i in range (len(snake)):
    #       if snake[i][0]==snake[j][0] and snake[i][1]==snake[j][1]:
    #           running = False
    
    pg.display.update()

# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()