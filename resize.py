import os

from PIL import Image

# images = os.listdir("img")

# a = 0

# for i in images:
#     img = Image.open("img/" + i)
#     img.thumbnail(
#         (300, 300),
#         Image.ANTIALIAS
#     )
#     img.save("optimized/" + i)
#     a = a + 1
#     print(a)

img = Image.open("LOGOS WB/152X152.png")

img.thumbnail(
    (152, 152),
    Image.ANTIALIAS
)


img.save("LOGOS WB/optimized/152X152.png")

# images = os.listdir("LOGOS WB")

# for i in images:
#     width, height = i[:len(i)-4].split('X')
#     width = int(width)
#     height = int(height)
#     img = Image.open("LOGOS WB/" + i)
#     img.thumbnail(
#         (width, height),
#         Image.ANTIALIAS
#     )
#     img.save("LOGOS WB/optimized/" + i)

