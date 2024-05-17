import turtle
import random

# 设置屏幕
screen = turtle.Screen()
screen.title("小球接接乐")
screen.bgcolor("black")
screen.setup(width=600, height=600)

# 创建托盘
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# 创建小球
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.speed(0)
ball.goto(0, 250)
ball.dy = -10  # 加快速度
ball.dx = 3   # 水平速度

# 移动托盘
def move_left():
    x = paddle.xcor()
    x -= 20
    if x < -280:
        x = -280
    paddle.setx(x)

def move_right():
    x = paddle.xcor()
    x += 20
    if x > 280:
        x = 280
    paddle.setx(x)

# 键盘绑定
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# 主循环
while True:
    screen.update()

    # 移动小球
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # 边界检测
    if ball.ycor() > 290:
        ball.dy *= -1
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1

    # 碰撞检测
    if (ball.ycor() < -240 and paddle.xcor() - 40 < ball.xcor() < paddle.xcor() + 40):
        ball.dy *= -1

    # 游戏结束
    if ball.ycor() < -290:
        ball.hideturtle()
        paddle.hideturtle()
        turtle.write("游戏结束", align="center", font=("Courier", 24, "normal"))
        break

screen.mainloop()
