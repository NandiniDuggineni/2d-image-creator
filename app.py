import streamlit as st
import os

# Import the image generator function (you'll need to update generate_assets.py accordingly)
from generate_assets import generate_all_assets

st.title("2D Image Assets Preview")

assets_folder = "assets"

# Check if assets folder exists and has images; if not, generate assets
if not os.path.exists(assets_folder) or len(os.listdir(assets_folder)) == 0:
    st.info("Assets not found or empty. Generating 2D image assets now...")
    generate_all_assets()
    st.success("Image assets generated!")

# List PNG images in assets folder
images = [img for img in os.listdir(assets_folder) if img.lower().endswith(".png")]

if not images:
    st.warning("No PNG images found in the assets folder.")
else:
    for img_name in images:
        img_path = os.path.join(assets_folder, img_name)
        st.image(img_path, caption=img_name)

