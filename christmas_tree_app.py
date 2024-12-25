import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random

# 绘制圣诞树的函数
def draw_christmas_tree():
    fig, ax = plt.subplots(figsize=(6, 8), facecolor="black")

    # 绘制树的主体（绿色三角形）
    for i in range(3):
        x = [-i - 1, 0, i + 1]
        y = [-i, 3 - i, -i]
        ax.fill(x, y, color="green")

    # 绘制星星（顶部的黄色五角星）
    star_x = np.array([0, 0.1, 0.5, 0.2, 0.3, 0, -0.3, -0.2, -0.5, -0.1]) * 1.5
    star_y = np.array([1, 0.4, 0.3, 0, -0.5, -0.2, -0.5, 0, 0.3, 0.4]) + 2.7
    ax.fill(star_x, star_y, color="yellow")

    # 绘制树干（棕色矩形）
    ax.fill([-0.3, -0.3, 0.3, 0.3], [-2, -3, -3, -2], color="brown")

    # 随机装饰物（红色和黄色的圆点）
    for _ in range(50):
        x = random.uniform(-3, 3)
        y = random.uniform(-2, 2.7)
        color = random.choice(["red", "gold"])
        ax.scatter(x, y, color=color, s=50)

    # 添加雪花（白色小点）
    for _ in range(100):
        x = random.uniform(-3.5, 3.5)
        y = random.uniform(-3.5, 3.5)
        ax.scatter(x, y, color="white", s=10, alpha=0.7)

    # 设置画布背景色和边界
    ax.set_facecolor("black")
    ax.axis("off")
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-3.5, 3.5)

    return fig

# Streamlit 页面配置
st.set_page_config(page_title="圣诞树生成器", page_icon="🎄", layout="centered")

# 页面标题
st.title("🎄 圣诞树生成器 🎄")

# 添加祝福语
st.markdown("<h2 style='text-align: center; color: red;'>小倩圣诞快乐！🎅🤶</h2>", unsafe_allow_html=True)

# 按钮触发生成圣诞树
if st.button("生成圣诞树"):
    st.pyplot(draw_christmas_tree())

# 底部祝福语
st.write("✨ **Merry Christmas!** ✨")
