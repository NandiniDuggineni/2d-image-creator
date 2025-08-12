import streamlit as st
import os

st.title("2D Image Assets Preview")

assets_folder = "assets"
if not os.path.exists(assets_folder):
    st.error("Assets folder not found. Run 'generate_assets.py' first.")
else:
    images = [img for img in os.listdir(assets_folder) if img.lower().endswith(".png")]

    if not images:
        st.warning("No PNG images found in the assets folder.")
    else:
        for img_name in images:
            img_path = os.path.join(assets_folder, img_name)
            st.image(img_path, caption=img_name)

