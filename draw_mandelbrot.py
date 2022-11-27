from PIL import Image

width = 1280
height = 720

image = Image.new("RGB", size=(width, height))


with open("x, y, color.txt", "r") as pixel_file:
    information = pixel_file.readlines()

for each_pixel in information[:-1]:
    image.putpixel((int(each_pixel.split(" ")[0]), int(each_pixel.split(" ")[1])), (int(each_pixel.split(" ")[2][:-1]) % 4 * 64, int(each_pixel.split(" ")[2][:-1]) % 8 * 32, int(each_pixel.split(" ")[2][:-1]) % 16 * 16))

image.save(str(width) + "_" + str(height) + ".png")