from threading import Thread, Lock

pos = 1000


class UpdatePos(Thread):
    def __init__(self, lock, offset):
        super().__init__()
        self.lock = lock
        self.offset = offset

    def run(self):
        global pos
        for i in range(1000000):
            self.lock.acquire()
            pos += self.offset
            self.lock.release()


if __name__ == '__main__':
    lock = Lock()
    t1 = UpdatePos(lock, 100)
    t2 = UpdatePos(lock, -100)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(pos)
