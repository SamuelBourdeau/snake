"""
v1 : pareil mais au moins on peut sortir du programme
avec la touche 'q', ou avec la souris en fermant la fenêtre
"""

from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((300, 300))
clock = pg.time.Clock()

# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True
while running:

    clock.tick(1)

    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False

    # xxx ici c'est discutable, car si on tape 'q'
    # on va quand même changer de couleur avant de sortir...
   
    #création du damier
    width = 15 
    height = 15
    color=(255,255,255)
    for i in range(20):
        for j in range(20):
            x=i*15
            y=j*15
            if abs(x-y) % 30==0:
                rect = pg.Rect(x, y, width, height)
                pg.draw.rect(screen, color, rect)
   
    #création d'un serpent fixe 
    snake = [[10, 15],[11, 15],[12, 15]]    # les coordonnées du corps du serpent
    red=(255,0,0)
    pg.draw.rect(screen, red, pg.Rect(15*snake[0][0], 15*snake[0][1], 15, 15))
    pg.draw.rect(screen, red, pg.Rect(15*snake[1][0], 15*snake[1][1], 15, 15))
    pg.draw.rect(screen, red, pg.Rect(15*snake[2][0], 15*snake[2][1], 15, 15))
    
    
    pg.display.update()


# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()