from PIL import Image

img = Image.open('pokedex/pikachu.jpg')

print(img)
print(img.format)
print(img.size)
print(img.mode)
print(dir(img))

# This is how you can apply filters to photos using Python
# Photos should be saved as '.png' since this format supports filters
from PIL import Image, ImageFilter

img = Image.open('pokedex/charmander.jpg')

filtered_img = img.filter(ImageFilter.BLUR)     # Blur Image
filtered_img.save("blur.png", 'png')            # Saves as new png file
filtered_img = img.filter(ImageFilter.SMOOTH)   # Smooth Image
filtered_img.save("smooth.png", 'png')          # Saves as new png file
filtered_img = img.convert('L')                 # Black & White Image
filtered_img.save("grey.png", 'png')            # Saves as new png file
crooked = filtered_img.rotate(90)               # Rotate Image
crooked.save("crooked.png", 'png')              # Saves as new png file
resized = filtered_img.resize((300, 300))       # Resize Image
resized.save("resized.png", 'png')              # Saves as new png file
box = (100, 100, 400, 400)                      # Create a box
region = filtered_img.crop(box)                 # Crop image to fit in the box
region.save("cropped.png", 'png')               # Saves as new png file
#region.show()                                  # Opens img in new window

img2 = Image.open('./astro.jpg')
img2.thumbnail((400, 400))          # Thumbnail resizes image while keeping aspect ratio
img2.save('thumbnail.jpg')          # Saves as new png file
print(img2.size)
