import multiprocessing
from random import randint
from time import sleep


def worker(*args):
    duration = randint(1, 10)
    sleep(duration)
    print(f'Processing file {args} with {multiprocessing.current_process().name}; Sleeped {duration} sec')


class CSVHandler(multiprocessing.Process):
    def __init__(self, files: list[str] | tuple[str] = None, worker: callable = None, timeout: int = 1):
        super().__init__()
        self.files = files
        self.worker = worker
        self.timeout = timeout

    def run(self):
        processes = [multiprocessing.Process(target=self.worker, args=(file,), name=file) for file in self.files]
        for pr in processes:
            pr.start()
        sleep(self.timeout)
        for pr in multiprocessing.active_children():
            print(f'{pr.name} processing timeout exceeded')
            pr.terminate()
            sleep(0.1)
            pr.close()


if __name__ == '__main__':
    filenames = ['file_1.csv', 'file_2.csv', 'file_3.csv']
    csv_worker = CSVHandler(filenames, worker)
    csv_worker.timeout = 5
    csv_worker.start()
