from PIL import Image, ImageFont, ImageDraw
from datetime import datetime
from pytz import timezone


def get_current_time():
    return datetime.now(timezone('Asia/Tashkent')).strftime('%H:%M')


def generate_image(text):
    im = Image.open("mirfozil.png")
    W, H = im.size
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(font='resources/ds-digit.ttf', size=190)
    wt, ht = draw.textsize(text, font=font)
    draw.text(((W - wt) / 2, (H - ht) / 2 ), text, font=font, fill='#FF00F7')
    im.save('time_image.jpg')
