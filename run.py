import colorsys
import json
from PIL import Image, ImageDraw
from PIL import ImageFont
from metadata_json_generator import get_data

size = (512, 512)

TOTAL = 10_000

for _ in range(TOTAL):
    rgb = colorsys.hls_to_rgb(_*3.6, 0.4, 0.4)
    r, g, b = [int(255 * c) for c in rgb]

    # print(round(_ * 3.6), rgb, r, g, b)
    img = Image.new(mode="RGB", size=size, color=(r, g, b))

    d = ImageDraw.Draw(img)

    fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 216)
    d.text((0, 0), f"{_}", font=fnt, align='center')

    img.save(f'/tmp/{_}.png', 'png')
    print(_)
    with open(f'/tmp/{_}.json', 'w') as file_json:
        file_json.write(json.dumps(get_data(_, TOTAL)))
