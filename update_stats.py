import os
import requests
from collections import defaultdict
from PIL import Image, ImageDraw, ImageFont

USERNAME = "harrisonharrisonharrison"
TOKEN = os.getenv("GITHUB_TOKEN") 
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

query = """
query($login: String!) {
  user(login: $login) {
    followers { totalCount }
    repositoriesContributedTo { totalCount }
    issues { totalCount }
    pullRequests { totalCount }
    mergedPRs: pullRequests(states: MERGED) { totalCount }
    contributionsCollection { totalCommitContributions }
    repositories(first: 100, ownerAffiliations: OWNER, isFork: false, orderBy: {field: PUSHED_AT, direction: DESC}) {
      nodes {
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
          edges {
            size
            node { name }
          }
        }
      }
    }
  }
}
"""

response = requests.post(
    "https://api.github.com/graphql", 
    json={"query": query, "variables": {"login": USERNAME}}, 
    headers=HEADERS
)
data = response.json()["data"]["user"]

followers = data["followers"]["totalCount"]
repos_contributed = data["repositoriesContributedTo"]["totalCount"]
total_issues = data["issues"]["totalCount"]
total_prs = data["pullRequests"]["totalCount"]
merged_prs = data["mergedPRs"]["totalCount"]
total_commits = data["contributionsCollection"]["totalCommitContributions"]

pr_percentage = 0
if total_prs > 0:
    pr_percentage = int((merged_prs / total_prs) * 100)

language_sizes = defaultdict(int)
for repo in data["repositories"]["nodes"]:
    for edge in repo["languages"]["edges"]:
        language_sizes[edge["node"]["name"]] += edge["size"]

top_languages = sorted(language_sizes.items(), key=lambda x: x[1], reverse=True)[3:6]
top_language_names = [lang[0] for lang in top_languages]

image = Image.open("./assets/StatisticsMain.png")
draw = ImageDraw.Draw(image)

font_path = "./pixel_font.ttf"
font_title = ImageFont.truetype(font_path, 24)
font_body = ImageFont.truetype(font_path, 16)

# Colors
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 85, 85)
COLOR_GOLD = (255, 215, 0)  

def draw_stat(draw, x, y, key_text, value_text, font):
    draw.text((x, y), key_text, fill=COLOR_WHITE, font=font)
    key_width = draw.textlength(key_text, font=font)
    draw.text((x + key_width, y), str(value_text), fill=COLOR_GOLD, font=font)

title_x = 141
start_x = 70
current_y = 110
line_height = 30

# Title
draw.text((title_x, current_y), "HARRISON'S GITHUB STATS", fill=COLOR_RED, font=font_title)
current_y += 50

# Stats
draw_stat(draw, start_x, current_y, "> PARTY SIZE: ", f"{followers} FOLLOWERS", font_body)
key_length = draw.textlength("> PARTY SIZE: ", font=font_body)
followers_length = draw.textlength(f"{followers} FOLLOWERS", font=font_body)
draw.text((start_x + 5 + key_length + followers_length, current_y), '(click back and follow me!)', fill=COLOR_WHITE, font=font_body)
current_y += line_height

draw_stat(draw, start_x, current_y, "> REPOSITORIES CONTRIBUTED TO (PAST YEAR): ", repos_contributed, font_body)
current_y += line_height

draw_stat(draw, start_x, current_y, "> TOTAL COMMITS (PAST YEAR): ", total_commits, font_body)
current_y += line_height

draw_stat(draw, start_x, current_y, "> TOTAL PRS: ", total_prs, font_body)
current_y += line_height

draw_stat(draw, start_x, current_y, "> TOTAL ISSUES: ", total_issues, font_body)
current_y += line_height

draw_stat(draw, start_x, current_y, "> MERGED PR PERCENTAGE: ", f"{pr_percentage}%", font_body)
current_y += line_height + 15  

# Top Languages Section
draw.text((start_x, current_y), "> TOP USED LANGUAGES:", fill=COLOR_WHITE, font=font_body)
current_y += line_height

for lang in top_language_names:
    draw.text((start_x + 20, current_y), f"- {lang}", fill=COLOR_GOLD, font=font_body)
    current_y += 25

image.save("./assets/Statistics_Live.png")
