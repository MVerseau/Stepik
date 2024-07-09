import multiprocessing
import sys
from threading import Timer
import time
from random import randint


class ParallelExecuter(multiprocessing.Process):
    def __init__(self, tasks: list | tuple, arg: list | tuple, timeout: int | float = None, *args,
                 **kwargs):
        super().__init__()
        self.log = []
        self.timeout = timeout
        self.task = tasks
        self.arg = arg

    @staticmethod
    def termination():
        for pr in multiprocessing.active_children():
            pr.terminate()
            pr.join()
            # print(f'{pr.name}: {pr.exitcode}')

    def run(self):
        processes = [multiprocessing.Process(target=item[0], args=(item[1],), name=item[0].__name__) for item in
                     zip(self.task, self.arg)]
        for pr in processes:
            pr.start()
        tm = Timer(self.timeout, self.termination)
        tm.start()
        tm.join()
        for pr in processes:
            self.log.append(
                f'Process {pr.name}: completed successfully' if pr.exitcode == 0 else f'Process {pr.name}: processing timeout exceeded')
        for pr in multiprocessing.active_children():
            pr.close()
        print(self.log)

    def execute(self):
        self.start()


def func(arg):
    duration = randint(0, 10)
    # print(f'{multiprocessing.current_process().name}; to sleep {duration} sec')
    time.sleep(duration)
    return print(arg)


def main():
    cl=ParallelExecuter((func, func, func, func), ('Hi', 000, dict(), (5)), timeout=5)
    cl.execute()
    cl.join()
    print(time.time()-start_time)


if __name__ == '__main__':

    start_time=time.time()
    main()