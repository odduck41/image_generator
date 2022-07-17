from PIL import Image,\
     ImageDraw,\
     ImageFont
import random
import json

bg_color = random.choice(json.load(open("colors.json", "rb"))["colors"])
text_color = random.choice(json.load(open("colors.json", "rb"))["colors"])

img=Image.new("RGB", (1277, 715), color = (bg_color))
font = ImageFont.truetype("arial.ttf", size=40)
text = ImageDraw.Draw(img)
text.text(
    (15, img.width/4),
    f"Only {text_color} text on the {bg_color} background",
    fill=text_color,
    font=font
)

img.save(f"{text_color} on {bg_color}.png")
