from threading import Thread

pos = 1000


class UpdatePos(Thread):
    def __init__(self, offset):
        super().__init__()
        self.offset = offset

    def run(self):
        global pos
        for i in range(1000000):
            pos += self.offset


if __name__ == '__main__':
    t1 = UpdatePos(100)
    t2 = UpdatePos(-100)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(pos)
