from threading import Thread


class BigJob(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        result = 1
        for i in range(1, self.n + 1):
            result *= i
        print(result)


if __name__ == '__main__':
    job = BigJob(100000)
    job.start()
