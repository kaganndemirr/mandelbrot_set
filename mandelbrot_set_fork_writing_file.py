import os
import time

from PIL import Image

def escape_time_algorithm(c, m):
    z = complex(0, 0)
    for i in range(m):
        z = z ** 2 + c
        if abs(z) > 2:
            return i
    return 0


if __name__ == "__main__":

    start = time.time()

    encoding = 'utf-8'

    width, height = 1280, 720
    x1 = -2
    x2 = 2
    y1 = -2
    y2 = 2

    pixel_file = open("x, y, color.txt", "w")

    max_iter = 1_000

    fork_number = 128

    shutdown_list = []
    p_id = 0

    for process_number in range(fork_number):
        p_id = os.fork()
        if p_id < 0:
            print("Child {} failed!".format(process_number))
            exit(-1)
        elif p_id == 0:
            for x in range(process_number * (width // fork_number), (process_number + 1) * (width // fork_number)):
                zx = x * (x2 - x1) / width + x1
                for y in range(height):
                    zy = y * (y2 - y1) / height + y1
                    color = escape_time_algorithm(complex(zx, zy), max_iter)
                    pixel_file.write(str(x) + " " + str(y) + " " + str(color) + "\n")

            exit(0)

        else:
            shutdown_list.append(p_id)

    if p_id > 0:

        pixel_file.close()

        for i_pid in shutdown_list:
            os.waitpid(i_pid, 0)

        end = time.time()
        print("Elapsed time = {}s.".format(end - start))