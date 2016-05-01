import threading
import time


def big_calc_job(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(result)

if __name__ == '__main__':

    # 不用 thread
    print('=== start ===')
    big_calc_job(100000)
    print('=== end ===')

    # # 使用 thread
    # print('=== start ===')
    # job = threading.Thread(target=big_calc_job, args=(100000,))
    # job.start()
    # # job.join()
    # print('=== end ===')

    # # 檢查 thread 是否還在運行
    # print('=== start ===')
    # job = threading.Thread(target=big_calc_job, args=(100000,))
    # job.start()
    # while job.is_alive():
    #     print('Waiting...')
    #     time.sleep(1)
    # print('=== end ===')
