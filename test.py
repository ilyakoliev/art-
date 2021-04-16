import streamlit as st
from PIL import Image, ImageDraw
import random

st.title("Фигуры это искусство?")
ans = st.radio('Добавить кружочков', ['да', 'нет'], index=1)

go = st.button('🎲')
if go:
    image = Image.new('RGB', (2400, 2400), 'white')
    draw = ImageDraw.Draw(image)
    
    if ans == 'да':
        for i in range(0, 60):
            x1 = random.randint(1, 12) * 200 - 50
            y1 = random.randint(1, 12) * 200 - 50
            draw.ellipse((x1 - 25, y1 - 25, x1 + 25, y1 + 25), fill='black', outline='black')

    for i in range(0, random.randint(3, 8)):
        points = random.randint(3, 8)
        xy = []
        for j in range(0, points):
            x = random.randint(1, 12) * 200 - 100
            y = random.randint(1, 12) * 200 - 100
            xy.append((x, y))
        xy.append(xy[0])
        draw.polygon(xy, outline="black")

    image.save('draw-art.jpg', quality = 100)
    st.image('draw-art.jpg')
