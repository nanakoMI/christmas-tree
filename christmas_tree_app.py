import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random

# Function to draw the Christmas tree
def draw_custom_christmas_tree():
    # Create a figure
    fig, ax = plt.subplots(figsize=(6, 10), facecolor="black")

    # Parameters for the tree
    tree_width = 6  # Width of the base of the tree
    tree_height = 9  # Height of the tree
    decoration_colors = ["red", "gold", "orange"]  # Colors for decorations

    # Draw the tree as a filled triangle
    tree_x = [-tree_width / 2, 0, tree_width / 2]
    tree_y = [0, tree_height, 0]
    ax.fill(tree_x, tree_y, color="green", zorder=1)

    # Draw the star at the top
    star_x = np.array([0, 0.2, 0.5, 0.3, 0.4, 0, -0.4, -0.3, -0.5, -0.2]) * 1.2
    star_y = np.array([1, 0.4, 0.3, 0, -0.5, -0.2, -0.5, 0, 0.3, 0.4]) + tree_height
    ax.fill(star_x, star_y, color="yellow", zorder=2)

    # Add decorations to the tree
    for _ in range(70):  # Number of decorations
        x = random.uniform(-tree_width / 2 + 0.3, tree_width / 2 - 0.3)
        y = random.uniform(0.3, tree_height - 0.3)
        if abs(x) < (tree_width / 2) * (y / tree_height):  # Ensure decorations are within the tree
            ax.scatter(x, y, color=random.choice(decoration_colors), s=100, zorder=3)

    # Add snowflakes in the background
    for _ in range(120):  # Number of snowflakes
        x = random.uniform(-tree_width - 2, tree_width + 2)
        y = random.uniform(-1, tree_height + 2)
        ax.scatter(x, y, color="white", s=random.randint(10, 30), alpha=0.7, zorder=0)

    # Add the text at the bottom
    ax.text(0, -1, "Merry Christmas", fontsize=20, color="red", ha="center", va="center", bbox=dict(facecolor="white", edgecolor="none", boxstyle="round,pad=0.5"))

    # Finalize the plot
    ax.axis("off")  # Hide axes
    ax.set_xlim(-tree_width - 1, tree_width + 1)
    ax.set_ylim(-2, tree_height + 2)

    return fig

# Streamlit page configuration
st.set_page_config(page_title="圣诞树生成器", page_icon="🎄", layout="centered")

# Page title
st.title("🎄 自定义圣诞树生成器 🎄")

# Button to generate the Christmas tree
if st.button("生成圣诞树"):
    st.pyplot(draw_custom_christmas_tree())

# Footer
st.write("✨ **Merry Christmas and Happy New Year!** ✨")

