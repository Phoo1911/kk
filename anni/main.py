
from turtle import *
import streamlit as st
from PIL import Image
import math

st.title("Happy 3rd Anniversary! 💖")
st.write("Love you always and forever ❤️")

# Display your photo
image_path = "KakaoTalk_20241118_043307704.jpg"  # Replace with your image file
try:
    img = Image.open(image_path)
    st.image(img, caption="A lovely memory together", use_column_width=True)
except Exception as e:
    st.error(f"Error displaying your photo: {e}")


# Function to draw a heart using Turtle and save as an image
def draw_heart_image(filename="heart.png"):
    speed(0)
    bgcolor("black")
    color("red")
    penup()
    goto(0, 0)
    pendown()

    for i in range(100):
        h = 12 * math.sin(i) ** 3
        goto(h * 20, (12 * math.cos(i) - 5 * math.cos(2 * i) - 2 * math.cos(3 * i) - math.cos(4 * i)) * 20)

    penup()
    goto(0, 0)
    done()

    # Save the drawing as an image (use a screenshot tool or manually save)
    print("Drawing completed. Please save the drawing manually.")


