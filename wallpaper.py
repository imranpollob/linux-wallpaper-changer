import requests
import os
import random

user_input = input('Press Enter for a random photo, or type a name and press Enter :D\n')

response = requests.get("https://pixabay.com/api/?key=10229979-e52bc85fc62f5e3ee13ee7e29&q=" + user_input + "&per_page=100&min_width=1440&min_height=900")

data = response.json()
total_hits = len(data["hits"])

if total_hits == 0:
    print("Sorry!! No photos for your type")
else:
    img_link = data["hits"][random.randint(1, total_hits)]["largeImageURL"]
    print("Sit Tight!!!")
    os.system("gsettings set org.gnome.desktop.background picture-uri " + img_link)