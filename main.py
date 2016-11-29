#teamwork with Erica Jurado

from graphics import *
from enemy import *
from player import *
from chaser import *
from wave import *
from projectile import *
from healthbar import *
import time
import random
import math

window = GraphWin("Final", 1000, 600)
image = Image(Point(500, 300), "tiger.gif")
image.draw(window)

keys = {"w": False, "a": False, "s": False, "d": False, "q": False}


def keypress_callback(event):
    if event.char in "wasdq":
        keys[event.char] = True

def keyrelease_callback(event):
    if event.char in "wasdq":
        keys[event.char] = False

def keyboard_callback(event):
    if " " == event.char:
        projectile = Projectile(window, player.circle.getCenter().getX()+20, player.circle.getCenter().getY())
        projectiles.append(projectile)

window.bind_all("<Key>", keypress_callback)
window.bind_all("<KeyRelease>", keyrelease_callback)
window.bind_all("<KeyRelease-space>", keyboard_callback)

start_time = time.time()
last_time = start_time
quit = False
frames = 0
enemies = []
enemy_spawn_rate = 2
enemy_spawn_timer = 2
player = Player(window, 30, window.getHeight()/2)
chasers = []
chaser_spawn_rate = 3
chaser_spawn_timer = 3
waves = []
wave_spawn_rate = 2
wave_spawn_timer = 2
projectiles = []
projectile_spawn_rate = 2
projectile_spawn_timer = 2


score_counter = 0
collision_counter = 0

healthBar = Text(Point(80, 100), "Health Bar: ")
healthBar.setTextColor(color_rgb(255, 255, 255))
healthBar.setStyle("bold")
healthBar.draw(window)
recs = []
rec1 = Healthbar(window, 130, 100, 170, 120)
rec2 = Healthbar(window, 170, 100, 210, 120)
rec3 = Healthbar(window, 210, 100, 250, 120)
recs.append(rec1)
recs.append(rec2)
recs.append(rec3)

score_info = Text(Point(80, 80), "Score: ")
score_info.setTextColor(color_rgb(255, 255, 255))
score_info.draw(window)
score = Text(Point(140, 80), str(score_counter))
score.setTextColor(color_rgb(255, 255, 255))
score.draw(window)

while not quit:

    current_time = time.time()
    delta_time = current_time - last_time

    # Update the player based on input
    player.update(keys, delta_time)

    enemy_spawn_timer -= delta_time
    chaser_spawn_timer -= delta_time
    wave_spawn_timer -= delta_time
    projectile_spawn_timer -= delta_time
    # Make a new enemy at a random y location if enemy_spawn_rate seconds has passed
    if enemy_spawn_timer < 0:
        enemy = Enemy(window, window.getWidth(), random.randint(0, window.getHeight()))
        enemies.append(enemy)
        # Reset the enemy spawn timer
        enemy_spawn_timer = enemy_spawn_rate
    for enemy in enemies:
        enemy.update(delta_time)
        # Remove the enemy from the screen and the list of enemies if it gets to the screen's far left
        if enemy.circle.getCenter().getX() < 0:
            enemy.circle.undraw()
            enemies.remove(enemies.index(enemy))

    # Collision detection
    for enemy in enemies:
        if player.circle_collision(enemy.circle):
            enemy.circle.undraw()
            enemies.remove(enemy)
            collision_counter += 1


    if chaser_spawn_timer < 0:
        chaser = Chaser(window, window.getWidth(), random.randint(0, window.getHeight()))
        chasers.append(chaser)
        # Reset the enemy spawn timer
        chaser_spawn_timer = chaser_spawn_rate


    for chaser in chasers:
        chaser.set_to_chase(player)
        chaser.chase(delta_time)
        # Remove the enemy from the screen and the list of enemies if it gets to the screen's far left
        if chaser.circle.getCenter().getX() < 0:
            chaser.circle.undraw()
            chasers.remove(chasers.index(chaser))


    # Collision detection
    for chaser in chasers:
        if player.circle_collision(chaser.circle):
            chaser.circle.undraw()
            chasers.remove(chasers.index(chaser))
            collision_counter += 1

    if wave_spawn_timer < 0:
        wave = Wave(window, window.getWidth(), random.randint(0, window.getHeight()))
        waves.append(wave)
        # Reset the enemy spawn timer
        wave_spawn_timer = wave_spawn_rate
    for wave in waves:
        wave.update(delta_time)
        # Remove the enemy from the screen and the list of enemies if it gets to the screen's far left
        if wave.circle.getCenter().getX() < 0:
            wave.circle.undraw()
            waves.remove(waves.index(wave))

    # Collision detection
    for wave in waves:
        if player.circle_collision(wave.circle):
            wave.circle.undraw()
            waves.remove(waves.index(wave))
            collision_counter += 1


    for projectile in projectiles:
        projectile.update(delta_time)
        # Remove the enemy from the screen and the list of enemies if it gets to the screen's far left
        if projectile.circle.getCenter().getX() < 0:
            projectile.circle.undraw()
            projectiles.remove(projectile)


    if collision_counter == 1:
        rec3.health_drop()
    elif collision_counter == 2:
        rec2.health_drop()
    elif collision_counter == 3:
        rec1.health_drop()
        quit = True
        player.collision_with_enemy()
        game_over_text = Text(Point(window.getWidth()/2.0, window.getHeight()/2.0), "Game Over!\nClick to exit.")
        game_over_text.setTextColor("red")
        game_over_text.setStyle("bold italic")
        game_over_text.setSize(20)
        game_over_text.draw(window)


    for chaser1 in chasers:
        for chaser2 in chasers:
            if not chaser1 is chaser2:
                if chaser1.chaser_collision(chaser2):
                    chaser1.circle.undraw()
                    chaser2.circle.undraw()
                    chasers.remove(chaser1)
                    chasers.remove(chaser2)
                    score_counter += 200
                    score.setText(str(score_counter))
    for enemy in enemies:
        for chaser in chasers:
            if chaser.chaser_collision(enemy):
                chaser.circle.undraw()
                enemy.circle.undraw()
                chasers.remove(chaser)
                enemies.remove(enemy)
                score_counter += 200
                score.setText(str(score_counter))
        for wave in waves:
            if wave.wave_collision(enemy):
                wave.circle.undraw()
                enemy.circle.undraw()
                waves.remove(wave)
                enemies.remove(enemy)
                score_counter += 200
                score.setText(str(score_counter))
        for projectile in projectiles:
            if projectile.projectile_collision(enemy):
                projectile.circle.undraw()
                enemy.circle.undraw()
                projectiles.remove(projectile)
                enemies.remove(enemy)
                score_counter += 200
                score.setText(str(score_counter))


    for chaser in chasers:
        for wave in waves:
            if wave.wave_collision(chaser):
                wave.circle.undraw()
                chaser.circle.undraw()
                waves.remove(wave)
                chasers.remove(chaser)
                score_counter += 200
                score.setText(str(score_counter))
        for projectile in projectiles:
            if projectile.projectile_collision(chaser):
                chaser.circle.undraw()
                projectile.circle.undraw()
                chasers.remove(chaser)
                projectiles.remove(projectile)
                score_counter += 200
                score.setText(str(score_counter))

    for wave in waves:
        for projectile in projectiles:
            if projectile.projectile_collision(wave):
                projectile.circle.undraw()
                wave.circle.undraw()
                projectiles.remove(projectile)
                waves.remove(wave)
                score_counter += 200
                score.setText(str(score_counter))


    if keys["q"]:
        quit = True

    last_time = current_time
    frames += 1

window.getMouse()
window.close()
exit()
