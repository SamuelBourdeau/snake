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
white=(255,255,255)
black=(0,0,0)
green=(0,255,0)
pomme=[randint(0,15),randint(0,15)]
running = True
while running:

    clock.tick(5)

    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
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
    width = 15 
    height = 15
    
    for i in range(20):
        for j in range(20):
            x=i*15
            y=j*15
            if abs(x-y) % 30==0:
                rect = pg.Rect(x, y, width, height)
                pg.draw.rect(screen, white, rect)
            else : 
                rect = pg.Rect(x, y, width, height)
                pg.draw.rect(screen, black, rect)
    
    #création d'une pomme
    if snake[0]==pomme:
        pomme=[randint(0,15),randint(0,15)]
    else :
        snake.pop()                 #permet de ne pas enlever le dernier bloc du serpent si on mange une pomme
    pg.draw.rect(screen, green, pg.Rect(pomme[0]*15,pomme[1]*15, 15, 15))

    #serpent qui bouge
        
    first_x, first_y=snake[0]
    newcell_x, newcell_y=first_x + direction[0], first_y + direction[1]
    snake.insert(0, [newcell_x, newcell_y])
    for i in range (len(snake)):
        pg.draw.rect(screen, red, pg.Rect(15*snake[i][0], 15*snake[i][1], 15, 15))
    

    

    pg.display.update()

# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()