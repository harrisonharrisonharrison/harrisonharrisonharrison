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

# 3. Draw the retro text onto the brick wall
draw.text((50, 50), "HARRISONHARRISONHARRISON'S GITHUB STATS", fill=(255, 0, 0), font=font_title) # Red text
draw.text((50, 100), f"> REPOS FOUND: {public_repos}", fill=(255, 255, 255), font=font_body)
draw.text((50, 130), f"> PARTY SIZE:  {followers} FOLLOWER(S)", fill=(255, 255, 255), font=font_body)

# 4. Save over the live file that your CHAMBER_STATS.md links to
image.save("./assets/Statistics_Live.png")
print("Successfully baked live stats into the pixel-art grid!")