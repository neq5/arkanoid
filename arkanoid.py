#!/usr/bin/env python3
# pip3 install pgzero

import random
import pgzrun
import sys

TITLE = "Arkanoid by neq5@o2.pl"

BALL_SPEED = 5

WIDTH = 800
HEIGHT = 800

BALL_X_SPEED = BALL_SPEED
BALL_Y_SPEED = BALL_SPEED

loser = 0

paddle = Actor("palette.png")
paddle.x = WIDTH // 2
paddle.y = 790

ball = Actor("ball.png")
ball.x = 30
ball.y = 300

bars_list = []

def place_bars(x,y,image):
    bar_x = x
    bar_y = y
    for i in range(25):
        bar = Actor(image)
        bar.x = bar_x
        bar.y = bar_y
        bar_x += 31
        bars_list.append(bar)

box_list = ["red.png", "blue.png", "yellow.png", "pink.png"]

x = 25
y = 50

for color in box_list:
    place_bars(x, y, color)
    y += 31

def check_loser():
    global loser
    if loser:
        sys.exit("game over")
        
def update_ball():
    global BALL_X_SPEED, BALL_Y_SPEED, loser
    ball.x -= BALL_X_SPEED
    ball.y -= BALL_Y_SPEED

    if (ball.x >= WIDTH) or (ball.x <=0):
        BALL_X_SPEED *= -1

    if ball.y <= 0:
        BALL_Y_SPEED *= -1
    if ball.y >= HEIGHT:
        loser = 1

def draw():
    screen.clear()
    paddle.draw()
    ball.draw()

    for bar in bars_list:
        bar.draw()

def update():
    global BALL_X_SPEED, BALL_Y_SPEED, loser
    if keyboard.left:
        if paddle.x >= 1:
            paddle.x = paddle.x - 5
    if keyboard.right:
        if paddle.x <= WIDTH:
            paddle.x = paddle.x + 5
    
    update_ball()

    if len(bars_list) == 0:
        sys.exit("winner!")

    for bar in bars_list:
        if ball.colliderect(bar):
            bars_list.remove(bar)
            BALL_Y_SPEED *= -1

    if paddle.colliderect(ball):
        BALL_Y_SPEED *= -1
        rand = random.randint(0,1)
        if rand:
            BALL_X_SPEED *= -1

    check_loser()

pgzrun.go()
