import time

def escape_time_algorithm(c, m):
    z = complex(0, 0)
    for i in range(m):
        z = z ** 2 + c
        if abs(z) > 2:
            return i
    return 0


width, height = 1280, 720
x1 = -2.0
x2 = 2.0
y1 = -2.0
y2 = 2.0

pixel_file = open("x, y, color.txt", "w")

max_iter = 10-000
start = time.time()
for x in range(width):
    zx = x * (x2 - x1) / width + x1
    for y in range(height):
        zy = y * (y2 - y1) / height + y1
        color = escape_time_algorithm(complex(zx, zy), max_iter)
        pixel_file.write(str(x) + " " + str(y) + " " + str(color) + "\n")

pixel_file.close()

end = time.time()

print("Elapsed time = {}s.".format(end - start))


