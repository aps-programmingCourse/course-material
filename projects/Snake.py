#!/usr/bin/python3
# Snake

import turtle, time, random
delay = 0.1

# Score
score = 0
highScore = 0

# Set up the screen
wn = turtle.Screen()
wn.title("snake")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake Head
snakeHead = turtle.Turtle()
snakeHead.speed(0)
snakeHead.shape("square")
snakeHead.color("black")
snakeHead.penup()
snakeHead.goto(0,0)
snakeHead.direction = "stop"

#Food
food = turtle.Turtle()
food.speed (0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# Scoring Turtle
scoreTurtle = turtle.Turtle()
scoreTurtle.speed(10)
scoreTurtle.color("white")
scoreTurtle.penup()
scoreTurtle.sety(250)
scoreTurtle.hideturtle()
scoreTurtle.write("score: 0   high score: 0", align="center", font=("courier", 24, "normal"))

# Functions
def move():
    if snakeHead.direction == "up":
        y = snakeHead.ycor()
        snakeHead.sety(y + 20)
        
    if snakeHead.direction == "down":
        y = snakeHead.ycor()
        snakeHead.sety(y - 20)
        
    if snakeHead.direction == "left":
        x = snakeHead.xcor()
        snakeHead.setx(x - 20)
        
    if snakeHead.direction == "right":
        x = snakeHead.xcor()
        snakeHead.setx(x + 20)

def go_up():
    if snakeHead.direction != "down":
        snakeHead.direction = "up"
      

def go_down():
    if snakeHead.direction != "up":
        snakeHead.direction = "down"
    
def go_left():
    if snakeHead.direction != "right":
        snakeHead.direction = "left"
    
def go_right():
    if snakeHead.direction != "left":
        snakeHead.direction = "right"
        
def writeScore():
  scoreTurtle.clear()
  scoreTurtle.write("Score: {} High Score: {}".format(score, highScore), align="center", font=("courier", 24, "normal"))
    
# keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# main game loop
while True:
  
  wn.update()
  
  # check for a collision with the border
  if snakeHead.xcor() > 290 or snakeHead.xcor() < -290 or snakeHead.ycor() > 290 or snakeHead.ycor() <-290:
      time.sleep(1)
      snakeHead.goto(0,0)
      snakeHead.direction = "stop"
      
      # Hide the segments
      for segment in segments:
          segment.goto(1000,1000)
          
      # clear the segments list
      segments.clear()
      
      # Reset delay 
      delay = 0.1 
      
      #Reset the score 
      score = 0
      
      writeScore()
  
  # Check for a collision with the food
  if snakeHead.distance(food) < 20:
  
  # move food 
      x = random.randint(-290, 209)
      y = random.randint(-290, 290)
      food.goto(x, y)

      # Add a segment
      new_segment = turtle.Turtle()
      new_segment.speed(0)
      new_segment.shape("square")
      new_segment.color("grey")
      new_segment.penup()
      segments.append(new_segment)
      
      # Shorten the delay
      delay-= 0.001
      
      #Increase the score
      score +=10
  
      if score > highScore:
          highScore = score
          
      writeScore()
      
  # Move the end segments first in reversed
  for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)
      
  # Move segments to where the head is  
  if len(segments)>0:
     x = snakeHead.xcor()
     y = snakeHead.ycor()
     segments[0].goto(x, y)
      
  move()
  
  # Check for snake head collision with body
  for segment in segments:
     if segment.distance(snakeHead) < 20:
        time.sleep(1)
        snakeHead.goto(0,0)
        snakeHead.direction = "stop"
        
        # Hide the segments
        for segment in segments:
           segment.goto(1000,1000)
          
        # Clear the segments list
        segments.clear()
        
        # Reset the delay
        delay = 0.1
        
        score = 0
        
        writeScore()
        
  time.sleep(delay)

wn.mainloop()