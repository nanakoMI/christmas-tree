import turtle
import random

# 初始化屏幕
screen = turtle.Screen()
screen.title("圣诞树生成器 - 小王圣诞快乐")
screen.bgcolor("black")
screen.setup(width=800, height=600)

# 创建画笔
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# 动态绘制 "小王圣诞快乐" 的文字
def draw_text():
    pen.penup()
    pen.goto(0, -250)
    pen.color("red")
    pen.write("小王圣诞快乐", align="center", font=("Arial", 30, "bold"))

# 绘制圣诞树的主体部分
def draw_tree():
    tree = turtle.Turtle()
    tree.speed(3)
    tree.hideturtle()
    tree.color("green")

    # 绘制树的主体（多层三角形）
    levels = 5  # 树的层数
    base_width = 240
    for i in range(levels):
        width = base_width - (i * 40)
        height = 50
        tree.penup()
        tree.goto(-width / 2, -50 - (i * height))
        tree.pendown()
        tree.begin_fill()
        for _ in range(3):  # 绘制三角形
            tree.forward(width)
            tree.left(120)
        tree.end_fill()

# 绘制圣诞树顶部的星星
def draw_star():
    star = turtle.Turtle()
    star.speed(2)
    star.hideturtle()
    star.penup()
    star.goto(0, 120)
    star.color("yellow")
    star.begin_fill()
    for _ in range(5):
        star.forward(40)
        star.right(144)
    star.end_fill()

# 添加彩色装饰物（动态效果）
def add_decorations():
    decorations = turtle.Turtle()
    decorations.speed(0)
    decorations.hideturtle()
    colors = ["red", "gold", "blue", "orange", "white"]
    for _ in range(40):
        x = random.randint(-100, 100)
        y = random.randint(-180, 100)
        decorations.penup()
        decorations.goto(x, y)
        decorations.pendown()
        decorations.dot(10, random.choice(colors))

# 添加动态雪花
def draw_snowflakes():
    snow = turtle.Turtle()
    snow.speed(0)
    snow.hideturtle()
    snow.color("white")
    for _ in range(50):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        snow.penup()
        snow.goto(x, y)
        snow.pendown()
        snow.dot(5)

# 绘制圣诞树的树干
def draw_trunk():
    trunk = turtle.Turtle()
    trunk.speed(2)
    trunk.hideturtle()
    trunk.color("brown")
    trunk.penup()
    trunk.goto(-15, -250)
    trunk.pendown()
    trunk.begin_fill()
    for _ in range(2):  # 绘制矩形
        trunk.forward(30)
        trunk.left(90)
        trunk.forward(50)
        trunk.left(90)
    trunk.end_fill()

# 绘制完整的圣诞树
def main():
    draw_text()  # 绘制祝福文字
    draw_star()  # 绘制顶部星星
    draw_tree()  # 绘制圣诞树主体
    draw_trunk()  # 绘制树干
    add_decorations()  # 添加装饰
    draw_snowflakes()  # 添加雪花
    screen.mainloop()

# 启动程序
main()

