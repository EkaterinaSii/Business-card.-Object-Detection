
from PIL import Image
import os

starting_point_for_numering = 0 
wrong_type = 0
in_folder = "business_cards/images/valid/"
out_folder = "business_cards/images/valid/"


for count, filename in enumerate(os.listdir(in_folder)):
    img = Image.open(f"{in_folder}/{filename}")
    img_w, img_h = img.size
    if img.size != (1280,1280):
        background = Image.new("RGB", (1280,1280), (0, 0, 0, 1))
        bg_w, bg_h = background.size
        offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
        background.paste(img,offset)
        #background.show()
        background.save(f"{out_folder}/{filename}")

