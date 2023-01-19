import colorama
from colorama import Style, Back, Fore
import os
import sys
import subprocess
import discord
import tkinter as tk
import turtle as t
import time
import socket
from subprocess import call

colorama.init(autoreset=True)

console = input(f"""
{Fore.CYAN}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⠾⠿⠿⠯⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣾⠛⠁⠀⠀⠀⠀⠀⠀⠈⢻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠿⠁⠀⠀⠀⢀⣤⣾⣟⣛⣛⣶⣬⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠟⠃⠀⠀⠀⠀⠀⣾⣿⠟⠉⠉⠉⠉⠛⠿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠋⠀⠀⠀⠀⠀⠀⠀⣿⡏⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣼⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠷⣤⣤⣠⣤⣤⡤⡶⣶⢿⠟⠹⠿⠄⣿⣿⠏⠀⣀⣤⡦⠀⠀⠀⠀⣀⡄
⢀⣄⣠⣶⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠓⠚⠋⠉⠀⠀⠀⠀⠀⠀⠈⠛⡛⡻⠿⠿⠙⠓⢒⣺⡿⠋⠁
⠉⠉⠉⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀
{Fore.WHITE}______________________________________________________________________________

{Fore.BLUE}Welcome to the Sea. Please choose the following option.
{Fore.WHITE}
[1] Info
[2] Start
[3] Exit

> """)
if console == "1":
    print("The Sea is a command from TuraOS Made by Wernox. It lets you play Snake Game on the TuraOS terminal. I hope you enjoy!")
    time.sleep(4)
    os.system('cls')
    def open_py_file():
      call(["python", "C:\\Users\\Admin\\Desktop\\TuraOS\\bin\\sea.py"])

    open_py_file()
if console == "2":
    import turtle 
    import random
    import time
    import subprocess
    from subprocess import call

    screen = turtle.Screen()
    screen.title("Snake Game")
    screen.setup(width=700,height=700)
    screen.tracer(0)
    screen.bgcolor("#1d1d1d")

    turtle.speed(5)
    turtle.pensize(4)
    turtle.penup()
    turtle.goto(-310, 250)
    turtle.pendown()
    turtle.color("red")
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(500)
    turtle.penup()
    turtle.hideturtle()

    score = 0
    delay = 0.1

    snake = turtle.Turtle()
    snake.speed()
    snake.shape('square')
    snake.color("green")
    snake.penup()
    snake.goto(0, 0)
    snake.direction = 'stop'

    fruit = turtle.Turtle()
    fruit.speed(0)
    fruit.shape("square")
    fruit.color("white")
    fruit.penup()
    fruit.goto(30, 30)

    old_fruit = []

    scoring = turtle.Turtle()
    scoring.speed(0)
    scoring.color("white")
    scoring.penup()
    scoring.hideturtle()
    scoring.goto(0, 300)
    scoring.write("Points: ", align="center", font=("Courier", 24, "bold"))
    def snake_go_up():
        if snake.direction != "down":
            snake.direction = "up"
    def snake_go_down():
        if snake.direction != "up":
            snake.direction = "down"
    def snake_go_left():
        if snake.direction != "right":
            snake.direction = "left"
    def snake_go_right():
        if snake.direction != "left":
            snake.direction = "right"
    def snake_move():
        if snake.direction == "up":
            y = snake.ycor()
            snake.sety(y + 20)
        if snake.direction == "down":
            y = snake.ycor()
            snake.sety(y - 20)
        if snake.direction == "left":
            x = snake.xcor()
            snake.setx(x - 20)
        if snake.direction == "right":
            x = snake.xcor()
            snake.setx(x + 20)

    screen.listen()
    screen.onkeypress(snake_go_up, "Up")
    screen.onkeypress(snake_go_down, "Down")
    screen.onkeypress(snake_go_left, "Left")
    screen.onkeypress(snake_go_right, "Right")

    while True:
        screen.update()

        if snake.distance(fruit) < 20:
            x = random.randint(-290, 270)
            y = random.randint(-240, 240)
            fruit.goto(x, y)
            scoring.clear()
            score += 1
            scoring.write("Points: {}".format(score), align="center", font=("Courier", 24, "bold"))
            delay -= 0.001

            new_fruit = turtle.Turtle()
            new_fruit.speed(0)
            new_fruit.shape("square")
            new_fruit.color("red")
            new_fruit.penup()
            old_fruit.append(new_fruit)
        
        for index in range(len(old_fruit) -1, 0, -1):
            a = old_fruit[index -1].xcor()
            b = old_fruit[index -1].ycor()

            old_fruit[index].goto(a, b)

        if len(old_fruit) > 0:
            a = snake.xcor()
            b = snake.ycor()
            old_fruit[0].goto(a, b)
        snake_move()

        if snake.xcor() > 280 or snake.xcor() < -300 or snake.xcor() > 240 or snake.xcor() < -240:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            scoring.goto(0,0)
            scoring.write("   Game over!  \n Your score is {}".format(score), align="center", font=("Courier", 30, "bold"))
        
        for food in old_fruit:
            if food.distance(snake) < 20:
                time.sleep(1)
                screen.clear()
                screen.bgcolor("turquoise")
                scoring.goto(0,0)
                scoring.write("   Game over!  \n Your score is {}".format(score), align="center", font=("Courier", 30, "bold"))
        
        
        time.sleep(delay)
        
if console == "3":
    question = input(f"Are you sure you want to quit The Sea? {Fore.GREEN}Y{Fore.WHITE}/{Fore.RED}N{Fore.WHITE} ")
    if question == "Y":
        def open_py_file():
          call(["python", "C:\\Users\\Admin\\Desktop\\TuraOS\\term\\terminal.py"])

        open_py_file()
    if question == "N":
        def open_py_file():
          call(["python", "C:\\Users\\Admin\\Desktop\\TuraOS\\bin\\sea.py"])

        open_py_file()