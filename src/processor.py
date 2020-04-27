import json
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO


def embed_image(video_id):
    image = get_image(video_id)
    w, h = image.size
    title = get_title(video_id)

    insert_play_button(image, w, h)

    insert_header(image, w, h, title)

    byte_arr = BytesIO()
    image.save(byte_arr, format="PNG")
    byte_arr = byte_arr.getvalue()

    return byte_arr


def get_title(video_id):
    response = requests.get(
        f"https://www.youtube.com/oembed?format=json&url=https://www.youtube.com/watch?v={video_id}"
    )

    return response.json()["title"]


def get_image(video_id):
    url = f"https://i.ytimg.com/vi/{video_id}/sddefault.jpg"
    response = requests.get(url)

    return Image.open(BytesIO(response.content))


def insert_play_button(image, w, h):
    play = Image.open("./src/static/play.png")

    image.paste(play, ((w - 68) // 2, (h - 48) // 2), play)


def insert_header(image, w, h, title):
    insert_shadow(image, w, h)
    insert_watch_later(image, w, h)
    insert_share(image, w, h)
    insert_title(image, w, h, title)


def insert_shadow(image, w, h):
    shadow = Image.open("./src/static/shadow.png").resize((w, h * 2))

    image.paste(shadow, (0, 0), shadow)


def insert_watch_later(image, w, h):
    clock = Image.open("./src/static/clock.png")
    image.paste(clock, (w - 160, 10), clock)
    text = "Watch later"
    ImageDraw.Draw(image).text(
        (w - 160 - len(text) // 2 - 15, 10 + 36 + 5),
        text,
        font=ImageFont.truetype("./src/static/fontm.ttf", 14),
        fill=(255, 255, 255),
    )


def insert_share(image, w, h):
    arrow = Image.open("./src/static/arrow.png")
    image.paste(arrow, (w - 70, 10), arrow)
    text = "Share"
    ImageDraw.Draw(image).text(
        (w - 70 - len(text) // 2 + 2, 10 + 36 + 5),
        text,
        font=ImageFont.truetype("./src/static/fontm.ttf", 14),
        fill=(255, 255, 255),
    )


# make sure to render arabic font as well
def insert_title(image, w, h, title):
    name = Image.open("./src/static/name.png")
    image.paste(name, (20, 10 + 15), name)
    ImageDraw.Draw(image).text(
        (75, 10 + (36 + 5) // 2),
        title,
        font=ImageFont.truetype("./src/static/fontm.ttf", 18),
        fill=(255, 255, 255),
    )
