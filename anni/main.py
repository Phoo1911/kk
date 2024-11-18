import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Happy 3 years Anniversary! 💖")
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




