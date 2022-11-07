from PIL import Image, ImageFilter

img = Image.open('img/pokedex/pikachu.jpg')
print(img.format)
print(img.size)

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png","png")
filtered_img2 = img.convert('L')
filtered_img2.save("grey.png","png")
# resize = filtered_img2.resize((300,300))
# resize.save("grey.png","png")
# crooked = filtered_img2.rotate(180)
# crooked.save("grey.png","png")
# filtered_img2.show()
box = (100,100,400,400)
region = filtered_img2.crop(box)
region.save("grey.png","png")

img2 = Image.open('img/astro.jpg')
img2.thumbnail((400,400))
img2.save('thumbnail.jpg')