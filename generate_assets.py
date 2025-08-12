from PIL import Image, ImageDraw
from math import sin, cos, pi
import os

def draw_cat(filename, size=100):
    img = Image.new("RGBA", (size, size), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([20, 20, 80, 80], fill="#d9b382")  # face
    draw.polygon([(20,20), (35,5), (50,20)], fill="#d9b382")  # left ear
    draw.polygon([(80,20), (65,5), (50,20)], fill="#d9b382")  # right ear
    draw.ellipse([35, 45, 45, 55], fill="black")  # left eye
    draw.ellipse([55, 45, 65, 55], fill="black")  # right eye
    draw.polygon([(50,60), (45,65), (55,65)], fill="pink")   # nose
    img.save(filename)

def draw_dog(filename, size=100):
    img = Image.new("RGBA", (size, size), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([20, 30, 80, 90], fill="#a0522d")  # head
    draw.rectangle([15, 15, 35, 40], fill="#a0522d")  # left ear
    draw.rectangle([65, 15, 85, 40], fill="#a0522d")  # right ear
    draw.ellipse([35, 55, 45, 65], fill="black")  # left eye
    draw.ellipse([55, 55, 65, 65], fill="black")  # right eye
    draw.ellipse([48, 75, 52, 79], fill="black")  # nose
    img.save(filename)

def draw_bird(filename, size=100):
    img = Image.new("RGBA", (size, size), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([30, 40, 70, 80], fill="deepskyblue")  # body
    draw.ellipse([50, 20, 70, 40], fill="deepskyblue")  # head
    draw.polygon([(70,30), (80,35), (70,40)], fill="orange")  # beak
    draw.ellipse([60, 30, 65, 35], fill="black")  # eye
    draw.polygon([(40,60), (55,65), (40,70)], fill="lightskyblue")  # wing
    img.save(filename)

def draw_fish(filename, size=100):
    img = Image.new("RGBA", (size, size), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([20, 40, 80, 70], fill="gold")  # body
    draw.polygon([(20,40), (10,55), (20,70)], fill="orange")  # tail
    draw.ellipse([65, 50, 70, 55], fill="black")  # eye
    draw.line([(75, 55), (80, 55)], fill="red", width=2)  # mouth
    img.save(filename)

def draw_tree(filename, size=100):
    img = Image.new("RGBA", (size, size), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    draw.rectangle([45, 70, 55, 100], fill="#8B5A2B")  # trunk
    draw.polygon([(25, 70), (50, 30), (75, 70)], fill="forestgreen")  # leaves big
    draw.polygon([(30, 50), (50, 20), (70, 50)], fill="green")  # leaves small
    img.save(filename)

def draw_cloud(filename, size=100):
    img = Image.new("RGBA", (size, size), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([20, 40, 60, 80], fill="white")
    draw.ellipse([40, 30, 80, 70], fill="white")
    draw.ellipse([60, 40, 100, 80], fill="white")
    img.save(filename)

def draw_moon(filename, size=100):
    img = Image.new("RGBA", (size, size), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([20, 20, 80, 80], fill="lightyellow")  # full moon
    draw.ellipse([40, 20, 90, 80], fill=(0,0,0,0))  # transparent layer
    draw.ellipse([50, 20, 90, 80], fill="midnightblue")  # crescent shadow
    img.save(filename)

def draw_star(filename, size=100, color="yellow"):
    img = Image.new("RGBA", (size, size), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    cx, cy = size//2, size//2
    r_outer = size//2 - 5
    r_inner = r_outer//2
    points = []
    for i in range(10):
        angle = i * pi / 5
        r = r_outer if i %2 == 0 else r_inner
        x = cx + r * sin(angle)
        y = cy - r * cos(angle)
        points.append((x,y))
    draw.polygon(points, fill=color)
    img.save(filename)

def draw_forest_background(filename, width=400, height=300):
    img = Image.new("RGB", (width, height), "skyblue")
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, height*0.7, width, height], fill="darkgreen")  # grass
    tree_positions = [50, 130, 210, 290, 370]
    for x in tree_positions:
        draw.rectangle([x-10, height*0.7, x+10, height], fill="#8B5A2B")  # trunk
        draw.polygon([(x-30, height*0.7), (x, height*0.4), (x+30, height*0.7)], fill="forestgreen")  # leaves big
        draw.polygon([(x-25, height*0.55), (x, height*0.3), (x+25, height*0.55)], fill="green")  # leaves small
    img.save(filename)

def generate_all_assets():
    os.makedirs("assets", exist_ok=True)
    draw_cat("assets/cat.png")
    draw_dog("assets/dog.png")
    draw_bird("assets/bird.png")
    draw_fish("assets/fish.png")
    draw_tree("assets/tree.png")
    draw_cloud("assets/cloud.png")
    draw_moon("assets/moon.png")
    draw_star("assets/star.png")
    draw_forest_background("assets/forest_background.png")
    print("All images generated in the 'assets' folder.")

if __name__ == "__main__":
    generate_all_assets()
