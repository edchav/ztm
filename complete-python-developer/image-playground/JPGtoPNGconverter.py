import sys
import os
#import pdb debugging purposes.
from PIL import Image

# Grab first and second argument
pokedex = sys.argv[1]
newFolder = sys.argv[2]

# check is new/ exists if not create it
if not(os.path.isdir(newFolder)):
    os.mkdir(newFolder)

# loop through pokedex, and convert images to png
for image in os.listdir(pokedex):
    f, e = os.path.splitext(image)
    newImage = f + '.png'
    if image != newImage:
        try:
            with Image.open(os.path.join(pokedex, image)) as img:
                img.save(os.path.join(newFolder, newImage))
        except OSError:
            print("cannot convert", image)
#pdb.set_trace()
