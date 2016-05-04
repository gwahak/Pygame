import random
import math

import time


def calc_pi(point_count):
    in_circle_count = 0
    for i in range(point_count):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        dist2 = x ** 2 + y ** 2
        if dist2 <= 1 ** 2:
            in_circle_count += 1
    return in_circle_count * 4 / point_count


def get_error_rate(found, theory):
    return abs(found - theory) / theory


def main():
    start = time.process_time()
    ans = calc_pi(1000000)
    end = time.process_time()

    print("PI = {0:.6f}({1:.2f}%)".format(ans, get_error_rate(ans, math.pi) * 100))
    print(end - start)


if __name__ == '__main__':
    main()
