import json
from PIL import Image, ImageDraw, ImageFont
import requests

# data = {"author_url":"https:\/\/www.youtube.com\/channel\/UCZE6iNWl5dDd8hj88wAAmYw","title":"SPA server MVP","version":"1.0","width":459,"provider_url":"https:\/\/www.youtube.com\/","author_name":"M Hasbini","provider_name":"YouTube","height":344,"thumbnail_height":360,"thumbnail_url":"https:\/\/i.ytimg.com\/vi\/ChlK4vq8Nwk\/hqdefault.jpg","type":"video","thumbnail_width":480,"html":"\u003ciframe width=\"459\" height=\"344\" src=\"https:\/\/www.youtube.com\/embed\/ChlK4vq8Nwk?feature=oembed\" frameborder=\"0\" allow=\"accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen\u003e\u003c\/iframe\u003e"}

# https://i.ytimg.com/vi/ChlK4vq8Nwk/maxresdefault.jpg
# https://i.ytimg.com/vi/ChlK4vq8Nwk/hqdefault.jpg

# import ipdb; ipdb.set_trace();

# print("test")

filename = "maxresdefault.jpg"

fnt = ImageFont.truetype("fontm.ttf", 14)
fnt_b = ImageFont.truetype("fontm.ttf", 18)
img = Image.open(filename)

play = Image.open("play.png")

w, h = img.size

draw = ImageDraw.Draw(img)

img.paste(play, (int((w - 68) / 2), int((h - 48) / 2)), play)

shadow = Image.open("shadow.png").resize((w, h * 2))

img.paste(shadow, (0, 0), shadow)

clock = Image.open("clock.png")
img.paste(clock, (w - 160, 10), clock)
s = "Watch later"
draw.text(
    (w - 160 - int(len(s) / 2) - 15, 10 + 36 + 5), s, font=fnt, fill=(255, 255, 255)
)

arrow = Image.open("arrow.png")
img.paste(arrow, (w - 70, 10), arrow)
s = "Share"
draw.text(
    (w - 70 - int(len(s) / 2) + 2, 10 + 36 + 5), s, font=fnt, fill=(255, 255, 255)
)


name = Image.open("name.png")
img.paste(name, (20, 10 + 15), name)
s = "SPA server MVP"
draw.text((75, 10 + int((36 + 5) / 2)), s, font=fnt_b, fill=(255, 255, 255))

img.show()

# img.save('out.png')

# os.system('open out.png')
