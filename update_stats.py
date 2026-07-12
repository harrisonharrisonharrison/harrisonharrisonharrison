import os
import requests
from PIL import Image, ImageDraw, ImageFont

response = requests.get(f"https://api.github.com/users/harrisonharrisonharrison")
data = response.json()

public_repos = data.get("public_repos", 0)
followers = data.get("followers", 0)

image = Image.open("./assets/StatisticsMain.png")
draw = ImageDraw.Draw(image)

# Download a free pixel font (.ttf) and keep it in your src/ folder
font_path = "./pixel_font.ttf"
font_title = ImageFont.truetype(font_path, 24)
font_body = ImageFont.truetype(font_path, 16)

draw.text((141, 110), "HARRISON'S GITHUB STATS", fill=(255, 0, 0), font=font_title) # Red text
draw.text((70, 160), f"> REPOS FOUND: {public_repos}", fill=(255, 255, 255), font=font_body)
draw.text((70, 190), f"> PARTY SIZE:  {followers} FOLLOWER(S)", fill=(255, 255, 255), font=font_body)

image.save("./assets/Statistics_Live.png")
