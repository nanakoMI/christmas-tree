import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random
import time

# Function to draw the Christmas tree with elegance and beauty
def draw_elegant_christmas_tree():
    # Create a figure
    fig, ax = plt.subplots(figsize=(6, 10), facecolor="black")

    # Parameters for the tree
    layers = 6  # Number of layers
    layer_height = 1.5  # Height of each layer
    trunk_width = 1  # Width of the tree trunk

    # Draw the layers of the tree
    for i in range(layers):
        x = [-i - 1, 0, i + 1]  # Triangle vertices for the x-axis
        y = [-(i * layer_height), layer_height - (i * layer_height), -(i * layer_height)]  # Triangle vertices for the y-axis
        ax.fill(x, y, color="#006400")  # Dark green for the tree
        st.pyplot(fig)
        time.sleep(0.3)  # Pause for visual effect

    # Draw the star at the top
    star_x = np.array([0, 0.1, 0.5, 0.2, 0.3, 0, -0.3, -0.2, -0.5, -0.1]) * 1.5
    star_y = np.array([1, 0.4, 0.3, 0, -0.5, -0.2, -0.5, 0, 0.3, 0.4]) + (layers * layer_height)
    ax.fill(star_x, star_y, color="#FFD700")  # Golden star
    st.pyplot(fig)
    time.sleep(0.5)  # Pause for visual effect

    # Draw the trunk
    ax.fill([-trunk_width / 2, -trunk_width / 2, trunk_width / 2, trunk_width / 2], 
            [-layers * layer_height - 0.5, -layers * layer_height - 2, -layers * layer_height - 2, -layers * layer_height - 0.5], 
            color="#8B4513")  # Brown trunk
    st.pyplot(fig)
    time.sleep(0.5)  # Pause for visual effect

    # Add elegant decorations (symmetrical balls and garlands)
    decoration_colors = ["red", "gold", "blue", "silver", "white"]
    for i in range(layers):
        for j in range(3 + i):  # Decorations increase with layers
            x = random.uniform(-i - 0.5, i + 0.5)
            y = -(i * layer_height) + random.uniform(-0.2, 0.2)
            ax.scatter(x, y, color=random.choice(decoration_colors), s=100, alpha=0.9)

        # Draw a garland for each layer
        x_garland = np.linspace(-i - 0.7, i + 0.7, 30)
        y_garland = [-(i * layer_height) + 0.1 * np.sin(4 * np.pi * (xi / (2 * i + 0.1))) for xi in x_garland]
        ax.plot(x_garland, y_garland, color="yellow", lw=2, alpha=0.8)
        st.pyplot(fig)
        time.sleep(0.3)  # Pause for each layer's decorations

    # Add snowflakes in the background
    for _ in range(80):
        x = random.uniform(-layers - 2, layers + 2)
        y = random.uniform(-layers * layer_height - 3, layers * layer_height + 3)
        ax.scatter(x, y, color="white", s=random.randint(20, 50), alpha=0.6)

    # Add holiday greeting text
    ax.text(0, -layers * layer_height - 4, "🎄 小王圣诞快乐！ 🎅", fontsize=20, color="red", ha="center", va="center")

    # Finalize the plot
    ax.axis("off")  # Hide axes
    ax.set_xlim(-layers - 1, layers + 1)
    ax.set_ylim(-layers * layer_height - 5, layers * layer_height + 3)

    st.pyplot(fig)  # Render the final tree

# Streamlit page configuration
st.set_page_config(page_title="优雅圣诞树生成器", page_icon="🎄", layout="centered")

# Page title
st.title("🎄 优雅圣诞树生成器 🎄")

# Holiday greeting
st.markdown("<h2 style='text-align: center; color: red;'>小王圣诞快乐！🎅🤶</h2>", unsafe_allow_html=True)

# Button to generate the Christmas tree
if st.button("生成优雅圣诞树"):
    draw_elegant_christmas_tree()

# Footer
st.write("✨ **Merry Christmas and Happy New Year!** ✨")
