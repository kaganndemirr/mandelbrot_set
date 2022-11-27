import os
import time

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

    width, height = 128, 128
    x1 = -2.0
    x2 = 2.0
    y1 = -2.0
    y2 = 2.0

    max_iter = 1_000_000

    fork_number = 64

    pipe_list = []

    for pipe_number in range(fork_number):
        pipe_list.append(list(os.pipe()))

    shutdown_list = []
    p_id = 0

    for process_number in range(fork_number):
        p_id = os.fork()
        if p_id < 0:
            print("Child {} failed!".format(process_number))
            exit(-1)
        elif p_id == 0:
            information = str()
            for x in range(process_number * (width // fork_number), (process_number + 1) * (width // fork_number)):
                zx = x * (x2 - x1) / width + x1
                for y in range(height):
                    zy = y * (y2 - y1) / height + y1
                    color = escape_time_algorithm(complex(zx, zy), max_iter)
                    information += str(x) + " " + str(y) + " " + str(color) + "\n"

            if os.write(pipe_list[process_number][1], bytes(information, encoding)) < 0:
                print("Writing color failed!")
                exit(-1)

            exit(0)

        else:
            shutdown_list.append(p_id)

    if p_id > 0:

        for process_number in range(fork_number):
            information = os.read(pipe_list[process_number][0], 9_999_999_999)


        for i_pid in shutdown_list:
            os.waitpid(i_pid, 0)

        end = time.time()
        print("Elapsed time = {}s.".format(end - start))
