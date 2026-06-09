from email.mime import image

from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')

print(img)
print(img.format)
print(img.size)
print(img.mode)

filtered_img = img.filter(ImageFilter.BLUR) # SMOOTH, SHARPEN
filtered_img.save('blur.png', 'png')

filtered_img = img.convert('L')
filtered_img.save('gray.png', 'png')
filtered_img.rotate(90).show()
filtered_img.resize((300,300)).show()
box = (100, 100, 400, 400)
filtered_img.crop(box).show()

astro = Image.open(('./astro.jpg'))
print(astro.size)
astro.resize((400,400)).show()