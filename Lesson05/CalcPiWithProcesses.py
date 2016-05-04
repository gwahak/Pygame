import random
import time

import math
from multiprocessing.pool import Pool

from Lesson05.CalcPi import get_error_rate


def calc_pi(point_count):
    in_circle_count = 0
    for i in range(point_count):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        dist = x ** 2 + y ** 2
        if dist <= 1 ** 2:
            in_circle_count += 1
    return in_circle_count


def calc_pi_with_processes(point_count):
    processes_count = 4
    result = None
    with Pool(processes=processes_count) as pool:
        result = pool.map(calc_pi, [point_count // processes_count] * 4)
    return sum(result) * 4 / point_count


def main():
    start = time.process_time()
    ans = calc_pi_with_processes(1000000)
    end = time.process_time()

    print("PI = {0:.6f}({1:.2f}%)".format(ans, get_error_rate(ans, math.pi) * 100))
    print(end - start)


if __name__ == '__main__':
    main()
