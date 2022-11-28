from PIL import Image
from PIL import ImageDraw, ImageFont

img=Image.open('gol.jpg')
img_Draw=ImageDraw.Draw(img)

# use a truetype font
font = ImageFont.truetype("Gidole-Regular.ttf", 150)
img_Draw.text((300,550),"""this is the power of python for using font you have to 
dawnload it and put it next to the file""", fill=(255,0,0),font=font)
img.save('photow.jpg')