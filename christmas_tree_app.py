import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random
import time

# Function to dynamically draw a beautifully decorated Christmas tree
def draw_beautiful_christmas_tree():
    # Create a figure
    fig, ax = plt.subplots(figsize=(6, 8), facecolor="black")
    
    # Parameters for the tree
    layers = 6  # Number of layers
    layer_height = 1.5  # Height of each layer
    
    # Draw the layers of the tree one by one (dynamic effect)
    for i in range(layers):
        x = [-i - 1, 0, i + 1]  # Triangle vertices for the x-axis
        y = [-(i * layer_height), layer_height - (i * layer_height), -(i * layer_height)]  # Triangle vertices for the y-axis
        ax.fill(x, y, color="#228B22")  # Use a darker green for the tree
        st.pyplot(fig)
        time.sleep(0.5)  # Pause for visual effect
    
    # Draw the star at the top
    star_x = np.array([0, 0.1, 0.5, 0.2, 0.3, 0, -0.3, -0.2, -0.5, -0.1]) * 1.5
    star_y = np.array([1, 0.4, 0.3, 0, -0.5, -0.2, -0.5, 0, 0.3, 0.4]) + (layers * layer_height)
    ax.fill(star_x, star_y, color="gold")  # Golden star
    st.pyplot(fig)
    time.sleep(0.5)  # Pause for visual effect

    # Draw the trunk
    ax.fill([-0.5, -0.5, 0.5, 0.5], [-layers * layer_height - 0.5, -layers * layer_height - 2, -layers * layer_height - 2, -layers * layer_height - 0.5], color="#8B4513")
    st.pyplot(fig)
    time.sleep(0.5)  # Pause for visual effect

    # Add decorations (balls and garlands dynamically)
    for _ in range(80):
        x = random.uniform(-layers, layers)  # Random x position
        y = random.uniform(-(layers * layer_height), layers * layer_height)  # Random y position
        if y < layer_height * layers and abs(x) < (layers - abs(y) / layer_height):  # Ensure decorations are within the tree
            ax.scatter(x, y, color=random.choice(["red", "gold", "blue", "silver", "white"]), s=50, alpha=0.8)
            st.pyplot(fig)
            time.sleep(0.05)  # Small pause for each decoration

    # Add garlands (horizontal curved lines dynamically)
    for i in range(1, layers):
        y = -(i * layer_height) + layer_height / 2
        x = np.linspace(-i, i, 100)
        ax.plot(x, y - 0.1 * np.sin(5 * np.pi * x / i), color="yellow", lw=2, alpha=0.6)
        st.pyplot(fig)
        time.sleep(0.2)  # Pause for each garland

    # Add snowflakes in the background
    for _ in range(150):
        x = random.uniform(-layers - 2, layers + 2)
        y = random.uniform(-layers * layer_height - 2, layers * layer_height + 2)
        ax.scatter(x, y, color="white", s=random.randint(10, 30), alpha=0.5)
    
    # Add text for a holiday greeting
    ax.text(0, -layers * layer_height - 3, "🎄 小王圣诞快乐！ 🎅", fontsize=20, color="red", ha="center", va="center")
    st.pyplot(fig)  # Final render

# Streamlit page configuration
st.set_page_config(page_title="美化圣诞树生成器", page_icon="🎄", layout="centered")

# Page title
st.title("🎄 动态美化圣诞树生成器 🎄")

# Holiday greeting
st.markdown("<h2 style='text-align: center; color: red;'>倩倩圣诞快乐！🎅🤶</h2>", unsafe_allow_html=True)

# Button to generate the Christmas tree
if st.button("生成动态圣诞树"):
    draw_beautiful_christmas_tree()

# Footer
st.write("✨ **Merry Christmas and Happy New Year!** ✨")
