import turtle
import random

# 设置屏幕
screen = turtle.Screen()
screen.title("圣诞树生成器 - 小王圣诞快乐")
screen.bgcolor("black")
screen.setup(width=800, height=600)

# 创建绘制工具
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# 绘制彩色文字 "小王圣诞快乐"
def draw_text():
    pen.penup()
    pen.goto(0, -250)
    pen.color("red")
    pen.write("小王圣诞快乐", align="center", font=("Arial", 30, "bold"))

# 绘制动态的圣诞树
def draw_tree():
    tree = turtle.Turtle()
    tree.speed(1)
    tree.hideturtle()
    tree.color("green")

    # 绘制树的主体（分段三角形）
    levels = 3
    base_width = 200
    for i in range(levels):
        width = base_width - (i * 50)
        height = 50
        tree.penup()
        tree.goto(-width / 2, -50 - (i * height))
        tree.pendown()
        tree.begin_fill()
        for _ in range(3):  # 三角形
            tree.forward(width)
            tree.left(120)
        tree.end_fill()

    # 绘制树干
    tree.penup()
    tree.goto(-15, -200)
    tree.pendown()
    tree.color("brown")
    tree.begin_fill()
    for _ in range(2):  # 矩形
        tree.forward(30)
        tree.left(90)
        tree.forward(50)
        tree.left(90)
    tree.end_fill()

# 绘制星星
def draw_star():
    star = turtle.Turtle()
    star.speed(3)
    star.hideturtle()
    star.penup()
    star.goto(0, 100)
    star.color("yellow")
    star.begin_fill()
    for _ in range(5):
        star.forward(50)
        star.right(144)
    star.end_fill()

# 添加随机彩色装饰物
def add_decorations():
    decorations = turtle.Turtle()
    decorations.speed(0)
    decorations.hideturtle()
    colors = ["red", "gold", "blue", "orange"]
    for _ in range(30):  # 随机生成装饰物
        x = random.randint(-90, 90)
        y = random.randint(-180, 100)
        decorations.penup()
        decorations.goto(x, y)
        decorations.pendown()
        decorations.dot(10, random.choice(colors))

# 添加雪花效果
def draw_snowflakes():
    snow = turtle.Turtle()
    snow.speed(0)
    snow.hideturtle()
    snow.color("white")
    for _ in range(50):  # 随机生成雪花
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        snow.penup()
        snow.goto(x, y)
        snow.pendown()
        snow.dot(5)

# 绘制完整的圣诞树
def main():
    draw_text()
    draw_star()
    draw_tree()
    add_decorations()
    draw_snowflakes()
    screen.mainloop()

# 运行
main()
