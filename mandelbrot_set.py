import time

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


max_iter = 1_000_000
start = time.time()
for x in range(width):
    zx = x * (x2 - x1) / width + x1
    for y in range(height):
        zy = y * (y2 - y1) / height + y1
        color = escape_time_algorithm(complex(zx, zy), max_iter)

end = time.time()

print("Elapsed time = {}s.".format(end - start))


