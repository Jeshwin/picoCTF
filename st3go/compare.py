#!/usr/bin/python3

from PIL import Image

flag = Image.open("pico.flag.png") # 585x172
(w, h) = flag.size
colors = [0 for i in range(w*h)]

def rgb_to_hex(rgb):
    return '%02x%02x%02x%02x' % rgb


for y in range(0, h):
    for x in range(0, w):
        # print(str(x) + ', ' + str(y))
        color = rgb_to_hex(flag.getpixel( (x,y) ))[:-2]
        colors[(y * w) + x] = color
        # print('Hex Color: #{0}'.format(color))

colors = sorted(list(set(colors)))
print(colors)

