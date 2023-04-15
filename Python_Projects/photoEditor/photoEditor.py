# Photo Editor
# Edits photos that are in the imgs folder
# Make sure you are in the virtual environment and have Pillow installed

from PIL import Image, ImageFilter, ImageEnhance
import os

print("Welcome to the Photo Editor")
print("Type 1 for B&W")
print("Type 2 for Sketch")
userImput = input("What edit do you want?")

path = "./imgs"
pathOut = "./editedImgs"

# 1 = B&W, Creates a Black and White image
if userImput == "1":
    for filename in os.listdir(path):
        img = Image.open(f"{path}/{filename}")

        edit = img.filter(ImageFilter.SHARPEN).convert('L')

        factor = 1.5
        enhancer = ImageEnhance.Contrast(edit)
        edit = enhancer.enhance(factor)

        cleanName = os.path.splitext(filename)[0]

        edit.save(f"{pathOut}/{cleanName}.png", 'png')

    print("Done")

# 2 = Sketch, Creates a Sketch image
elif userImput == "2":
    for filename in os.listdir(path):
        img = Image.open(f"{path}/{filename}")

        edit = img.filter(ImageFilter.SHARPEN)

        factor = 1.5
        enhancer = ImageEnhance.Contrast(edit)
        edit = enhancer.enhance(factor)

        edit = edit.filter(ImageFilter.EMBOSS)

        cleanName = os.path.splitext(filename)[0]

        edit.save(f"{pathOut}/{cleanName}.png", 'png')

    print("Done")

#  emboss = img_gray_smooth.filter(ImageFilter.EMBOSS)