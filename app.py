import streamlit as st
from gtts import gTTS
import os
import tempfile
from PIL import Image, ImageDraw, ImageFont

st.set_page_config(page_title="Storytelling App", page_icon="📖")

# Root directory of your script
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# ----- Image creation functions -----

def draw_star(draw, center, size, color):
    from math import sin, cos, pi
    points = []
    for i in range(10):
        angle = i * pi / 5  # 36 degrees step
        r = size if i % 2 == 0 else size / 2
        x = center[0] + r * sin(angle)
        y = center[1] - r * cos(angle)
        points.append((x, y))
    draw.polygon(points, fill=color)

def create_luma_scene(filename, width=400, height=300):
    img = Image.new("RGB", (width, height), "midnightblue")
    draw = ImageDraw.Draw(img)

    # Draw moon crescent
    draw.ellipse((280, 30, 360, 110), fill="lightyellow")
    draw.ellipse((300, 30, 380, 110), fill="midnightblue")

    # Draw stars cluster
    star_positions = [(50, 50), (80, 90), (120, 40), (160, 80), (200, 50)]
    for pos in star_positions:
        draw_star(draw, pos, 15, "white")

    # Draw Luma - bigger shining star with glow
    glow_radius = 25
    for alpha in range(20, 0, -2):
        glow_color = (255, 255, 200, int(12 * alpha))
        glow_img = Image.new("RGBA", (width, height))
        glow_draw = ImageDraw.Draw(glow_img)
        glow_draw.ellipse(
            [150 - glow_radius, 150 - glow_radius, 150 + glow_radius, 150 + glow_radius],
            fill=glow_color,
        )
        img = Image.alpha_composite(img.convert("RGBA"), glow_img)

    draw_star(draw, (150, 150), 20, "yellow")

    # Add text label
    try:
        font = ImageFont.truetype("arial.ttf", 18)
    except:
        font = ImageFont.load_default()
    draw.text((140, 180), "Luma", fill="yellow", font=font)

    img.convert("RGB").save(filename)

# ----- Story & TTS functions -----

def load_story(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return [scene.strip() for scene in f.read().split("\n\n") if scene.strip()]

def generate_tts(text, lang="en"):
    tts = gTTS(text=text, lang=lang)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_file.name)
    return temp_file.name

# ----- Streamlit UI -----

st.title("📖 Minimal Storytelling App with 2D Images")

# Load stories
stories_dir = os.path.join(ROOT_DIR, "stories")
if not os.path.isdir(stories_dir):
    st.error(f"Stories folder not found at `{stories_dir}`. Please upload the 'stories' folder.")
else:
    story_files = [f for f in os.listdir(stories_dir) if f.endswith(".txt")]
    if not story_files:
        st.warning(f"No story files found in `{stories_dir}`.")
    else:
        story_choice = st.selectbox("Choose a Story:", story_files)

        if story_choice:
            story_path = os.path.join(stories_dir, story_choice)
            scenes = load_story(story_path)

            # Generate and display special Luma scene image
            scene_image_path = os.path.join(ROOT_DIR, "static", "luma_scene.jpg")
            if not os.path.exists(scene_image_path):
                create_luma_scene(scene_image_path)
            st.image(scene_image_path)

            # Background music path
            bg_music_path = os.path.join(ROOT_DIR, "static", "soft_music.mp3")
            if os.path.exists(bg_music_path):
                st.audio(bg_music_path, format="audio/mp3", start_time=0)

            # Display story text
            full_story = "\n\n".join(scenes)
            st.write(full_story)

            if st.button("▶ Play Narration for Full Story"):
                audio_file = generate_tts(full_story)
                with open(audio_file, "rb") as f:
                    audio_bytes = f.read()
                st.audio(audio_bytes, format="audio/mp3")
