import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Happy 3rd Anniversary! 💖")
st.write("Love you always and forever ❤️")

# Create a heart shape using Matplotlib
t = np.linspace(0, 2 * np.pi, 100)
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

fig, ax = plt.subplots()
ax.plot(x, y, color="red")
ax.set_aspect('equal')
ax.axis('off')

st.pyplot(fig)

# Display your photo
image_path = "KakaoTalk_20241118_043307704.jpg"  # Replace with your photo file path
try:
    from PIL import Image
    img = Image.open(image_path)
    st.image(img, caption="A lovely memory together", use_column_width=True)
except Exception as e:
    st.error(f"Error displaying your photo: {e}")



