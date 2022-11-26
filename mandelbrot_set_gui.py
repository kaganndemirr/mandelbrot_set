import time

from PIL import Image


def escape_time_algorithm(c, m):
    z = complex(0, 0)
    for i in range(m):
        z = z ** 2 + c
        if abs(z) > 2:
            return i
    return 0


width, height = 128, 128
x1 = -2.0
x2 = 2.0
y1 = -2.0
y2 = 2.0

image = Image.new("RGB", size=(width, height))


max_iter = 1_000_000
start = time.time()
for x in range(width):
    zx = x * (x2 - x1) / width + x1
    for y in range(height):
        zy = y * (y2 - y1) / height + y1
        color = escape_time_algorithm(complex(zx, zy), max_iter)
        # print("{}, {}, {}".format(x, y, color))
        image.putpixel((x, y), (color % 4 * 64, color % 8 * 32, color % 16 * 16))
end = time.time()

print(end - start)
image.save(str(width) + "_" + str(height) + "_" + str(max_iter) + "_serial.png")


