import streamlit as st
import os

st.title("🖼️ 2D Image Assets Preview")

assets_folder = "assets"
if not os.path.exists(assets_folder):
    st.error("Assets folder not found. Run 'generate_assets.py' first.")
else:
    images = os.listdir(assets_folder)
    images = [img for img in images if img.endswith(".png")]

    for img_name in images:
        st.image(os.path.join(assets_folder, img_name), caption=img_name)
