from PIL import Image

width = 3840
height = 2160

image = Image.new("RGB", size=(width, height))

python = "x, y, color.txt"
cpp_serial_release = "/mnt/c/Users/kaganndemirr/mandelbrot_set/MandelbrotSetSerial/cmake-build-release-wsl/x, y, color.txt"
cpp_parallel_release = "/mnt/c/Users/kaganndemirr/mandelbrot_set/MandelbrotSetForkWritingFile/cmake-build-release-wsl/x, y, color.txt"

with open(cpp_parallel_release, "r") as pixel_file:
    information = pixel_file.readlines()

for each_pixel in information[:-1]:
    image.putpixel((int(each_pixel.split(" ")[0]), int(each_pixel.split(" ")[1])), (int(each_pixel.split(" ")[2][:-1]) % 4 * 64, int(each_pixel.split(" ")[2][:-1]) % 8 * 32, int(each_pixel.split(" ")[2][:-1]) % 16 * 16))

image.save(str(width) + "_" + str(height) + ".png")