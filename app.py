import streamlit as st
from PIL import Image, ImageDraw

def create_scene_image(description, width=400, height=300):
    img = Image.new("RGB", (width, height), "skyblue")
    draw = ImageDraw.Draw(img)
    desc = description.lower()

    if "sun" in desc:
        draw.ellipse((300, 20, 360, 80), fill="yellow", outline="orange")
    if "tree" in desc:
        draw.rectangle((50, 180, 90, 280), fill="sienna")
        draw.ellipse((20, 130, 120, 210), fill="green")
    if "grass" in desc:
        draw.rectangle((0, 280, width, height), fill="darkgreen")
    if "night" in desc:
        draw.rectangle((0, 0, width, height), fill="black")
        # Add simple stars
        for x, y in [(50, 50), (100, 80), (200, 60), (300, 100), (350, 50)]:
            draw.ellipse((x, y, x+5, y+5), fill="white")
    return img

st.title("🎨 2D Scene Image Creator")

desc = st.text_area("Enter scene description or keywords (e.g. 'sun, tree, grass, night'):")

if st.button("Generate Image"):
    if not desc.strip():
        st.warning("Please enter a description.")
    else:
        img = create_scene_image(desc)
        st.image(img)
